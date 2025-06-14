def classify_books(*args, **kwargs):
    fiction = {}
    non_fiction = {}
    book_codes = {v: k for k, v in kwargs.items()}
    for genre, name in args:
        if genre == "fiction":
            fiction[name] = book_codes[name]
        elif genre == "non_fiction":
            non_fiction[name] = book_codes[name]

    sorted_fictions = sorted(fiction.items(), key=lambda kvp: kvp[1])
    sorted_nonfiction = sorted(non_fiction.items(), key=lambda kvp: kvp[1], reverse=True)
    result = ''
    if sorted_fictions:
        result += 'Fiction Books:\n'
        for name, code in sorted_fictions:
            result += f'~~~{code}#{name}\n'
    if sorted_nonfiction:
        result += 'Non-Fiction Books:\n'
        for name, code in sorted_nonfiction:
            result += f'***{code}#{name}\n'

    return result

print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
