#Calculate the sum of list of numbers.
def sumofnum(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + sumofnum(data[1:])

#Recursion list sum --> test data[1, 2, [3, 4], [5, 6]]
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
	    if type(element) == type([]):
		    total = total + recursive_list_sum(element)
	    else:
		    total = total + element
    return total

#Fsctorial of non-negative integer
def fact(n):
    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)

#Fibonacci Series --> 1,1,2,3,5,8,13........
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibo(n-1) + (fibo(n-2)))

#Sum of a non-negtaive integer(345-->12)
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 +sumDigits(int(n/10))

#Sum of the positive integers of n + (n-2) +(n-4)....
def sum_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series(n-2)

#Calculating the harmomic sum of n-1
# Harmonic Sum --> is the sum of reciprocals of the positive integers.
def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

#Calculating the geometric sum on n-1
# Geometric SUm --> is a series with a constant ratio between successive terms
def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric_sum(n-1)

#Calculating the value of 'a' to the power 'b'
def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
         return a * power(a, b-1)


if __name__ == '__main__':

    print(sumofnum([1+2+15]))
    print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))
    print(fact(0))
    print(fibo(3))
    print(sumDigits(345))
    print(sum_series(10))
    print(harmonic_sum(4))
    print(geometric_sum(7))
    print(power(3, 4))