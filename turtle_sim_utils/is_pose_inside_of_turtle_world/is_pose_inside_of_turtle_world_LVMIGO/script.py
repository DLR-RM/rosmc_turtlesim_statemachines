
def execute(self, inputs, outputs, gvm):
    max_val_x, max_val_y, min_val_x, min_val_y = 11.08, 11.08, 0, 0
    x_pos = inputs["x_pos"]
    y_pos = inputs["y_pos"]
    is_pose_inside = (min_val_x < x_pos < max_val_x) and (min_val_y < y_pos < max_val_y)
    if is_pose_inside:
        return "yes"
    else:
        return "no"
