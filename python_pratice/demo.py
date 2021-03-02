a = 1


def fun():
    global a
    a = 2
    print(f'a_num: {a}')
    print(a)
    print('zhe shi yige fangfa')


fun()
