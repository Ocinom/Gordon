cpus = {
    'cpu 1' : ['make 1', 'size 1'],
    'cpu 2' : ['make 2', 'size 2'],
    'cpu 3' : ['make 3', 'size 3'],
}

def get_args(cpu: str):
    if cpu not in cpus.keys():
        raise KeyError('CPU does not exist.')
    return cpus[cpu]

print(get_args('cpu 1'))
print(get_args('cpu 2'))
print(get_args('cpu 3'))
