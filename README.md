# fast_py_dict: A 50-100x Faster Read Only Dict for Python


    $ python bench.py
    N = 1000 running bench for 1000 times
    func=<function bench.<locals>.py_map at 0x7fa147c1e5e0>, dt=0.00s, 1.65 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1e940>, dt=0.00s, 11.85 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1e790>, dt=0.00s, 3.36 M lookups/s
    N = 10000 running bench for 100 times
    func=<function bench.<locals>.py_map at 0x7fa147c1e790>, dt=0.01s, 1.67 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1ea60>, dt=0.00s, 8.36 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1e940>, dt=0.00s, 35.44 M lookups/s
    N = 100000 running bench for 10 times
    func=<function bench.<locals>.py_map at 0x7fa147c1e940>, dt=0.07s, 1.48 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1eb80>, dt=0.02s, 5.75 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1ea60>, dt=0.00s, 85.36 M lookups/s
    N = 1000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa147c1ea60>, dt=0.97s, 1.03 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1eca0>, dt=0.37s, 2.71 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1eb80>, dt=0.01s, 150.09 M lookups/s
    N = 10000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa147c1eb80>, dt=8.06s, 1.24 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1edc0>, dt=8.99s, 1.11 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1eca0>, dt=0.14s, 69.65 M lookups/s
    N = 100000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa147c1eca0>, dt=101.77s, 0.98 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa147c1eee0>, dt=214.22s, 0.47 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa147c1edc0>, dt=2.04s, 49.02 M lookups/s
