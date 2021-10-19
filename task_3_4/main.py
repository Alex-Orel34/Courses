st = input()
index = len(st) // 2-1
print(f'letter in the middle {st[index]}')
if st[index] == st[0]:
    st1 = st[1:-1:]
    print(st1)
