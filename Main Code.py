# Notes remove vp. from all labels for coord. sys AND the parathesis on the pi() AND vp. from arrow 

# region Imports
import vpython as vp
# endregion

# region compatablaility methods from VCcode to Growscript, Don't add these to Glowscript
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = False)

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

def hat(number):
    return vp.hat(number)
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

pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vec(axis.toffset, 0, 0), 
         text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_x_axis = arrow(pos = origin, axis = vec(-axis.l, 0, 0))
neg_x_axis.shaftwidth = axis.s
neg_x_axis.color = vec(1, 0, 0)

neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vec(-axis.toffset, 0, 0), 
         text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
pos_y_axis = arrow(pos = origin, axis = vec(0, axis.l, 0))
pos_y_axis.shaftwidth = axis.s 
pos_y_axis.color = vec(0, 1, 0)

pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vec(0, axis.toffset, 0), 
         text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_y_axis = arrow(pos = origin, axis = vec(0, -axis.l, 0))
neg_y_axis.shaftwidth = axis.s
neg_y_axis.color = vec(0, 1, 0)

neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vec(0, -axis.toffset, 0), 
         text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

pos_z_axis = arrow(pos = origin, axis = vec(0,0,axis.l))
pos_z_axis.shaftwidth = axis.s
pos_z_axis.color = vec(0, 0, 1)

pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
neg_z_axis.shaftwidth = axis.s
neg_z_axis.color = vp.vec(0, 0, 1)

neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion

# region Particle Creation
Particle = sphere(pos = origin + vec(-0.2, 0.2, 4), radius = 0.1)
Particle.color = vec(0, 0.5, 1)
Particle.q = 1.602e-19 # C, charge of a proton
Particle.m = 9.11e-31 # Kg, mass of a proton
Particle.a = vec(0, 0, 0)
Particle.v = vec(1, -1, 10)
# endregion

# region Coil Creation

# region Constants for Coil
R = 0.5  # Radius of the Coil
N = 20 # This tells us how many pieces will be in the Coil
POI = Particle.pos       # Our point of interest, Specific place we care about
B_Total = vec(0, 0, 0)   # Will hold the total magnetic field
F_Total = vec(0, 0, 0)   # WIll hold the current force 
theta_min = radians(0)   # Our starting angle for the Coil in Radians
theta_max = radians(360) # Our ending angle for the Coil in Radians
current = 1e5            # positive implies current CCW, negative CW og 1e4
mu_0 = 4*pi()*1e-7       # Constant in back of book of mu
scale_factor = 10**(2.5) # Widening, unknown ATM
scale_factor2 = 0.1
stauration_factor = 1.5
# endregion

# region Initial Calculations for Coil
angle_tot = theta_max - theta_min # The total angle the Coil will have
dtheta = angle_tot / (N - 1)      # A small bit of angle
ds = R * dtheta                   # A small bit of arc lenght
constant = mu_0 * current/4/pi()  # This is from the eq B = mu*I/Area integral of ds cross r vec / r mag
# endregion

# region Total Magnetic Field Arrow at one point and Force Arrow
Force_arrow = arrow(pos = Particle.pos, axis = F_Total)
Force_arrow.color = vec(0, 1, 0) # Green
Force_arrow.opacity = 0.5

velocity_arrow = arrow(pos = Particle.pos, axis = F_Total)
velocity_arrow.color = vec(0, 0, 0) # Green
velocity_arrow.opacity = 0.5


B_Total_arrow = arrow(pos = Particle.pos, axis = B_Total * scale_factor)
B_Total_arrow.color = vec(0.627, 0.125, 0.941) # Purple 
B_Total_arrow.opacity = 0.5
# endregion

# region Methods
# Method to generate the position of all the current arrows in a Coil
def create_positions_list(starting_angle, ending_angle, d_theta, z_position, Radius):
    position_list = [] # List to hold positions generated for each arrow
    
    # Loop we gives us a rectangluar unit vector based on current angle
    for current_theta in arange (starting_angle, ending_angle, d_theta): 
        
        # Get current angle and breaks it, into x & y components as a unit vector
        current_position_hat = vec(cos(current_theta), sin(current_theta), 0) 
        
        # Current position depending on the radius and z position
        current_position = Radius * current_position_hat + vec(0, 0, z_position)
        
        # Add the positions to our list
        position_list.append(current_position) 
        
    return position_list # Return a position list

# Method to create a Coil, it can be moved in z direction, x & y are locked
def create_coil(position_list, Radius):
    current_in_coil = [] # Made up from the currents in Coil
    Coil_visual = ring(pos = vec(0, 0, position_list[0].z), axis = vec(0, 0, 1), radius = Radius * 0.95)
    Coil_visual.thickness = 0.2
    Coil_visual.opacity = 0.4
    Coil_visual.texture = vp.textures.metal
    
    # This loop creates current arrows
    for number_in_list in arange(0, len(position_list), 1): # Note: you never actually reach the value = len(positions_list)  
        current_arrow = vp.arrow()         # Creates standard arrow
        current_arrow.color = vec(1, 0, 0) # Color arrow red to represent current
        
        if number_in_list == len(position_list) - 1: 
            current_arrow.pos = position_list[number_in_list]
            current_arrow.axis = position_list[0] - position_list[number_in_list]
        else:
            current_arrow.pos = position_list[number_in_list]
            current_arrow.axis = position_list[number_in_list + 1] - position_list[number_in_list]
            
        current_in_coil.append(current_arrow)
    
    return current_in_coil

# Method to calculate the magnetic field total from a Coil at a specific point
def current_magnetic_field_from_coil(current_in_coil_list, my_POI):
    B_Total_Temp = vec(0, 0, 0) # Will hold the magnetic field contribution from all the currents in Coil
    
    # Loop will go through all the positions (representing current) in the coil    
    for current_arrow in current_in_coil_list:
        r = my_POI - current_arrow.pos # Get vector from a current in the Coil to point of interest
        ds = current_arrow.axis - current_arrow.pos # vector a small amount of distance pointed in dir of current
        
        B_Total_Temp += constant * cross(ds,r) / mag(r)**3 # db added to the total b field in POI
        B_Total_arrow.axis = B_Total_Temp * scale_factor
        
    return B_Total_Temp
# endregion

# region BUILDING Position list + Coils + current arrows
# List to hold positions generated for each arrow
positions_list_1 = create_positions_list(theta_min + dtheta/2, theta_max, dtheta, 0, R) 
currents_in_Coil_List_1 = create_coil(positions_list_1, R)

positions_list_2 = create_positions_list(theta_min + dtheta/2, theta_max, dtheta, 15, R)
currents_in_Coil_List_2 = create_coil(positions_list_2, R)
# endregion

# endregion

# region Animation of Electron
t = 0
dt = 1e-9
sim_speed = 0.000000005

while t < 10000 * dt:
    rate(sim_speed/dt)
    
    # First time the electron position will be vec(0, 0, 0)
    current_B_field_1 = current_magnetic_field_from_coil(currents_in_Coil_List_1, Particle.pos) # Magnetic field from Coil 1
    current_B_field_2 = current_magnetic_field_from_coil(currents_in_Coil_List_2, Particle.pos) # Magnetic field from Coil 2
    
    # Adding both fields
    current_B_field_Total = current_B_field_1 + current_B_field_2
    
    current_force = Particle.q * cross(Particle.v, current_B_field_Total)

    Particle.a = current_force / Particle.m
    Particle.v += Particle.a * dt
    Particle.pos += Particle.v * dt
    
    print(f"The current velocity is {Particle.v} at time {t}")
    
    velocity_arrow.axis = Particle.v
    
    if Particle.v == vec(0, 0, 0):
        Force_arrow.opacity = 0
    
    Force_arrow.axis = stauration_factor * hat(current_force)  
    
    B_Total_arrow.axis = current_B_field_Total * scale_factor
    B_Total_arrow.pos = Force_arrow.pos = velocity_arrow.pos = Particle.pos
    
    t += dt

# endregion