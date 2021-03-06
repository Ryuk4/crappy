import time

import crappy2
from crappy2.links import Link

crappy2.blocks.MasterBlock.instances = []  # Init masterblock instances
# import alerte_jerome

t0 = time.time()
if __name__ == '__main__':
    try:
        # Creating objects

        # instronSensor=crappy2.sensor.ComediSensor(channels=[1,3],gain=[-3749.3,-3198.9*1.18],offset=[24,13])
        # biaxeTech1=crappy2.technical.Biaxe(port='/dev/ttyS4')
        # biaxeTech2=crappy2.technical.Biaxe(port='/dev/ttyS5')
        # biaxeTech3=crappy2.technical.Biaxe(port='/dev/ttyS6')
        # biaxeTech4=crappy2.technical.Biaxe(port='/dev/ttyS7')
        # axes=[biaxeTech1,biaxeTech2,biaxeTech3,biaxeTech4]

        # Creating blocks
        camera = crappy2.blocks.StreamerCamera("Ximea", numdevice=0, freq=None, save=False,
                                               save_directory="/media/biaxe/SSD1To/Essais_biface_caoutchouc/cam_pc/",
                                               xoffset=0, yoffset=0, width=2048, height=2048)
        displayer = crappy2.blocks.CameraDisplayer(framerate=10)

        link_camera_to_displayer = Link(name="link_camera_to_displayer")

        camera.add_output(link_camera_to_displayer)
        displayer.add_input(link_camera_to_displayer)
        # compacter_effort=crappy2.blocks.Compacter(200)
        # save_effort=crappy2.blocks.Saver("/home/biaxe/Bureau/Publi/effort.txt")
        # graph_effort=crappy2.blocks.Grapher("dynamic",('t(s)','F2(N)'),('t(s)','F4(N)'))
        # camera2=crappy2.blocks.StreamerCamera("Ximea",numdevice=1,freq=10,save=True,save_directory="/media/biaxe/SSD1To/Essais_biface_caoutchouc/cam_arriere/",xoffset=0,yoffset=0,width=2048,height=2048)
        # compacter_extenso=crappy2.blocks.Compacter(100)
        # save_extenso=crappy2.blocks.Saver("/home/corentin/Bureau/extenso_big_spots_non_binarise.txt")
        # graph_extenso=crappy2.blocks.Grapher("dynamic",('t(s)','Exx(%)'),('t(s)','Eyy(%)'))

        # effort=crappy2.blocks.MeasureComediByStep(instronSensor,labels=['t(s)','F2(N)','F4(N)'],freq=200)
        # extenso = crappy2.blocks.VideoExtenso(camera="Ximea",numdevice=0,xoffset=0, yoffset=0, width=2048, height=2048,
        #                                      white_spot=True, labels=['t(s)', 'Exx(%)', 'Eyy(%)'], display=True)

        # compacter_extenso2=crappy2.blocks.Compacter(100)
        # save_extenso2=crappy2.blocks.Saver("/home/corentin/Bureau/extenso_1_spot.txt")
        # graph_extenso2=crappy2.blocks.Grapher("dynamic",('t(s)','Exx(%)'),('t(s)','Eyy(%)'))

        # effort=crappy2.blocks.MeasureComediByStep(instronSensor,labels=['t(s)','F2(N)','F4(N)'],freq=200)
        # extenso2 = crappy2.blocks.VideoExtenso(camera="Ximea", numdevice=1, xoffset=0, yoffset=0, width=2048,
        #                                       height=2048, white_spot=True, labels=['t(s)', 'Exx(%)', 'Eyy(%)'],
        #                                       display=True)

        # signalGenerator=crappy2.blocks.SignalGenerator(path=[{"waveform":"hold","time":3},
        # {"waveform":"limit","cycles":3,"phase":0,"lower_limit":[50,'F(N)'],"upper_limit":[5,'Exx(%)']}],
        # send_freq=400,repeat=True,labels=['t(s)','signal'])

        # signalGenerator=crappy2.blocks.SignalGenerator(path=[{"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[50,'F2(N)'],"upper_limit":[10,'Exx(%)']},
        # {"waveform":"limit","gain":0,"cycles":0.5,"phase":0,"lower_limit":[50,'F4(N)'],"upper_limit":[9.7,'Eyy(%)']},
        # {"waveform":"limit","gain":1,"cycles":0.5,"phase":-np.pi,"lower_limit":[50,'F2(N)'],"upper_limit":[10,'Exx(%)']}],
        # send_freq=400,repeat=True,labels=['t(s)','signal'])
        # signalGenerator=crappy2.blocks.SignalGenerator(path=[{"waveform":"limit","gain":1,"cycles":1,"phase":0,"lower_limit":[10,'F2(N)'],"upper_limit":[1000,'Exx(%)']}],
        # send_freq=400,repeat=True,labels=['t(s)','signal'])

        # signalGenerator_horizontal=crappy2.blocks.SignalGenerator(path=[{"waveform":"limit","gain":1,"cycles":1,"phase":0,"lower_limit":[10,'F2(N)'],"upper_limit":[1000,'Exx(%)']}],
        # send_freq=400,repeat=True,labels=['t(s)','signal'])

        # biotens=crappy2.blocks.CommandBiaxe(biaxe_technicals=[biaxeTech1,biaxeTech2],speed=-200) # vertical
        # horizontal # speed must be <0 for traction
        # biotens_horizontal=crappy2.blocks.CommandBiaxe(biaxe_technicals=[biaxeTech3,biaxeTech4],speed=-200)

        # Creating links

        link1 = crappy2.links.Link()
        # link2=crappy2.links.Link()
        # link6=crappy2.links.Link()

        # link3=crappy2.links.Link()
        # link4=crappy2.links.Link()
        # link5=crappy2.links.Link()


        # Linking objects

        # camera.add_output(link1)
        # effort.add_output(link1)
        # effort.add_output(link12)
        # effort.add_output(link6)

        # extenso.add_output(link2)
        # extenso.add_output(link22)
        # extenso.add_output(link3)
        # extenso2.add_output(link1)

        # signalGenerator.add_input(link1)
        # signalGenerator.add_input(link2)
        # signalGenerator.add_output(link9)

        # signalGenerator_horizontal.add_input(link12)
        # signalGenerator_horizontal.add_input(link22)
        # signalGenerator_horizontal.add_output(link92)

        # biotens.add_input(link9)
        # biotens_horizontal.add_input(link92)

        # compacter_effort.add_input(link6)
        # compacter_effort.add_output(link7)
        # compacter_effort.add_output(link8)

        # save_effort.add_input(link7)

        # graph_effort.add_input(link8)

        # compacter_extenso.add_input(link3)
        # compacter_extenso2.add_input(link1)
        # compacter_extenso.add_output(link4)
        # compacter_extenso.add_output(link5)
        # compacter_extenso2.add_output(link2)
        # compacter_extenso2.add_output(link6)

        # save_extenso.add_input(link4)

        # graph_extenso.add_input(link5)
        # graph_extenso2.add_input(link2)
        # save_extenso2.add_input(link6)

        # Starting objects
        # print "top :",crappy2.blocks._meta.MasterBlock.instances
        t0 = time.time()
        for instance in crappy2.blocks.MasterBlock.instances:
            instance.t0 = t0

        for instance in crappy2.blocks.MasterBlock.instances:
            instance.start()

    # Waiting for execution

    # Stopping objects
    except KeyboardInterrupt:
        print "KEYBOARD INTERRUP RECEIVED IN MAIN"
        for instance in crappy2.blocks.MasterBlock.instances:
            try:
                instance.stop()
            except Exception as e:
                print e

    except Exception as e:
        print "Exception in main :", e
        for instance in crappy2.blocks.MasterBlock.instances:
            try:
                instance.stop()
            except Exception as e:
                print e
