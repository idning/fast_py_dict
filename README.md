# fast_py_dict: A 50-100x Faster Read Only Dict for Python


    $ python bench.py
    N = 1000 running bench for 1000 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51c8b0>, dt=0.00s, 1.68 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51cdc0>, dt=0.00s, 12.10 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51c940>, dt=0.00s, 2.40 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51cd30>, dt=0.00s, 9.16 M lookups/s
    N = 10000 running bench for 100 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51cd30>, dt=0.01s, 1.67 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51c8b0>, dt=0.00s, 8.32 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51cdc0>, dt=0.00s, 2.40 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51c940>, dt=0.00s, 35.28 M lookups/s
    N = 100000 running bench for 10 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51c940>, dt=0.07s, 1.50 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51cd30>, dt=0.02s, 5.69 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51c8b0>, dt=0.05s, 1.89 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51cdc0>, dt=0.00s, 90.31 M lookups/s
    N = 1000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51cdc0>, dt=0.79s, 1.27 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51c940>, dt=0.33s, 3.03 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51cd30>, dt=0.64s, 1.56 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51c8b0>, dt=0.01s, 142.90 M lookups/s
    N = 10000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51c8b0>, dt=10.33s, 0.97 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51cdc0>, dt=9.39s, 1.07 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51c940>, dt=8.81s, 1.13 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51cd30>, dt=0.14s, 70.13 M lookups/s
    N = 100000000 running bench for 1 times
    func=<function bench.<locals>.py_map at 0x7fa0fb51cd30>, dt=111.16s, 0.90 M lookups/s
    func=<function bench.<locals>.np_map at 0x7fa0fb51c8b0>, dt=187.46s, 0.53 M lookups/s
    func=<function bench.<locals>.mdict_map at 0x7fa0fb51cdc0>, dt=103.43s, 0.97 M lookups/s
    func=<function bench.<locals>.torch_map at 0x7fa0fb51c940>, dt=2.07s, 48.28 M lookups/s

