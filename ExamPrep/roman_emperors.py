def list_roman_emperors(*args, **kwargs):
    successful = {}
    unsuccessful = {}

    for emperor, status in args:
        if status:
            successful[emperor] = kwargs[emperor]
        else:
            unsuccessful[emperor] = kwargs[emperor]

    successful = sorted(successful.items(), key= lambda kvp: (-kvp[1], kvp[0]))
    unsuccessful = sorted(unsuccessful.items(), key=lambda kvp: (kvp[1], kvp[0]))

    result = f'Total number of emperors: {len(kwargs)}\n'
    if successful:
        result += 'Successful emperors:\n'
        for e, y in successful:
            result += f"****{e}: {y}\n"
    if unsuccessful:
        result += 'Unsuccessful emperors:\n'
        for e, y in unsuccessful:
            result += f"****{e}: {y}\n"

    return result