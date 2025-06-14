from functools import reduce

def operate(operator, *args):
    def sum_num():
        return reduce(lambda x, y: x +y, args)
    def sub_num():
        return reduce(lambda x, y: x -y, args)
    def mul_num():
        return reduce(lambda x, y: x *y, args)
    def div_num():
        return reduce(lambda x, y: x /y, args)
    mapper = {
        "+": sum_num,
        "-": sub_num,
        "*": mul_num,
        "/": div_num()
    }
    return mapper[operator]()
