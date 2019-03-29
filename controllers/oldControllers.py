def nowalls(robot):
    #Collects packets without walls:
    y = 1 
    for x in range(5): 
        packet_dict = robot.sense_packets(); 
        print str(packet_dict) 
        a = packet_dict[y] 
        print str(a) 
        b = a[0] 
        print str(b) 
        c = a[1] 
        print str(c)

        if b > 0: 
            robot.turn_right(1) 
            robot.step_forward(b) 
            if c > 0: 
                robot.turn_left(1) 
            if c < 0: 
                robot.turn_right(1) 
                c = c * -1 


        if b < 0: 
            robot.turn_left(1) 
            b = b * -1 
            robot.step_forward(b) 
            if c > 0: 
                robot.turn_right(1) 
            if c < 0: 
                robot.turn_left(1) 
                c = c * -1 

        robot.step_forward(c) 
        robot.jump() 
        y = y + 1


