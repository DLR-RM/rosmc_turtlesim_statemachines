
def execute(self, inputs, outputs, gvm):
    global_storage_id_of_turtle_pose = inputs["global_storage_id_of_turtle_pos"]

    my_x = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "x")
    my_y = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "y")
    my_phi = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "phi")
    
    outputs['x_pos'] = my_x
    outputs['y_pos'] = my_y
    return 0
