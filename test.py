# A = [1, 2, 11, 14, 110]
# N = 5
#
# def minmax(A, N):
#     max = A[0]
#     min = A[0]
#     for i in range(1, N):
#         if A[i] > max:
#             max = A[i]
#         elif A[i] < min:
#             min = A[i]
#     summaxmin = min + max
#     print(summaxmin)
#
# minmax(A, N)

def insertionsort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
        print(cur)

insertionsort([11, 1, 15, 14, 999, 3])
