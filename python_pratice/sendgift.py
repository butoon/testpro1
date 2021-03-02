have_gitf = False


def send():
    print('发礼物啦')
    global have_gitf
    have_gitf = True


def show():
    if have_gitf == True:
        print("收到礼物辣")
    else:
        print('没有收到礼物')


if __name__ == '__main__':
    send()
    show()
