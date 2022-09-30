
def execute(self, inputs, outputs, gvm):
    x_scale = inputs["x_scale"]
    y_scale = inputs["y_scale"]
    x_pos = inputs["x_pos"]
    y_pos = inputs["y_pos"]
    outputs["x_pos_1"] = x_pos + x_scale / 2.0
    outputs["y_pos_1"] = y_pos + y_scale / 2.0
    outputs["x_pos_2"] = x_pos - x_scale / 2.0
    outputs["y_pos_2"] = y_pos + y_scale / 2.0
    outputs["x_pos_3"] = x_pos - x_scale / 2.0
    outputs["y_pos_3"] = y_pos - y_scale / 2.0
    outputs["x_pos_4"] = x_pos + x_scale / 2.0
    outputs["y_pos_4"] = y_pos - y_scale / 2.0
    return 0
