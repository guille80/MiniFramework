from .base import AlgorithmBase

class MeanDummy(AlgorithmBase):
    def __init__(self, config):
        super().__init__(config)

    def client_update(self, w_t, cid):
        # Dummy implementation: return the weights unchanged
        return w_t + cid

    def aggregate(self, w_t, updates):
        # Simple mean aggregation
        return sum(updates) / len(updates)   

    def execute(self, data):
        # Dummy execution method
        print("Executing MeanDummy with data:", data)

class MeanDummyAlgorithm(AlgorithmBase):
    def __init__(self, config):
        super().__init__(config)

    def client_update(self, w_t, cid):
        # Dummy implementation: return the weights unchanged
        return w_t

    def aggregate(self, w_t, updates):
        # Simple mean aggregation
        num_updates = len(updates)
        if num_updates == 0:
            return w_t
        
        aggregated_weights = {}
        for key in w_t.keys():
            aggregated_weights[key] = sum(update[key] for update in updates) / num_updates
        
        return aggregated_weights

    def execute(self, data):
        # Dummy execution method
        print("Executing MeanDummyAlgorithm with data:", data)