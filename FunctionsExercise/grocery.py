def grocery_store(**kwargs):
    receipt = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    result = ''
    for key, value in receipt:
        result += f"{key}: {value}\n"
    return result

