"""
data = {
    'a': {
        'b': {
            'c': True
        },
        'd':{
            'e': True,
            'f':{
                'g': True
            }
        }
    },
    'h': True,
    'i': {}
}
"""

def file_hash(data):
    path_list = []
    for k,v in data.iteritems():
        if v == True:
            path_list.append(k)
        else:
            path_list += (recursive_path(k, v))
    return path_list

def recursive_path(path_so_far, data):
    path = []
    for k,v in data.iteritems():
        if v == True:
            path.append(path_so_far + k)
        else:
            path += (recursive_path(path_so_far + k, v))
    return path
