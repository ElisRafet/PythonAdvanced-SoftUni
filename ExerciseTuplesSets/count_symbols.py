text = tuple(input())
unique_symbols = set(char for char in text)
for char in sorted(unique_symbols):
    print(f"{char}: {text.count(char)} time/s")