def math_operations(*args, **kwargs):
    operations = {
        'a': lambda x, y: x+ y,
        's': lambda x, y: x -y,
        'd': lambda x, y: x / y if y !=0 else x,
        'm': lambda x, y: x * y
    }
    keys = list(operations.keys())
    for i in range(len(args)):
        key = keys[i % 4]
        operation = operations[key]
        kwargs[key] = operation(kwargs[key], args[i])
    result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    return "\n".join(f"{key}: {value:.1f}" for key, value in result)

