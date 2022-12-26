
def find_max(data):
    """Return the highest number present in the non empty python list"""
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest


print(find_max([1, 2, 3, 1000]))