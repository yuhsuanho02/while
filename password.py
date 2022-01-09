password = 'a1234567'
i=3
while i > 0:
    pwd = input('請輸入你的密碼: ')
    if pwd == password:
        print('成功登入')
        break
    else:
        i = i - 1
        print('密碼錯誤!還有', i, '次機會')