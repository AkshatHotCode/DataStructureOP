#------------------------------WORST CASE AND BEST CASE------------------------------

#Usually, when someone asks you about the complexity of an algorithm - they're interested in the worst-case complexity (Big-O). Sometimes, they might be interested in the best-case complexity as well (Big-Omega).

#To understand the relationship between these, let's take a look at another piece of code:

def search_algo(num, items):
    for item in items:
        if item == num:
            return True
        else:
            pass

nums = [2, 4, 6, 8, 10]

print(search_algo(2, nums))

"""In the script above, we have a function that takes a number and a list of numbers as input. It returns true if the passed number is found in the list of numbers, otherwise, it returns None.
If you search for 2 in the list, it will be found in the first comparison. This is the best case complexity of the algorithm in that the searched item is found in the first searched index. 
The best case complexity, in this case, is O(1). On the other hand, if you search 10, it will be found at the last searched index. The algorithm will have to search through all the items in
the list, hence the worst-case complexity becomes O(n)."""