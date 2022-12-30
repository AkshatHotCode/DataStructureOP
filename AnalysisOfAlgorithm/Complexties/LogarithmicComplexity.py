#------------------------------------LOGARITHMIX COMLEXITY--------------------------------------------

"""Some algorithms achieve logarithmic complexity, such as Binary Search. Binary Search searches for an element in an array, by checking the middle of an array, and pruning the half in which the element isn't. It does this again for the remaining half, and continues the same steps until the element is found. In each step, it halves the number of elements in the array."""

def complex_algo(items):

    for i in range(5):
        print("Python is awesome")

    for item in items:
        print(item)

    for item in items:
        print(item)

    print("Big O")
    print("Big O")
    print("Big O")

complex_algo([4, 5, 6, 8])