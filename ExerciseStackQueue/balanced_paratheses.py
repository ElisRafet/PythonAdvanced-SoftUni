expression = input()
opening_par = '({['
closing_par = ')}]'
par_stack = []

for char in expression:
    if char in opening_par:
        par_stack.append(char)
    else:
        if not par_stack:
            print('NO')
            break
        last_par = par_stack.pop()
        if opening_par.index(last_par) != closing_par.index(char):
            print('NO')
            break
else:
    if par_stack:
        print('NO')
    else:
        print('YES')
        