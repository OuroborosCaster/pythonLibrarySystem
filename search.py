def search(library):
    print('欢迎使用搜索功能'.center(30))
    keyword = input('请输入搜索关键字：'.rjust(19))
    result = []
    for i in range(1, len(library) + 1):
        if keyword in library[i]['书名'] or keyword in library[i]['作者'] or keyword in library[i]['出版方']:
            result.append(i)
    return result
