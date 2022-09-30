def execute(self, inputs, outputs, gvm):
    import numpy as np
    
    turtle_name = inputs["turtle_name"]
    x_pos = inputs['x_pos']
    y_pos = inputs['y_pos']
    amplitude = inputs['amplitude']

    my_x = gvm.get_variable(turtle_name + "/" + "x")
    my_y = gvm.get_variable(turtle_name + "/" + "y")
    my_phi = gvm.get_variable(turtle_name + "/" + "phi")
    
    outputs['x_pos_forth'] = x_pos + np.cos(my_phi) * amplitude
    outputs['x_pos_back'] = x_pos - np.cos(my_phi) * amplitude
    outputs['y_pos_forth'] = y_pos + np.sin(my_phi) * amplitude
    outputs['y_pos_back'] = y_pos - np.sin(my_phi) * amplitude
    
    return 0
