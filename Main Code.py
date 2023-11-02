import vpython as vp

# Notes remove vp. from all labels for code to work

# region compatablaility methods from VCcode to Growscript, Don't add these to Glowscript
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"])

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = kid["radius"])

def radians(number):
    return vp.radians(number)

def sin(number):
    return vp.sin(number)

def cos(number):
    return vp.cos(number)

def arange(min, max, change):
    return vp.arange(min, max, change)

def cylinder(**kid):
    return vp.cylinder(pos = kid["pos"], axis = kid["axis"], color = kid["color"])

# endregion

# region Coordiante System 
origin = vec(0, 0, 0)
axis = sphere(pos = origin, radius = 5)  # Here radius is length of axis
axis.l = axis.radius  # Lenght of axis arrows
axis.s = 0.05         # Radius of axis arrows
axis.f = 'monospace'
axis.toffset = 0.05
axis.visible = False

pos_x_axis = arrow(pos = origin, axis = vec(axis.l, 0, 0))
pos_x_axis.shaftwidth = axis.s
pos_x_axis.color = vec(1, 0, 0)
pos_x_axis._round = True

pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vec(axis.toffset, 0, 0), 
         text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_x_axis = arrow(pos = origin, axis = vec(-axis.l, 0, 0))
neg_x_axis.shaftwidth = axis.s
neg_x_axis.color = vec(1, 0, 0)
neg_x_axis._round = True

neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vec(-axis.toffset, 0, 0), 
         text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
pos_y_axis = arrow(pos = origin, axis = vec(0, axis.l, 0))
pos_y_axis.shaftwidth = axis.s 
pos_y_axis.color = vec(0, 1, 0)
pos_y_axis._round=True

pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vec(0, axis.toffset, 0), 
         text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_y_axis = arrow(pos = origin, axis = vec(0, -axis.l, 0))
neg_y_axis.shaftwidth = axis.s
neg_y_axis.color = vec(0, 1, 0)
neg_y_axis._round = True

neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vec(0, -axis.toffset, 0), 
         text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

pos_z_axis = arrow(pos = origin, axis = vec(0,0,axis.l))
pos_z_axis.shaftwidth = axis.s
pos_z_axis.color = vec(0, 0, 1)
pos_z_axis._round=True 


pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
neg_z_axis.shaftwidth = axis.s
neg_z_axis.color = vp.vec(0, 0, 1)
neg_z_axis._round = True 

neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion

# region Election Creation

electron = sphere(pos = origin, radius = 0.1)
electron.color = vec(0, 0, 1)

# endregion

# region Rings Creation
# Constants for Rings
R =  2 # Radius of the Ring
N = 10 # This tells us how many pieces will be in the Ring

theta_min = radians(0)   # Our starting angle for the Ring in Radians
theta_max = radians(360) # Our ending angle for the Ring in Radians

coil_2 = [] # Made up of cylinders

Stage3_L = vp.label(pos = vec(-0, 5, 0), text = 'Stage 3')

# Initial Calculations for Rings
angle_tot = theta_max - theta_min # The total angle the Ring will have
dtheta = angle_tot / (N - 1)      # A small bit of angle
ds = R * dtheta                   # A small bit of arc lenght

# Make list of positions for each arrow
positions_list = []
for current_theta in arange (theta_min + dtheta/2, theta_max, dtheta):
    # Gives us a rectangluar unit vector based on current angle
    current_position_hat = vec(cos(current_theta), sin(current_theta), 0)
    current_position = R * current_position_hat 
    positions_list.append(current_position) # Add the positions to our list
    
# BUILDING RING 1
coil_1 = [] # Made up of cylinders
for number_in_list  in arange(0, len(positions_list), 1): # Note: you never actually reach the value = len(positions_list)
    if number_in_list == len(positions_list) - 1: 
        current_arrow = arrow(pos = positions_list[number_in_list], axis = positions_list[0] - positions_list[number_in_list])
        coil_1.append(current_arrow)
    else:
        current_arrow = arrow(pos = positions_list[number_in_list], axis = positions_list[number_in_list + 1] - positions_list[number_in_list])
        coil_1.append(current_arrow)
        
        
     
# endregion