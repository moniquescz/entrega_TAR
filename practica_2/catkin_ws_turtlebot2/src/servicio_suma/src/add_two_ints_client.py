#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from servicio_suma.srv import *

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

def calculate_expression_client(a, b, c, d, e):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(a, b, c, d, e)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == "__main__":
    if len(sys.argv) == 6:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        d = int(sys.argv[4])
        e = int(sys.argv[5])
    else:
        print("Usage: %s a b c d e" % sys.argv[0])
        sys.exit(1)
    print(f"Requesting {a} + {b} - ({c} * {d} / {e})")
    print(f"Result: {calculate_expression_client(a, b, c, d, e)}")
