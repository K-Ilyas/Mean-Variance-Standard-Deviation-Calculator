import numpy as np

def calculate(list_):
    if len(list_) < 9 :
        raise ValueError("List must contain nine numbers.")
    
    np_array = np.array(list_)
    np_array = np_array[0:9].reshape((3,3))

    calculations = dict({
        'mean': [list(np_array.mean(axis=0)), list(np_array.mean(axis=1)), np_array.mean()],
        'variance': [list(np_array.var(axis=0)), list(np_array.var(axis=1)), np_array.var()],
        'standard deviation': [list(np_array.std(axis=0)), list(np_array.std(axis=1)), np_array.std()],
        'max': [list(np_array.max(axis=0)), list(np_array.max(axis=1)), np_array.max()],
        'min': [list(np_array.min(axis=0)), list(np_array.min(axis=1)), np_array.min()],
        'sum': [list(np_array.sum(axis=0)), list(np_array.sum(axis=1)), np_array.sum()]

    })

    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))