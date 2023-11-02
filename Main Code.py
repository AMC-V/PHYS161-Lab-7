import vpython as vp

coil1 = []
coil2= []
R=  2
N =10

Stage3_L = label(pos = vec(-0, 5, 0), text = 'Stage 3')
theta_min = radians(0)
theta_max = radians(360)
angle_tot = theta_max-theta_min
dtheta = angle_tot / (N-1)
ds = R * dtheta

#BUILD RING 1
for theta in arange (theta_min + dtheta/2, theta_max, dtheta):                                          # for ring 1 
    cylinder(pos = vec(R*sin(theta),R*cos(theta),0), radius = 0.05 * ds, color = color.red)
    theta_hat = vec(sin(theta), cos(theta), 0)
    cylinder.ds = R*theta_hat
    coil1.append(ring)
        
#build ring 2
for theta in arange (theta_min + dtheta/2, theta_max, dtheta):                                          # for ring 2 
    cylinder(pos = vec(R*sin(theta), R*cos(theta), -1), radius = 0.05 * ds, color = color.red)
    theta_hat = vec(cos(theta), sin(theta), 0)
    cylinder.ds = R*theta_hat
    coil2.append(ring)
     
