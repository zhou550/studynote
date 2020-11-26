from functools import reduce

def formatName(name):
    return name[0].upper()+name[1:].lower();
def prod(list):
    def multi(x, y):
        return x * y;

    return reduce(multi, list)


if __name__ == '__main__':
    list1 = ['adam', 'LISA', 'Bart']
    str=map(formatName,list1)
    print(list(str))
    list2 = [1, 2, 3, 4, 5]
    print(prod(list2))
