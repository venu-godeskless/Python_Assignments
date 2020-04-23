"""
Problem 4: Write a function treemap to map a function over nested list.
"""
def treemap(listing):
    for i, j in enumerate(listing):
        # if i ==type(list):
        if isinstance(j, list):
            treemap(j)
        else:
            listing[i] = listing[i] * listing[i]
    return listing

print(treemap([1, 2, [3, 4, [5]]]))
