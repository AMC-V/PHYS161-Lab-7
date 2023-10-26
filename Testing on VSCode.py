import vpython as vp

# region Constants 
POI = vp.vec(0, 3, 0)  # Our point of interest, Specific place we care about
x_min = -10          # Left side of the wire
x_max = 10           # Right side of the wire
N = 16               # Number of loops
current = 1e4        # positive implies current to the right, negative to the left
mu_0 = 4*vp.pi*1e-7  # Constant in back of book of mu
scale_factor = 1e4
wire = []            # wire is made up of multiple clinders
# endregion

# region Intitial Calculation
length = x_max - x_min     # The absolute lenght of wire
dx = length/N              # loops per lenght 
constant = mu_0*current/4/vp.pi   # This is from the eq B = mu*I/Area integral of ds cross r vec / r mag
# endregion 

# region B field arrow Creation

B_tot = vp.vec(0,0,0)
B_tot_arrow = vp.arrow(pos = POI, axis = B_tot*scale_factor, color = vp.vec(0.4, 0.4, 1)) # Arrow will be updated in loop

B_label = vp.label(pos=POI, text="mT", color = B_tot_arrow.color, xoffset=20, yoffset=-20, border=0, box=False, line=False)

# endregion

current_label = vp.label(pos=vp.vec(0.85*x_min, 0.15*x_max, 0), color = vp.vec(1, 0.1, 0.1), text="I", border=0, box=False, 
                         line=False)

print("h")

for x in vp.arange(x_min, x_max, dx):
    vp.rate(2)
    
    #for these particular cylinders, cylinder.pos is the LEFT end
    segment = vp.cylinder( pos=vp.vec(x,0,0), axis=vp.vec(0.925*dx, 0,0), opacity=0.35) # Create a peice of the wire
    
    #to use the CENTER of the cylinder as the source
    #add in dx/2 to the appropriate coordinate
    #alternatively, you could increase N dramatically to make this error tiny
    #but that dramatically slows computations later...
    current_arrow = vp.arrow(pos = vp.vec(x+dx/2,0,0), # create a arrow for current
                           axis = vp.vec(dx,0,0),
                           color = vp.vec(1,0,0), opacity = 0.8,shaftwidth = 0.5, headwidth = 1, headlength = 0.5)    
    
    r = POI - current_arrow.pos # Vector from current to point of interest
    ds = current_arrow.axis # 
    
    B_tot += constant*vp.cross(ds, r)/vp.mag(r)**3
    B_tot_arrow.axis = B_tot*scale_factor
    B_label.text = f"<i>B<sub>tot</sub></i> =  {1e3*B_tot.mag:.2f} mT"
    
    wire.append(segment)

#print("B_tot VECTOR at "+POI+" is "+B_tot)
#B_th = abs( mu_0*current/2/vp.pi/POI.y )
#print("B_th MAGNITUDE at "+POI+" is "+B_th)
#p_diff = ( vp.mag(B_tot) - B_th )/B_th*100
#print(f"% difference is {p_diff:.1f}%")