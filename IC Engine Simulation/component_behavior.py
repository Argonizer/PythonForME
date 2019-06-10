import math

def toDegrees(rad):
    return rad / math.pi * 180

def piston_behavior(crank_angle, object, crank_radius):
    y_pos = object.pivot_y +  crank_radius * math.cos(crank_angle)
    object.set_y(y_pos)

def crankshaft_behavior(crank_angle, object):
    object.set_angle(crank_angle)

def connecting_rod_behavior(crank_angle, object, crank_radius):
    y_pos = object.pivot_y + crank_radius * math.cos(crank_angle)
    object.set_y(y_pos)
    big_end_offset = crank_radius * math.sin(crank_angle)
    angle = math.atan(big_end_offset/185)
    object.set_angle(toDegrees(angle))

def camgear_behavior(cam_angle, object, offset_angle = 0):
    angle = (cam_angle + 3.6) * -1
    object.set_angle(angle + offset_angle)

def pushrod_behavior(cam_angle, object, rise_angle, return_angle):
    if cam_angle > rise_angle and cam_angle < rise_angle + 10:
        y_pos = object.pivot_y - 10  + (cam_angle - rise_angle)
    elif cam_angle >= rise_angle + 10 and cam_angle < return_angle - 10:
        y_pos = object.pivot_y - 10
    elif cam_angle >= return_angle - 10 and cam_angle < return_angle:
        y_pos = object.pivot_y + 10 - (return_angle - cam_angle)
    else:
        y_pos = object.pivot_y
    object.set_y(y_pos)

def rocker_behavior(cam_angle, object, rise_angle, return_angle, factor):
    if cam_angle > rise_angle and cam_angle < rise_angle + 10:
        angle = (cam_angle - rise_angle)/2 * factor
    elif cam_angle >= return_angle - 10 and cam_angle <= return_angle:
        angle = (cam_angle - return_angle)/2 * factor
    elif cam_angle >= rise_angle + 10 and cam_angle <= return_angle - 10:
        angle = -10/2 * factor
    else:
        angle = 0
    object.set_angle(angle)

def valve_behavior(cam_angle, object, rise_angle, return_angle):
    if cam_angle > rise_angle and cam_angle < rise_angle + 10:
        y_pos = object.pivot_y + 10  + (cam_angle - rise_angle)
    elif cam_angle >= rise_angle + 10 and cam_angle < return_angle - 10:
        y_pos = object.pivot_y + 10
    elif cam_angle >= return_angle - 10 and cam_angle < return_angle:
        y_pos = object.pivot_y + 10 - (return_angle - cam_angle)
    else:
        y_pos = object.pivot_y
    object.set_y(y_pos)

