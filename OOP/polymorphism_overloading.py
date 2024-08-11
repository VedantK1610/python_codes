from multipledispatch import dispatch


class FindArea:
    @dispatch(int, int)
    def Area(l, b):
        area = l * b
        print(area)

    @dispatch(int)
    def Area(r):
        area = 3.14 * (r * r)
        print(area)


obj = FindArea()
obj.Area(2, 4)
obj.Area(3)