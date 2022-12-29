y = int(input())
if (y % 400 == 0) or (y % 100 != 0 and y %4 == 0):
    print(y,"is leap year.")
else:
    print(y,"isn't leap year.")