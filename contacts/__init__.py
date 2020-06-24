from contacts.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 연락처 추가')
        print('2. 연락처 이름 검색')
        print('3. 연락처 전체 목록')
        print('4. 연락처 이름 삭제')
        return input('Menu\n')

    app = Controller()
    while 1:
        menu = print_menu()
        #if menu == '1':
            #app.register(input('이름\n'),
                         #input('전화번호\n'),input('이메일\n'),input('주소\n'))

        if menu == '1':
            print('휴대폰 작동중 삐릭삐릭 ')
            name = str(input('이름은?\n'))
            phone = str(input('번호는?.\n'))
            email = str(input('메일주소는?\n'))
            addr = str(input('주소는? \n'))

            result = app.register(name, phone, email, addr)
            print('%s 등록완료!' % result)


        if menu == '2':
            print(app.search(input('이름\n')))

        if menu == '3':
            list = app.list()
            temp = []
            for i in list:
                temp.append(i)
            print(temp)
        if menu == '4':
            app.remove(input('이름\n'))
        if menu == '0': break
