import torch
import numpy as np
import timeit
import math

from fast_dict import TorchMap

# for benchmark
class NumpyMap():
    def __init__(self, keys, vals):
        super().__init__()

        sorted_indices = np.argsort(keys)
        self.k = np.array(keys)[sorted_indices]
        self.v = np.array(vals)[sorted_indices]
        self._not_found = -1

    def map(self, keys):
        idx = np.searchsorted(self.k, keys)
        idx = np.clip(idx, 0, self.k.shape[0] - 1)
        return np.where(self.k[idx] == keys, self.v[idx], self._not_found)

def bench(N = 1*1000*1000):
    k = np.random.randint(1, 9223372036854775807, size=N, dtype=np.int64)
    v = np.random.randint(1, 9223372036854775807, size=N, dtype=np.int64)
    k_tensor = torch.tensor(k)
    v_tensor = torch.tensor(v)

    my_py_map = {}
    my_py_map = {i:j for i,j in zip(k, v)}

    def py_map():
        ret = []
        for i in k:
            if i in my_py_map:
                ret.append(my_py_map[i])
            else:
                ret.append(-1)

        return torch.tensor(ret)


    my_torch_map = TorchMap(k_tensor, v_tensor)

    my_np_map = NumpyMap(k, v)

    def torch_map():
        return my_torch_map.map(k_tensor)

    def np_map():
        return my_np_map.map(k)

    number_times = math.ceil(1e6/N)
    print(f'N = {N} running bench for {number_times} times')
    for func in [py_map, np_map, torch_map]:
        dt = timeit.timeit(func, number=number_times) / number_times
        print(f'{func=}, {dt=:.2f}s, {N/dt/1e6:.2f} M lookups/s')

    if N <= 10*1000:
        assert torch.equal(py_map(), torch_map())
        assert np.array_equal(np_map(), torch_map().numpy())

for n in (1000, 10*1000, 100*1000, 1000*1000, 10*1000*1000, 100*1000*1000):
    bench(n)
