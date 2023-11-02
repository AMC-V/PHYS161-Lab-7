import vpython as vp


# region Coordiante System 
origin = vp.vec(0, 0, 0)
axis = vp.sphere(pos = origin, radius = 5)  # Here radius is length of axis
axis.l = axis.radius  # Lenght of axis arrows
axis.s = 0.05         # Radius of axis arrows
axis.f = 'monospace'
axis.toffset = 0.05
axis.visible = False

pos_x_axis = vp.arrow(pos = origin, axis = vp.vec(axis.l,0,0), shaftwidth = axis.s, round=True,
         color = vp.vec(1, 0, 0))
pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vp.vec(axis.toffset, 0, 0), 
         text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_x_axis = vp.arrow(pos = origin, axis = vp.vector(-axis.l,0,0), shaftwidth = axis.s, round=True,
         color = vp.vec(1, 0, 0))
neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vp.vec(-axis.toffset, 0, 0), 
         text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
pos_y_axis = vp.arrow(pos = origin, axis = vp.vector(0,axis.l,0), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 1, 0))
pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vp.vec(0, axis.toffset, 0), 
         text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_y_axis = vp.arrow(pos = origin, axis = vp.vector(0,-axis.l,0), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 1, 0))
neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vp.vec(0, -axis.toffset, 0), 
         text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

pos_z_axis = vp.arrow(pos = origin, axis = vp.vector(0,0,axis.l), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 0, 1))
pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vp.vec(0, axis.toffset, 0), 
         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = vp.arrow(pos = origin, axis = vp.vector(0,0,-axis.l), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 0, 1))
neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vp.vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion