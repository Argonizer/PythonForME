
#IC Engine 2D Simulator
#author - Akshay Rawal

import pygame
import component
from component_behavior import *

pygame.init()

display_width = 670
display_height = 600

appDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IC Engine 2D Simulator")

piston_img = pygame.image.load("assets/piston.png")
conrod_img = pygame.image.load("assets/connecting_rod.png")
cam_img = pygame.image.load("assets/cam_bw.png")
pushrod_img = pygame.image.load("assets/pushrod.png")
engine_body_img = pygame.image.load("assets/cylinder_block_crank_case.png")
inlet_rockerarm_img = pygame.image.load("assets/rocker_arm.png")
exhaust_rockerarm_img = pygame.transform.flip(inlet_rockerarm_img, True, False)
valve_img = pygame.image.load("assets/valve.png")
crankshaft_img = pygame.image.load("assets/crankshaft.png")
gear40_img = pygame.image.load("assets/gears-40.png")
gear20_img = pygame.image.load("assets/gears-20.png")
combustion_img = pygame.image.load("assets/combustion.png")

Font = pygame.font.SysFont("Futura", 30)

crank_radius = crankshaft_img.get_size()[1]/2 - 34
gear20_width = gear20_img.get_size()[0]
gear40_width = gear40_img.get_size()[0]
gear40_height = gear40_img.get_size()[0]
cam_width = cam_img.get_size()[0]
cam_height = cam_img.get_size()[1]
gear40_offset = (gear40_img.get_size()[1] - gear20_img.get_size()[1])/2
cam_centre_x = (gear40_width - cam_width)/2
cam_centre_y = (gear40_height - cam_height)/2

clock = pygame.time.Clock()

engine_body_x = 30
engine_body_y = 0

component_list = []

def toRadians(deg):
    return deg * math.pi / 180

def toDegrees(rad):
    return rad / math.pi * 180

def cycle(min, max, angle):
    if angle <= min:
        return max
    elif angle >= max:
        return min
    return angle

def create_components_list():
    engine_body_object = component.component()
    engine_body_object._init_("engine_body", engine_body_x, 0, 0, engine_body_img)
    component_list.append(engine_body_object)

    crankgear_object = component.component()
    crankgear_object._init_("crankgear", engine_body_x + 230, 364, 0, gear20_img)
    component_list.append(crankgear_object)

    camgear_object = component.component()
    camgear_object._init_("camgear", engine_body_x + 230 + gear20_width - 15, 364 - gear40_offset, 0, gear40_img)
    component_list.append(camgear_object)

    camgear_object = component.component()
    camgear_object._init_("camgear", engine_body_x + 230 - gear40_width + 15, 364 - gear40_offset, 0, gear40_img)
    component_list.append(camgear_object)

    cam_object = component.component()
    cam_object._init_("inlet_cam", engine_body_x + 230 - gear40_width + cam_centre_y , 364 - gear40_offset + cam_centre_y, 0, cam_img)
    component_list.append(cam_object)

    cam_object = component.component()
    cam_object._init_("exhaust_cam", engine_body_x + 230 + gear20_width + cam_centre_x - 15 , 364 - gear40_offset + cam_centre_y, 0, cam_img)
    component_list.append(cam_object)

    pushrod_object = component.component()
    pushrod_object._init_("exhaust_pushrod", engine_body_x + 230 + gear20_width + cam_centre_x + cam_width/2 - 20, 364 - gear40_offset + cam_centre_y
                          - pushrod_img.get_size()[1], 0,
                      pushrod_img)
    component_list.append(pushrod_object)

    pushrod_object = component.component()
    pushrod_object._init_("inlet_pushrod", engine_body_x + 230 - gear40_width + cam_centre_y + cam_width/2 - 5,
                          364 - gear40_offset + cam_centre_y  - pushrod_img.get_size()[1], 0, pushrod_img)
    component_list.append(pushrod_object)

    crankshaft_object = component.component()
    crankshaft_object._init_("crankshaft", engine_body_x + 195, 330, 0, crankshaft_img)
    component_list.append(crankshaft_object)

    conrod_object = component.component()
    conrod_object._init_("connecting_rod", engine_body_x + 244, 16, 0, conrod_img)
    component_list.append(conrod_object)

    piston_object = component.component()
    piston_object._init_("piston", engine_body_x + 238, 190, 0, piston_img)
    component_list.append(piston_object)

    inlet_rocker_object = component.component()
    inlet_rocker_object._init_("inlet_rocker", engine_body_x + 102, 50, 0, inlet_rockerarm_img)
    component_list.append(inlet_rocker_object)

    exhaust_rocker_object = component.component()
    exhaust_rocker_object._init_("exhaust_rocker", engine_body_x + 337, 50, 0, exhaust_rockerarm_img)
    component_list.append(exhaust_rocker_object)

    inlet_valve_object = component.component()
    inlet_valve_object._init_("inlet_valve", engine_body_x + 244, 50, 0, valve_img)
    component_list.append(inlet_valve_object)

    exhaust_valve_object = component.component()
    exhaust_valve_object._init_("exhaust_valve", engine_body_x + 330, 50, 0, valve_img)
    component_list.append(exhaust_valve_object)

white = (255, 255, 255)
fuel_color = (159, 168, 244)
exhaust_flue_color = (214, 174, 163)
yellow = (255, 255, 0)

crank_angle = 0
cam_angle = 0
piston_y = 0

create_components_list()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break

    crank_angle_increment = 10
    crank_angle += crank_angle_increment
    cam_angle += crank_angle_increment/2
    crank_angle = cycle(0, 360, crank_angle)
    cam_angle = cycle(0, 360, cam_angle)

    inlet_valve_rise_angle = 0
    inlet_valve_return_angle = 105
    exhaust_valve_rise_angle = 247.5
    exhaust_valve_return_angle = 340


    appDisplay.fill(white)

    message = ""
    if 0 <= cam_angle < 90:
        message = "Suction Stroke"
    elif 90 <= cam_angle < 180:
        message = "Compression Stroke"
    elif 180 <= cam_angle < 270:
        message = "Power Stroke"
    elif 270 <= cam_angle < 360:
        message = "Exhaust Stroke"
    label = Font.render(message, 1, (0, 0, 0))
    appDisplay.blit(label, (15, 20))

    if inlet_valve_rise_angle < cam_angle < inlet_valve_return_angle:
        pygame.draw.rect(appDisplay, fuel_color, (engine_body_x + 190, 17, 77, 19))
        pygame.draw.rect(appDisplay, fuel_color, (engine_body_x + 249, 17, 18, 85))
        pygame.draw.rect(appDisplay, fuel_color, (engine_body_x + 235, 102, 140, piston_y - 95))

    elif exhaust_valve_rise_angle < cam_angle < exhaust_valve_return_angle:
        pygame.draw.rect(appDisplay, exhaust_flue_color, (engine_body_x + 335, 17, 77, 19))
        pygame.draw.rect(appDisplay, exhaust_flue_color, (engine_body_x + 335, 17, 18, 85))
        pygame.draw.rect(appDisplay, exhaust_flue_color, (engine_body_x + 235, 102, 140, piston_y - 95))


    elif 180 < cam_angle:
        if cam_angle < exhaust_valve_rise_angle:
            pygame.draw.rect(appDisplay, yellow, (engine_body_x + 235, 102, 140, piston_y - 95))
            appDisplay.blit(combustion_img, (engine_body_x + 240, 102))
        if cam_angle < 185:
            appDisplay.blit(combustion_img, (engine_body_x + 240, 102))

    elif inlet_valve_return_angle <= cam_angle < 180:
        compression_color = (159 + (80 - piston_y/3), 168 + (80 - piston_y/3), piston_y - 95)
        pygame.draw.rect(appDisplay, compression_color, (engine_body_x + 235, 102, 140, piston_y - 95))

    for component in component_list:
        if component.id == "engine_body":
            component.linear_draw(appDisplay)

        elif component.id == "piston":
            piston_behavior(toRadians(crank_angle - 180), component, crank_radius)
            component.linear_draw(appDisplay)
            piston_y = component.y

        elif component.id == "connecting_rod":
            connecting_rod_behavior(toRadians(crank_angle - 180), component, crank_radius)
            component.linear_rotate_draw(appDisplay)

        elif component.id == "crankshaft":
            crankshaft_behavior(crank_angle, component)
            component.rotate_draw(appDisplay)

        elif component.id == "crankgear":
            crankshaft_behavior(crank_angle, component)
            component.rotate_draw(appDisplay)

        elif component.id == "camgear":
            camgear_behavior(cam_angle, component)
            component.rotate_draw(appDisplay)

        elif component.id == "inlet_cam":
            camgear_behavior(cam_angle, component, inlet_valve_rise_angle - 45)
            component.rotate_draw(appDisplay)

        elif component.id == "exhaust_cam":
            camgear_behavior(cam_angle, component, exhaust_valve_rise_angle - 45)
            component.rotate_draw(appDisplay)

        elif component.id == "inlet_pushrod":
            pushrod_behavior(cam_angle, component, inlet_valve_rise_angle, inlet_valve_return_angle)
            component.linear_draw(appDisplay)

        elif component.id == "exhaust_pushrod":
            pushrod_behavior(cam_angle, component, exhaust_valve_rise_angle, exhaust_valve_return_angle)
            component.linear_draw(appDisplay)

        elif component.id == "inlet_rocker":
            rocker_behavior(cam_angle, component, inlet_valve_rise_angle, inlet_valve_return_angle, 1)
            component.rotate_draw(appDisplay)

        elif component.id == "exhaust_rocker":
            rocker_behavior(cam_angle, component, exhaust_valve_rise_angle, exhaust_valve_return_angle, -1)
            component.rotate_draw(appDisplay)

        elif component.id == "inlet_valve":
            valve_behavior(cam_angle, component, inlet_valve_rise_angle, inlet_valve_return_angle)
            component.linear_draw(appDisplay)

        elif component.id == "exhaust_valve":
            valve_behavior(cam_angle, component, exhaust_valve_rise_angle, exhaust_valve_return_angle)
            component.linear_draw(appDisplay)



    pygame.display.update()
    clock.tick(60)
