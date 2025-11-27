class AlgorithmBase:  
    def __init__(self, config):
        self.config = config

    def client_update(self, w_t, cid):
        raise NotImplementedError("Subclasses should implement this method")

    def aggregate(self, w_t, updates):
        raise NotImplementedError("Subclasses should implement this method")
      
    def execute(self, data):
        raise NotImplementedError("Subclasses should implement this method")