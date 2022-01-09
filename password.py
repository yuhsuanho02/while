password = 'a1234567'
i=3
while i > 0:
    i = i - 1
    pwd = input('請輸入你的密碼: ')
    if pwd == password:
        print('成功登入')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('帳戶已鎖定!請重新更該密碼!')