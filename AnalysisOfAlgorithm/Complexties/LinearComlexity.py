#-----------------------Linear Comlexity --- O(n)----------------------

"THe compllexity of an algorithm is said to linear if the steps required to comlete the execution of an algorithm increase or decrease linearly with the number of inputs."

#We use this program everyday, lets write a simple program that displays all items in the list to the console.

def linear_algorithm(items):
    for i in items:
        print(i)

linear_algorithm([14, 11, 26, 45])

"""The complexity of the linear_algo() function is linear in the above example since the number of iterations of the for-loop will be equal to the size of the input items array. For instance, if there are 4 items in the items list, the for-loop will be executed 4 times."""