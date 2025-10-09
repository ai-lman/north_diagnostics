import numpy as np

class Diagnostic:
    def __init__(self, path: str, shot: int):
        self.path = path
        self.shot = shot
        self.type = self.__class__.__name__
        
    def get_status(self):
        """ Return the status of the diagnostic. """
        return f"Diagnostic {self.type} is {'active' if self.active else 'inactive'}."
    
    def get_time_indices(self, start_time: float, end_time: float):        
        # Find the closest indices
        start_idx = (np.abs(self.time - start_time)).argmin()
        end_idx = (np.abs(self.time - end_time)).argmin()

        return start_idx, end_idx
