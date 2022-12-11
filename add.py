def add(library):
    print('欢迎使用添加功能'.center(30))
    dump = True
    while dump:
        name = input('请输入书名：'.rjust(19))
        for i in range(1, len(library) + 1):
            j=0
            if name == library[i]['书名']:
                print('该书已在库中！')
                j+=1
                break
        if j==0:
            dump = False
    author = input('请输入作者：'.rjust(19))
    publisher = input('请输入出版社：'.rjust(19))
    while True:
        price = input('请输入价格：'.rjust(19))
        try:
            price = float(price)
            break
        except ValueError:
            print('请输入数字！'.rjust(19))
    price = str(round(price, 2))
    book = {'书名': name, '作者': author, '出版方': publisher, '价格': price}
    print('您已添加以下书籍：'.center(30))
    print('书名：%s 作者：%s 出版方：%s 价格：%s'.center(30) % (name, author, publisher, price))
    return book
