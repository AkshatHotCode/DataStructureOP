#-----------------------Linear Comlexity --- O(n)----------------------

"THe compllexity of an algorithm is said to linear if the steps required to comlete the execution of an algorithm increase or decrease linearly with the number of inputs."

#We use this program everyday, lets write a simple program that displays all items in the list to the console.

def linear_algorithm(items):
    for i in items:
        print(i)

linear_algorithm([14, 11, 26, 45])

"""The complexity of the linear_algo() function is linear in the above example since the number of iterations of the for-loop will be equal to the size of the input items array. For instance, if there are 4 items in the items list, the for-loop will be executed 4 times."""

"""An important thing to note is that with large inputs, constants tend to lose value. This is why we typically remove constants from Big-O notation, and an expression such as O(2n) 
is usually shortened to O(n). Both O(2n) and O(n) are linear - the linear relationship is what matters, not the concrete value. For example, let's modify the linear_algo():"""

def linear_algorithm1(items):
    for i in items:
        print(i)

    for i in items:
        print(i)

"""There are two for-loops that iterate over the input items list. Therefore the complexity of the algorithm becomes O(2n), however in the case of infinite items in the input list,
the twice of infinity is still equal to infinity. We can ignore the constant 2 (since it is ultimately insignificant) and the complexity of the algorithm remains O(n)."""