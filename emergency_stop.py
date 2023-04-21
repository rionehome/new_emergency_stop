#!/usr/bin/env python

import rospy
import serial
import time
import sys

class Emergency():
    def __init__(self):
        rospy.init_node("emergency_stop")
        self.main()
    
    def main(self):
        ser = serial.Serial("/dev/ttyACM0", 9600)
        time.sleep(1)
        while True:
            try:
                res = ser.readline()
                if len(res) < 0:
                    pass
                else:
                    if res[0] == "1":
                        rospy.loginfo("Emergency button pressed!!")
                        sys.exit(0)
            except KeyboardInterrupt():
                print("----- finish -----")
                ser.close()

if __name__=='__main__':
    emergency = Emergency()