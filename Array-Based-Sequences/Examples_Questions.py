#1--> Function to ocpy elements of array A to array B.

def copy_array(input_arr):
    copied_array = [None]*len(input_arr)
    for i in range(len(input_arr)):
        copied_array[i] = input_arr[i]
    return copied_array


if __name__ == "__main__":
    copied_array = copy_array([11, 14, 26])
    for i in copied_array:
        print(i)
