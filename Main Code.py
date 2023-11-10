# Notes remove vp. from all labels AND the parathesis on the pi() AND vp. from arrow 

# region Imports
import vpython as vp
import sys
# endregion

# region compatablaility methods from VCcode to Growscript, Don't add these to Glowscript
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = True)

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = kid["radius"], make_trail = True)

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

# region Method for Particle Creation
def create_particle(start_location, size, velocity):   
    Particle_ = sphere(pos = origin + start_location, radius = size) # 0,.11,7.1
    Particle_.trail_radius = 0.01
    Particle_.color = vec(0, 0.5, 1)
    Particle_.q = 1.602e-19 # C, charge of a proton
    Particle_.m = 1.673e-27 # Kg, mass of a proton
    Particle_.a = vec(0, 0, 0)
    Particle_.v = velocity # 0, -10.5, 14
    
    return Particle_
    
Particle_1 = create_particle(vec(0, 0.57, 0), 0.1, vec(12.3, 10, 25))
Particle_2 = create_particle(vec(0.5, 0, -1), 0.1, vec(12.3, 7, -10))
# endregion

# region Coil Creation

# region Constants for Coil
R = 5  # Radius of the Coil
N = 50 # This tells us how many pieces will be in the Coil, 12
POI = Particle_1.pos       # Our point of interest, Specific place we care about
mu_0 = 4*pi()*1e-7       # Constant in back of book of mu
current = 10             # positive implies current CCW, negative CW
B_Total = vec(0, 0, 0)   # Will hold the total magnetic field
F_Total = vec(0, 0, 0)   # WIll hold the current force 
theta_min = radians(0)   # Our starting angle for the Coil in Radians
theta_max = radians(360) # Our ending angle for the Coil in Radians
scale_factor = 5e5       # To scale B field arrow
scale_factor2 = 1.5      # To scale Force and velocity arrows
# endregion

# region Initial Calculations for Coil
angle_tot = theta_max - theta_min # The total angle the Coil will have
dtheta = angle_tot / (N - 1)      # A small bit of angle
ds = R * dtheta                   # A small bit of arc lenght
constant = mu_0 * current/4/pi()  # This is from the eq B = mu*I/Area integral of ds cross r vec / r mag
theta_low = theta_min + dtheta/2  # This determines where the coil will start
# endregion

# region Total Magnetic Field and Force Arrow Method
def create_arrows(Particle_):
    arrows_list = []
    
    Force_on_Particle_arrow_ = arrow(pos = Particle_.pos, axis = origin)
    Force_on_Particle_arrow_.color = vec(0, 1, 0) # Green
    Force_on_Particle_arrow_.opacity = 0.5
    
    arrows_list.append(Force_on_Particle_arrow_)

    Force_on_Particle_arrow_label_ = vp.label(pos = Force_on_Particle_arrow_.axis, text = '<i>F</i>', 
        height = 16, border = 4, font = 'monospace', line = False, opacity = 0, 
        box = False)
    
    arrows_list.append(Force_on_Particle_arrow_label_)

    velocity_arrow_ = arrow(pos = Particle_.pos, axis = Particle_1.v)
    velocity_arrow_.color = vec(1, 1, 1) # White
    velocity_arrow_.opacity = 0.3
    
    arrows_list.append(velocity_arrow_)

    velocity_arrow_label_ = vp.label(pos = velocity_arrow_.axis, text = '<i>V</i>', 
        height = 16, border = 4, font = 'monospace', line = False, opacity = 0, 
        box = False)
    
    arrows_list.append(velocity_arrow_label_)

    B_Total_arrow_ = arrow(pos = Particle_.pos, axis = origin * scale_factor)
    B_Total_arrow_.color = vec(0.627, 0.125, 0.941) # Purple 
    B_Total_arrow_.opacity = 0.5
    
    arrows_list.append(B_Total_arrow_)

    B_Total_arrow_label_ = vp.label(pos = B_Total_arrow_.axis, text = '<i>B</i>', 
        height = 16, border = 4, font = 'monospace', line = False, opacity = 0, 
        box = False)
    
    arrows_list.append(B_Total_arrow_label_)
    
    return arrows_list
# endregion

# region Methods for Coil, Boundary, and Magentic field
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

# Method to create a Coil along with current arrows, x & y position are locked
def create_coil(position_list, Radius, Coil_name):
    current_in_coil = [] # Made up from the currents in Coil
    Coil_visual = ring(pos = vec(0, 0, position_list[0].z), axis = vec(0, 0, 1), radius = Radius)
    Coil_visual.thickness = 0.2
    Coil_visual.opacity = 0.4
    Coil_visual.texture = vp.textures.metal
    
    # Object labels
    vp.label(pos = vec(0, Radius, position_list[0].z), text = Coil_name, xoffset = 10, yoffset = 20, space = 10, height = 16, 
             border = 4, font = 'monospace', box = False, opacity = 0)
    
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

# Method to calculate the magnetic field from a Coil at a specific position
def current_magnetic_field_from_coil(current_in_coil_list, my_POI):
    
    # Holds the Magnetic field contributions from all the currents in Coil
    B_Total_Temp = vec(0, 0, 0) 
    
    # Loop will go through all the positions (representing current) in the coil    
    for my_current_arrow in current_in_coil_list:
        
        # Gets vector from a current in the Coil to point of interest
        r = my_POI - my_current_arrow.pos 
        
        # Gets a vector that represents a small amount of distance pointed in the direction of a current
        ds = my_current_arrow.axis - my_current_arrow.pos 
        
        # Stores a small amount of B field generated from a current in the Coil
        B_Total_Temp += constant * cross(ds,r) / mag(r)**3 
        
    return B_Total_Temp # Returns the total B field from a Coil at the current POI

# Method to create bounds visual on particle
def create_bounds(start_position, end_position, Radius):
    bound = cylinder(pos = vec(0, 0, start_position[0].z), axis = vec(0, 0, 2*end_position[0].z), color = vec(1, 1, 1))
    bound.radius = Radius
    bound.opacity = 0.1
    
def bounds_check(current_position, position_list_1, position_list_2):
    if mag(vec(current_position.x, current_position.y, 0))  >= mag(vec(position_list_1[0].x, position_list_1[0].y, 0)):
        print("r escape")
        sys.exit(0)
        
    elif current_position.z < position_list_1[0].z or current_position.z > position_list_2[0].z:
        print("z escape")
        sys.exit(0)
# endregion

# region BUILDING Position list + Coils + current arrows
positions_list_1 = create_positions_list(theta_low, theta_max, dtheta, -10, R) # Make a list to hold positions generated for each arrow
currents_in_Coil_List_1 = create_coil(positions_list_1, R, 'Coil_1') # Make Coil and a list that will hold all the currents inside the Coil

positions_list_2 = create_positions_list(theta_low, theta_max, dtheta, 10, R)
currents_in_Coil_List_2 = create_coil(positions_list_2, R, 'Coil 2')


arrow_list_1 = create_arrows(Particle_1)
arrow_list_2 = create_arrows(Particle_2)
create_bounds(positions_list_1, positions_list_2, R)
# endregion

# endregion

# region Animation

def single_timestep_calculation(Particle_, arrow_list_, dt_):
    # First time the particle's position will be vec(0, 0, 0)
    # Magnetic field from Coil 1
    current_B_field_1 = current_magnetic_field_from_coil(currents_in_Coil_List_1, Particle_.pos)
    
    # Magnetic field from Coil 2
    current_B_field_2 = current_magnetic_field_from_coil(currents_in_Coil_List_2, Particle_.pos) 
    
    # Adding both fields
    current_B_field_Total = current_B_field_1 + current_B_field_2
    
    current_force = Particle_.q * cross(Particle_.v, current_B_field_Total)

    # CAHNGE COLOR OF FORCE ARROWS AND VELO

    Particle_.a = current_force / Particle_.m
    Particle_.v += Particle_.a * dt_
    Particle_.pos += Particle_.v * dt_
    
    bounds_check(Particle_.pos, positions_list_1, positions_list_2)

    arrow_list_[0].pos = arrow_list_[2].pos = arrow_list_[4].pos = Particle_.pos

    arrow_list_[2].axis =  current_B_field_Total * scale_factor * 5
    arrow_list_[3].pos = arrow_list_[2].axis + arrow_list_[2].pos
   
    arrow_list_[4].axis = scale_factor2 * 1 * hat(Particle_1.v)
    arrow_list_[5].pos = arrow_list_[4].axis + arrow_list_[4].pos
    
    arrow_list_[0].axis =  scale_factor2 * hat(current_force) 
    arrow_list_[1].pos = arrow_list_[0].axis + arrow_list_[0].pos

t = 0 # Total runtime
dt = 1e-4 # Time step
sim_speed = 1e5

while True:
    rate(sim_speed/dt)
    
    single_timestep_calculation(Particle_1, arrow_list_1, dt)
    single_timestep_calculation(Particle_2, arrow_list_2, dt)
   
    t += dt

# endregion

