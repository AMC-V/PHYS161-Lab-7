# region Imports
import vpython as vp
# endregion

# Notes remove vp. from all labels for coord. sys AND the parathesis on the pi() AND vp. from arrow 

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

def pi():
    return vp.pi

def ring(**kid):
    return vp.ring(pos = kid["pos"], axis = kid["axis"], radius = kid["radius"])

def rate(number):
    return vp.rate(number)

def cross(number_1, number_2):
    return vp.cross(number_1, number_2)

def mag(number):
    return vp.mag(number)

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
pos_z_axis.opacity = 0


# pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
#          text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
neg_z_axis.shaftwidth = axis.s
neg_z_axis.color = vp.vec(0, 0, 1)
neg_z_axis._round = True 

neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion

# region Election Creation

electron = sphere(pos = origin + vec(0, .2, 0), radius = 0.1)
electron.color = vec(0, 0.5, 1)
electron.q = 1.602e-19 # C
electron.m = 9.11e-31 # Kg
electron.a = vec(0, 0, 0)
electron.v = vec(1, 0, 0.1)

# endregion

# region Coil Creation

# region Constants for Coil
R = 2 # Radius of the Coil
N = 10 # This tells us how many pieces will be in the Coil
POI = electron.pos  # Our point of interest, Specific place we care about
B_Total = vec(0, 0, 0)
theta_min = radians(0)   # Our starting angle for the Coil in Radians
theta_max = radians(360) # Our ending angle for the Coil in Radians
current = 1e4            # positive implies current CCW, negative CW
mu_0 = 4*pi()*1e-7       # Constant in back of book of mu
scale_factor = 1e3       # Widening, unknown ATM
# endregion

# region Initial Calculations for Coil
angle_tot = theta_max - theta_min # The total angle the Coil will have
dtheta = angle_tot / (N - 1)      # A small bit of angle
ds = R * dtheta                   # A small bit of arc lenght
constant = mu_0 * current/4/pi()  # This is from the eq B = mu*I/Area integral of ds cross r vec / r mag
# endregion

# region Total Magnetic Field Arrow at one point
B_Total_arrow = arrow(pos = electron.pos, axis = B_Total * scale_factor)
B_Total_arrow.color = vec(0, 1, 0) # Green 
B_Total_arrow.opacity = 0
# endregion

# region Loop to generate the position of all the arrows
positions_list = [] # List to hold positions generated for each arrow
for current_theta in arange (theta_min + dtheta/2, theta_max, dtheta):
    # Gives us a rectangluar unit vector based on current angle
    current_position_hat = vec(cos(current_theta), sin(current_theta), 0) # Get current angle and breaks it, into x & y components
    current_position = R * current_position_hat # Current position depending on the radius
    positions_list.append(current_position) # Add the positions to our list
# endregion 

# region BUILDING Coil 1 + current arrows
current_in_coil_1 = [] # Made up from the currents in Coil
Coil_visual = ring(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = R)
Coil_visual.thickness = 0.2
Coil_visual.color = vec(1, 0, 0)

# This loop creates current arrows
for number_in_list in arange(0, len(positions_list), 1): # Note: you never actually reach the value = len(positions_list)  
    current_arrow = vp.arrow()         # Creates standard arrow
    current_arrow.color = vec(1, 0, 0) # Color arrow red to represent current
    
    if number_in_list == len(positions_list) - 1: 
        current_arrow.pos = positions_list[number_in_list]
        current_arrow.axis = positions_list[0] - positions_list[number_in_list]
    else:
        current_arrow.pos = positions_list[number_in_list]
        current_arrow.axis = positions_list[number_in_list + 1] - positions_list[number_in_list]
        
    current_in_coil_1.append(current_arrow)
# endregion

# region Methods

# Method to calculate the magnetic field total from a Coil at a specific point
def current_magnetic_field_from_coil(current_in_coil_list, my_POI):
    B_Total = vec(0, 0, 0)
    
    for current_arrow in current_in_coil_list:
        r = my_POI - current_arrow.pos # Vector from current to point of interest
        ds = current_arrow.axis # vector a small amount of distance pointed in dir of current
        
        B_Total += constant*cross(ds, r)/mag(r)**3 # db added to the total b field in POI
        B_Total_arrow.axis = B_Total * scale_factor
        
    return B_Total
        
        
# endregion

# endregion

# region Animation of Electron
t = 0
dt = 1e-9
sim_speed = 0.000000005

while t < 10000*dt:
    rate(sim_speed/dt)
    
    current_B_field = current_magnetic_field_from_coil(current_in_coil_1, electron.pos)
    
    current_force = electron.q * cross(electron.v, current_B_field)
    
    electron.a = current_force/ electron.m
    electron.v += electron.a * dt
    electron.pos += electron.v * dt
    
    t += dt

# endregion