def fill_the_box(height, length, width, *args):
    volume = height * length * width
    boxes = 0
    for item in args:
        if item == "Finish":
            break
        boxes += item

    if volume > boxes:
        return f"There is free space in the box. You could put {volume-boxes} more cubes."
    return f"No more free space! You have {boxes - volume} more cubes."

