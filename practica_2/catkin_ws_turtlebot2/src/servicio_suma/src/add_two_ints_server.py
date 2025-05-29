#!/usr/bin/env python3

from __future__ import print_function

from servicio_suma.srv import AddTwoInts,AddTwoIntsResponse
import rospy


# def handle_add_two_ints(req):
#     print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
#     return AddTwoIntsResponse(req.a + req.b)

def handle_add_two_ints(req):
    # Evitar división por cero
    if req.e == 0:
        print("Error: División por cero")
        return AddTwoIntsResponse(float('nan'))  
    
    result = req.a + req.b - (req.c * req.d / req.e)
    print(f"Returning [{req.a} + {req.b} - ({req.c} * {req.d} / {req.e}) = {result}]")
    
    return AddTwoIntsResponse(result)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()



if __name__ == "__main__":
    add_two_ints_server()