import add, search

print('欢迎访问图书管理系统'.center(30))
library = {1: {'书名': '示例', '作者': '佚名', '出版方': '演示一号出版社', '价格': '40.55'}}
"""library = {1: {'书名': '示例', '作者': '佚名', '出版方': '演示一号出版社', '价格': '40.55'},
           2: {'书名': '西游记', '作者': '吴承恩', '出版方': '人民大学出版社', '价格': '23.84'},
           3: {'书名': '西游补', '作者': '佚名', '出版方': '首次出版社', '价格': '21.0'},
           4: {'书名': '三国演义', '作者': '罗贯中', '出版方': '新华出版社', '价格': '1900000.0'},
           5: {'书名': 'Harry Potter', '作者': 'J K Rowling', '出版方': '新华文轩', '价格': '34.5'},
           6: {'书名': 'Harry Potter and the secret chamber', '作者': 'JK Rowling', '出版方': '新华文轩',
               '价格': '209.0'},
           7: {'书名': 'The Lord of the Ring', '作者': 'JJR 托尔金', '出版方': '四川大学出版社', '价格': '12.0'}}"""


def main():
    while True:
        print('请选择要使用的功能：1.添加书籍 2.查询书籍 3.退出'.center(30))
        opt = input(''.center(18))

        match opt:
            case '1':
                while True:
                    book = add.add(library)
                    library[len(library) + 1] = book
                    print('新书籍已成功添加！是否继续添加？1.继续 2.回到菜单'.center(30))
                    i = input(''.center(18))
                    match i:
                        case '1':
                            continue
                        case '2':
                            break
                        case _:
                            print('指令无效！默认回到主菜单。'.center(30))
                            break
            case '2':
                while True:
                    result = search.search(library)
                    if len(result) != 0:
                        print('已搜索到下列结果：'.center(30))
                        index = 1
                        for i in result:
                            print('%d. 书名：%s 作者：%s 出版方：%s 价格：%s'.center(30) % (index,
                                                                                        library[i]['书名'],
                                                                                        library[i]['作者'],
                                                                                        library[i]['出版方'],
                                                                                        library[i]['价格']))
                            index += 1
                    else:
                        print('未搜索到结果。'.center(30))
                    print('是否继续搜索？1.继续 2.回到菜单'.center(30))
                    i = input(''.center(18))
                    match i:
                        case '1':
                            continue
                        case '2':
                            break
                        case _:
                            print('指令无效！默认回到主菜单。'.center(30))
                            break
            case '3':
                print('谢谢使用！'.center(30))
                print(library)
                exit(len(library))
            case _:
                print('请输入有效指令！'.center(30))
                continue


main()
