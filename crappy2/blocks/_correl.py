from ._meta import MasterBlock
from ..technical._correl import TechCorrel
from collections import OrderedDict
from time import time
import numpy as np
from multiprocessing import Process,Pipe


class Correl(MasterBlock):
  """
    This block uses the TechCorrel class (found in crappy[2]/technicals/_correl.py)\
    The first argument is the (y,x) resolution of the image, and you must specify the fields with fields=(...)
    See the docstring of TechCorrel to have more informations about the arguments specific to TechCorrel
    It will try to identify the deformation parameters for each fields. If you use custom fields, use labels=(...) to name the data sent through the link.\
    If no labels are specified, custom fields will be named by their position.
    Note that the reference image is only taken once, when the .start() method is called (after dropping the first image).
    IMPORTANT: This block has an extra method: .init()
    It is meant to compile all the necessary kernels and should be done before starting all the blocks, but AFTER creating, initializing and LINKING them. 
    In short, you simply have to add YourCorrelBlock.init() just before starting all the blocks
    You can omit this but the delay before processing the first images can be long enough to fill a link and crash. Also, the correl block will not send any value before this init is over.
  """
  def __init__(self,img_size,**kwargs):
    MasterBlock.__init__(self)
    self.ready = False
    self.Nfields = kwargs.get("Nfields")
    if self.Nfields is None:
      try:
        self.Nfields = len(kwargs.get("fields"))
      except TypeError:
        print "Error: Correl needs to know the number of fields at init with fields=(.,.) or Nfields=k"
        raise NameError('Missing fields')
    #self.labels = ('t',)+kwargs.get("labels",tuple([str(i+1) for i in range(self.Nfields)])) # If no labels are provided, name them '1', '2', ...

    # Creating the tuple of labels (to name the outputs)
    self.labels = ('t',)
    for i in range(self.Nfields): # If explicitly named with labels=(...)
      if kwargs.get("labels") is not None:
        self.labels += (kwargs.get("labels")[i],)
      elif kwargs.get("fields") is not None and isinstance(kwargs.get("fields")[i],str): # Else if we got a default field as a string, use this string (ex: fields=('x','y','r','exx','eyy'))
        self.labels += (kwargs.get("fields")[i],)
      else: # Custom field and no label given: name it by its position...
        self.labels += (str(i),)

    #print "[Correl Block] output labels:",self.labels
    if kwargs.get("labels") is not None:
      del kwargs["labels"] # We don't need to pass this arg to the TechCorrel class
    pipeProcess,self.pipeClass = Pipe()
    self.process = Process(target=self.main,args=(pipeProcess,img_size),kwargs=kwargs)


  def init(self):
    self.process.start()
    self.pipeClass.recv() # Waiting for init to be over
    self.ready = True

  def start(self):
    if self.ready == False:
      print "[Correl block] WARNING ! This block takes time to init, you must call .init() before .start() JUST before starting all the blocks to do initialize it properly. This way, the program only starts when correl is ready to process incoming data."
      self.init()
    self.pipeClass.send(0) # Notify the process to let it start

  def stop(self):
    self.process.terminate()


  def main(self,pipe,img_size,**kwargs):
    correl = TechCorrel(img_size,**kwargs)
    pipe.send(0) # Sending signal to let init return
    nLoops = 100 # For testing: resets the original images every nLoops loop
    try:
      pipe.recv() # Waiting for the actual start
      #print "[Correl block] Got start signal !"
      t2 = time()-1
      for i in range(2): # Drop the first images
        self.inputs[0].recv()
      correl.setOrig(self.inputs[0].recv().astype(np.float32)) # This is the only time the original picture is set, so the residual may increase if lightning vary or large displacements are reached
      correl.prepare()
      while True:
        t1 = time()
        print "[Correl block] processed",nLoops/(t1-t2),"ips"
        t2 = t1
        #correl.setOrig(self.inputs[0].recv())
        #correl.prepare()
        for i in range(nLoops):
          data = self.inputs[0].recv()
          correl.setImage(data.astype(np.float32))
          t = time()-self.t0
          out = [t]+correl.getDisp().tolist()
          Dout = OrderedDict(zip(self.labels,out))
          for o in self.outputs:
            o.send(Dout)
    except Exception as e:
      print "Error in Correl",e

  def __repr__(self):
    return "Correl block with"+str(self.levels)+"levels"
