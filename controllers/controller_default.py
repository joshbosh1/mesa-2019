# IMPORT TOOLBOX #
import toolbox

def control_robot(robot):


    ''' use this section for only no wall levels '''

    # DETECT HOW MANY PACKETS ARE IN THE AREA - SMALL MAP SO THIS CAN BE THE WHOLE TOTAL #
    pdict = robot.sense_packets()
    
    # SET A AS THE TOTAL NUM OF PACKETS #
    a = len(pdict)
    print(a)

    # NAVIGATE TO ALL PACKETS #

    target = 1

    for i in range(0, a):

        toolbox.noWallPackets(robot, target)

        target += 1

    # Detect the location of all vile viruses # 
    z = robot.num_viruses_left()

    target = 0

    for i in range(0, z):
        toolbox.huntVir(robot, target)
        target += 1


    ''' this section is for when there are walls '''



    pass