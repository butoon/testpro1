import money


def select_money():
    sendmoney = 1000
    if money.is_add_money == True:
        print('发工资啦')
        money.saved_money = money.saved_money + sendmoney
        print(f'当前工资为: {money.saved_money}')
    else:
        print(f'还没发工资,当前工资为：{money.save_money}')
