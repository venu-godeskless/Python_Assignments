
"""
Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
"""

def flatten_dict(a,x=''):
    result={}

    for keys,values in a.items():
        new_key=x+keys

        if isinstance(            values,dict):
            result.update(flatten_dict(values,new_key+'.'))
        else:
            result[new_key]=values

    return result

print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))