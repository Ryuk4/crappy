﻿import time

import crappy2

crappy2.blocks.MasterBlock.instances = []  # Init masterblock instances

if __name__ == '__main__':
    try:
        # Creating objects

        instronSensor = crappy2.sensor.ComediSensor(channels=[0], gain=[-48.8], offset=[0])
        t, F0 = instronSensor.get_data(0)
        print "offset=", F0
        instronSensor = crappy2.sensor.ComediSensor(channels=[0], gain=[-48.8], offset=[-F0])
        biotensTech = crappy2.technical.Biotens(port='/dev/ttyUSB0', size=25)

        # Creating blocks

        compacter_effort = crappy2.blocks.Compacter(150)
        save_effort = crappy2.blocks.Saver("/home/biotens/Bureau/Annie/test_lampe/rat_effort_1.txt")
        graph_effort = crappy2.blocks.Grapher("dynamic", ('t(s)', 'F(N)'))

        compacter_extenso = crappy2.blocks.Compacter(90)
        save_extenso = crappy2.blocks.Saver("/home/biotens/Bureau/Annie/test_lampe/rat_extenso_1.txt")
        graph_extenso = crappy2.blocks.Grapher("dynamic", ('t(s)', 'Exx(%)'), ('t(s)', 'Eyy(%)'))

        effort = crappy2.blocks.MeasureComediByStep(instronSensor, labels=['t(s)', 'F(N)'], freq=150)
        extenso = crappy2.blocks.VideoExtenso(camera="Ximea", white_spot=False,
                                              labels=['t(s)', 'Lx', 'Ly', 'Exx(%)', 'Eyy(%)'], display=True)

        # signalGenerator=crappy2.blocks.SignalGenerator(path=[{"waveform":"hold","time":0},
        # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.05,'F(N)'],"upper_limit":[90,'Eyy(%)']}],
        # send_freq=400,repeat=False,labels=['t(s)','signal'])
        # example of path:[{"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.05,'F(N)'],
        # "upper_limit":[i,'Eyy(%)']} for i in range(10,90,10)]

        signalGenerator = crappy2.blocks.SignalGenerator(path=[
            {"waveform": "limit", "gain": 1, "cycles": 2, "phase": 0, "lower_limit": [0.02, 'F(N)'],
             "upper_limit": [90, 'F(N)']}],
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[10,'Eyy(%)']},
            # {"waveform":"hold","time":120},
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[20,'Eyy(%)']},
            # {"waveform":"hold","time":120},
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[30,'Eyy(%)']},
            # {"waveform":"hold","time":120},
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[40,'Eyy(%)']},
            # {"waveform":"hold","time":120},
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[50,'Eyy(%)']},
            # {"waveform":"hold","time":120},
            # {"waveform":"limit","gain":1,"cycles":0.5,"phase":0,"lower_limit":[0.02,'F(N)'],"upper_limit":[90,'F(N)']}],
            send_freq=5, repeat=False, labels=['t(s)', 'signal', 'cycle'])

        biotens = crappy2.blocks.CommandBiotens(biotens_technicals=[biotensTech], speed=5)
        compacter_position = crappy2.blocks.Compacter(5)
        save_position = crappy2.blocks.Saver("/home/biotens/Bureau/Annie/test_lampe/rat_position_1.txt")

        # Creating links

        link1 = crappy2.links.Link()
        link2 = crappy2.links.Link()
        link3 = crappy2.links.Link()
        link4 = crappy2.links.Link()
        link5 = crappy2.links.Link()
        link6 = crappy2.links.Link()
        link7 = crappy2.links.Link()
        link8 = crappy2.links.Link()
        link9 = crappy2.links.Link()
        link10 = crappy2.links.Link()
        link11 = crappy2.links.Link()

        # Linking objects

        effort.add_output(link1)
        effort.add_output(link6)

        extenso.add_output(link2)
        extenso.add_output(link3)

        signalGenerator.add_input(link1)
        signalGenerator.add_input(link2)
        signalGenerator.add_output(link9)

        biotens.add_input(link9)
        biotens.add_output(link10)

        compacter_effort.add_input(link6)
        compacter_effort.add_output(link7)
        compacter_effort.add_output(link8)

        save_effort.add_input(link7)

        graph_effort.add_input(link8)

        compacter_extenso.add_input(link3)
        compacter_extenso.add_output(link4)
        compacter_extenso.add_output(link5)

        save_extenso.add_input(link4)

        graph_extenso.add_input(link5)

        compacter_position.add_input(link10)
        compacter_position.add_output(link11)

        save_position.add_input(link11)
        # Starting objects

        t0 = time.time()
        for instance in crappy2.blocks.MasterBlock.instances:
            instance.t0 = t0

        for instance in crappy2.blocks.MasterBlock.instances:
            instance.start()

    # Waiting for execution

    # Stopping objects

    except (Exception, KeyboardInterrupt) as e:
        print "Exception in main :", e
        # for instance in crappy2.blocks._meta.MasterBlock.instances:
        # instance.join()
        for instance in crappy2.blocks.MasterBlock.instances:
            try:
                instance.stop()
                print "instance stopped : ", instance
            except Exception as e:
                print e

                # try:
                # while True:
                # print instronSensor.get_data(0)[1]
                # time.sleep(0.1)
                # except KeyboardInterrupt:
                # pass
