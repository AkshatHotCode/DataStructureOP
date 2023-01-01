 #We will see the classic recursive algorithm, binary search, that is used to efficiently locate a
#value within a sorted sequence of n elements. This ia among the most important of computer algo, and it is the reason that we so often store data is
#in sorted order.

#When the sequence is in unsorted, the standard approch to search for a target valur is to use a loop and examine every element, until either finding the
#target or exhauting the data set. This is known as sequential search algorithm, and runs in O(n) time, linear time since every element is inspected in
#worst case.

#When the sequence is sorted and indexable, there is a much more efficient algorithm.


def binary_search(data, target, low, high)
    """Return True if the target is found in indicated portion of a Python List.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            #recur on the portion left to the middle
            return binary_search(data, target, low, mid-1)
        else:
            #recur on the portion right to the middle
            return binary_search(data, target, mid+1, high)


#Where sequential search works on O(n) time, the more efficient binary runs in O(log n) time. Shows, significant improvement, given that if n is in billion
#log n is only 30.