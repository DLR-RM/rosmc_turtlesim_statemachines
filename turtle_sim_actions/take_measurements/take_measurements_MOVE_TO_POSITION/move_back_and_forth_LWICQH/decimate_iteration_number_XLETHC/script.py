
def execute(self, inputs, outputs, gvm):
    outputs['iteration'] = inputs['iteration'] - 1
    return 0
