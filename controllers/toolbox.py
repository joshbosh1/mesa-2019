def openSpace(robot):
    robot.step_forward(robot.sense_steps(robot.SENSOR_FORWARD))
    if robot.sense_steps(robot.SENSOR_LEFT) == 0 and robot.sense_steps(robot.SENSOR_RIGHT) != 0:
        robot.turn_right()
    pack = 1
    ## Start PACKET path finding logic ##
    while True:
        # pass packet loc to dict, xy format #
        packets = robot.sense_packets()
        print(packets)
    
        ploc = packets[pack]
        x = ploc[0]
        y = ploc[1]
        print(x)
        print(y)
    
        ## Locate y dir first ##
        if y != 0:
            if y > 0:
                robot.step_forward(y)
                robot.jump()
            if y < 0:
                robot.turn_right(2)
                ty = y * -1
                robot.step_forward(ty)
                robot.jump()

        packets = robot.sense_packets()
        ploc = packets[pack]
        x = ploc[0]
        y = ploc[1]

        ## Locate the x dir now ##
        if x != 0:
            if x > 0:
                robot.turn_right()
                robot.step_forward(x)
                robot.jump()
            if x < 0:
                robot.turn_left()
                tx = x * -1
                robot.step_forward(tx)
                robot.jump()

        pack += 1

def huntVir(robot, target):
    vlist = robot.sense_viruses()
    vloc = vlist[target]
    x = vloc[0]
    y = vloc[1]

    ## Locate y dir first ##
    if y != 0:
        if y > 0:
             robot.step_forward(y)
        if y < 0:
            robot.turn_right(2)
            ty = y * -1
            robot.step_forward(ty)

        ## Locate the x dir now ##
    if x != 0:
        if x > 0:
            robot.turn_right()
            robot.step_forward(x)
        if x < 0:
            robot.turn_left()
            tx = x * -1
            robot.step_forward(tx)

def rightWall(robot):
    #Follows the right wall
    while True:
        f = robot.sense_steps(robot.SENSOR_FORWARD)
        r = robot.sense_steps(robot.SENSOR_RIGHT)
        l = robot.sense_steps(robot.SENSOR_LEFT)

        if r < 1:
            if f >= 1:
                robot.step_forward()
                
            else:
                if l >= 1:
                    robot.turn_left()
                    robot.step_forward()
                else:
                    robot.turn_right(2)
        elif r >= 1:
            robot.turn_right()
            robot.step_forward()
            
def leftWall(robot):
    #Follows the left wall
    while True:
        f = robot.sense_steps(robot.SENSOR_FORWARD)
        r = robot.sense_steps(robot.SENSOR_RIGHT)
        l = robot.sense_steps(robot.SENSOR_LEFT)

        if l < 1:
            if f >= 1:
                robot.step_forward()
            else:
                if r >= 1:
                    robot.turn_right()
                    robot.step_forward()
                else:
                    robot.turn_left(2)
        elif l >= 1:
            robot.turn_left()
            robot.step_forward()

def noWallPackets(robot, packetNum):
    #Without walls:
    stop = 0
    if True:
        packet_dict = robot.sense_packets()
        dist = packet_dict[packetNum] 
        x_dist = dist[0] 
        y_dist = dist[1] 
            
        if x_dist > 0:
            r_dist = robot.sense_steps(robot.SENSOR_RIGHT)
            if r_dist >= x_dist:
                robot.turn_right(1) 
                robot.step_forward(x_dist)
                if y_dist > 0:
                    l_dist = robot.sense_steps(robot.SENSOR_LEFT)
                    if l_dist >= y_dist:
                        robot.turn_left(1)
                    else:
                        stop = 1    
               
                if y_dist < 0:
                    y_dist = y_dist * -1
                    r_dist = robot.sense_steps(robot.SENSOR_RIGHT)
                    if r_dist >= y_dist:
                        robot.turn_right(1)
                    else:
                        stop = 1


        elif x_dist < 0:
            l_dist = robot.sense_steps(robot.SENSOR_LEFT)
            if l_dist >= x_dist * -1:
                robot.turn_left(1) 
                robot.step_forward(x_dist * -1)
                if y_dist > 0:
                    r_dist = robot.sense_steps(robot.SENSOR_RIGHT)
                    if r_dist >= y_dist:
                        robot.turn_right(1)
                    else:
                        stop = 1
                        

            if y_dist < 0:
                y_dist = y_dist * -1
                l_dist = robot.sense_steps(robot.SENSOR_LEFT)
                if l_dist >= y_dist:
                    robot.turn_left(1)
                else:
                    stop = 1
                        
        if stop < 1:
            robot.step_forward(y_dist) 
            robot.jump() 
            packetNum = packetNum + 1
