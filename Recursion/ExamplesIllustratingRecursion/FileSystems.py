import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)
    if os.path.getsize(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:7}'.format(total), path)
    return total

if '__name__' == '__main__':
    path = r"C:\Users\User\Desktop\Bank Statement Examples\tester"
    print(disk_usage(path))