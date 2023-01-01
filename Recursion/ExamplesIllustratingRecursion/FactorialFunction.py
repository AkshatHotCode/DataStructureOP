#The factorial function is important because it is known to equal the number of ways in which n distinct items can be arranged into a sequence,
#that is the number of permutations of n items.

#Recursion Defination
"""n! = 1, if n = 0
   n! = n * (n-1), if n => 1"""

#Python Code

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#This function does not use any explicit loops. Repetition, is provided by the repeated recursive invocations of the function. There is
#no circulairty in this definition, because each time the fucntion is invoked, its argument is smaller by one, and when a base case is reached,
#no further recursive calls are made.
