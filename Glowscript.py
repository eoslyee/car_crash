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
    road_lines.append(box(pos=vec(xpos, -0.14, 0), size=vec(2, 0.02, 0.3), 
    color=color.white, opacity=0.5))

surface_settings = {
    "asphalt": color.gray(0.35),
    "wet road": vec(0.3, 0.35, 0.45), 
    "ice": vec(0.75, 0.88, 1.0),
}

car_selection = {
    "small  (800 kg)":  {"mass": 800,  "scale": 0.85, "color": color.red},
    "medium (1400 kg)": {"mass": 1400, "scale": 1.0,  "color": color.blue},
    "large  (2500 kg)": {"mass": 2500, "scale": 1.2,  "color": color.green},
}

target_selection = {
    "Stationary Tree":    {"mass": 5000, "moving": False, "color": color.green},
    "Parked Car (1400 kg)": {"mass": 1400, "moving": False, "color": color.cyan},
    "Deer (120 kg)":      {"mass": 120,  "moving": True,  "color": color.orange},
    "Truck (6000 kg)":    {"mass": 6000, "moving": False, "color": color.red},
}

state = {
    "surface":     "Asphalt",
    "car_type":    "Medium (1400 kg)",
    "target_type": "Stationary Tree",
    "car_speed":   15.0,      # m/s (will use later) 
    "elasticity": 0.5,       # 0 = perfectly inelastic, 1 = elastic
    "running":     False,
    "reset_flag":  False,
    "t":           0.0,
    "dt":          0.005,
    "collided":    False,
}

# Defining Objects 
current_car = []
current_target = []

def clear(obj_list):
    for obj in obj_list: 
        obj.visible = False
    obj_list.clear()
    
def build_car(car_type, start_x = -12): 
    """Builds a simple car shape """
    clear_objects(current_car)
    info = car_selection[car_type]
    scale = info["scale"]
    col - info["color"] 
    
    body = box(pos=vec(start_x, 0.45*scale, 0),
              size = vec(3.5*scale, 0.8*scale, 1.8*scale), 
              color = col)
    
    cabin = box(pos=vec(start_x - 0.2*scale, 0.45*scale + 0.65*scale, 0),
                size=vec(1.8*scale, 0.65*scale, 1.6*scale),
                color=col * 0.75)
    # wheels           
    r = 0.32*scale 
    wheel_pos = [
        vec(start_x + 1.1*scale,  r,  0.95*scale),
        vec(start_x + 1.1*scale,  r, -0.95*scale),
        vec(start_x - 1.1*scale,  r,  0.95*scale),
        vec(start_x - 1.1*scae,  r, -0.95*scale),
    ]
    
    for wp in wheel_pos: 
        w = cylinder(pos=wp, axis=vec(0, 0, 0.2), radius=r, color=color.gray(0.2))
        current_car.append(w)
 
    current_car.append(body)
    current_car.append(cabin)

# User Controls 
scene.append_to_caption("\n")
 
# Setting Surface 

scene.append_to_caption("<b>Surface:</b>  ")
def set_ground(b): 
    state["surface"] = b.text
    ground.color = surface_colors[b.text]
    ground.color = surface_colors["Asphalt"] 

button(text="Asphalt",  bind=set_ground)
button(text="Wet Road", bind=set_ground)
button(text="Ice",      bind=set_ground)
scene.append_to_caption("\n\n")

# Setting Car Size

scene.append_to_caption("<b>Car Type:</b> ") 
def set_size(b): 
    state["car_type"] = b.text
    build_car(state["car_type"])

button(text="Small (800 kg)",  bind=set_ground)
button(text="Medium (1400 kg)", bind=set_ground)
button(text="Large (2500 kg)",      bind=set_ground)
scene.append_to_caption("\n\n")
    
 

# Graph 

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
    