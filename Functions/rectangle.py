def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    def area():
        return width * length
    def perimeter():
        return 2 * width + 2 * length
    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'