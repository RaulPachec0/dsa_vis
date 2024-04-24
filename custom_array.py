class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __str__(self):
        return '[' + ', '.join(str(item) if item is not None else '-' for item in self.data) + ']'

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value




if __name__ == '__main__':
    arr = Array(5)
    arr[0] = 10
    arr[1] = 25
    arr[2] = 30
    arr[3] = 80
    arr[4] = 50
    print("Array:", arr)