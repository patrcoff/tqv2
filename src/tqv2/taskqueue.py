class TaskQueue:
    """Used for instantiating a TaskQueue object which can receive custom functions to be added to available steps."""
    
    def __init__(self, modifier = None):
        self.funcs = {}
        if modifier:
            self.load(modifier)
    
    def run(self,**kwargs):
        if not kwargs['input']:
            return True

    def load(self):
        pass



def _placeholder():
    print('PLACEHOLDER')

