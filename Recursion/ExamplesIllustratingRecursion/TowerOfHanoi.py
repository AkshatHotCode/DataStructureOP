def move(n, src, dest, temp):
    if n >= 1:
        move(n-1, src, temp, dest)
        print("Movee %d -> &d" % (src, dest))
        move(n-1, temp, dest, src)