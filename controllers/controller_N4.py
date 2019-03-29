# Import the toolbox #
import toolbox

def control_robot(robot):

	''' this is testing how to do wall algos '''
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

	pass