# Web VPython 3.2

#Animation Window 
scene.width = 900
scene.height = 500
scene.background = color.gray(0.15)
scene.camera.pos    = vec(0, 6, 18)
scene.camera.axis   = vec(0, -3, -18)

#Setting the Scene 
ground = box(pos=vec(0, -0.3, 0), size=vec(60, 0.3, 8),
             color=color.gray(0.35), texture=textures.rough)
road_lines = []
for xpos in range(-28, 30, 4):
    road_lines.append(box(pos=vec(xpos, -0.14, 0), size=vec(2, 0.02, 0.3), color=color.white, opacity=0.5))
    
car_selection = {
    "Small  (800 kg)":  800,
    "Medium (1400 kg)": 1400,
    "Large  (2500 kg)": 2500,
}

target_selection = {
    "Stationary Tree":    {"mass": 5000, "moving": False, "color": color.green},
    "Parked Car (1400 kg)": {"mass": 1400, "moving": False, "color": color.cyan},
    "Deer (120 kg)":      {"mass": 120,  "moving": True,  "color": color.orange},
    "Truck (6000 kg)":    {"mass": 6000, "moving": False, "color": color.red},
}

##Defining the object 
#car = box(pos=vec(-3,-3,0),axis=vec(1,0,0), size=vec(1,1,3), color=color.red, texture=textures.metal)
#attach_light(car, offset=vec(3, 0, 1), color=color.green)
#
#target = box(pos=vec(3, 3, -5), size = vec(3, 3, 3), color = color.green, texture=textures.wood)
#
##Defining initial velocity/acceleration/position 
#velocity = vec(2, 1, -0.05)
#dt = 0.01 
#
##Simple animation 
#while True: 
#    rate(60) 
#    print(car.pos)
#    car.pos = car.pos + velocity * dt 
#    
#    
#while car.pos == target.pos: 
#    rate(0)
#    print("target was hit!")
    