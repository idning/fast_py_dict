import torch
import numpy as np

class TorchMap():
    def __init__(self, keys, vals):
        super().__init__()

        sorted_values, sorted_indices = torch.sort(keys)
        self.k = keys[sorted_indices]
        self.v = vals[sorted_indices]
        self._not_found = -1

    def map(self, keys):
        idx = torch.searchsorted(self.k, keys)
        idx = idx.clamp(max=self.k.shape[0] - 1)
        return torch.where(self.k[idx] == keys, self.v[idx], self._not_found)

