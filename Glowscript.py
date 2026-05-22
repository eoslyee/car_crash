# Web VPython 3.2

#Defining the object 
car = box(pos=vec(-3,-3,0),axis=vec(1,0,0), size=vec(1,1,3), color=color.red, texture=textures.metal)

target = box(pos=vec(3, 3, -5), size = vec(3, 3, 3), color = color.green, texture=textures.wood)

#Defining initial velocity/acceleration/position 
velocity = vec(2, 1, -0.05)
dt = 0.01 

#Simple animation 
while True: 
    rate(60) 
    print(car.pos)
    car.pos = car.pos + velocity * dt 
    
    
while car.pos == target.pos: 
    rate(0)
    print("target was hit!")
    