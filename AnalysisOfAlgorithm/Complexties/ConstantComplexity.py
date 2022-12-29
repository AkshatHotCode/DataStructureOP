#1 --> Constant Complexity - O(c)

"""The complexity of the algorithm is said to be constant if the steps required to complete the excution of an element of an algorithm remain constant, irrespective of the number of input."""
def constant_algorithm(items):
    result = items[0] * items[0]
    print(result)

constant_algorithm([14, 11, 26])

"""Therefore, irrespective of the input sixe, or the number of items in the input list items, the algorithm performs only 2 steps: 1st --> Finding the sqaure, 2nd --> Printing.
Hence the complexity remains constant."""