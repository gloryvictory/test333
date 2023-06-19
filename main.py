mylist = ['Привет иВан','Пока ИГОрь','Здравс твуй СветлАНА']
#Привет Иван, Привет Игорь, Привет Светлана

def print_hi(name):
    mylist = ['Привет иВан', 'Пока ИГОрь', 'Здравс твуй СветлАНА']
    for item in mylist:
        print(item)
        qqq = item.upper()
        print(qqq)

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    aa = 'qq'
    # qq => QQ
    aa = aa.upper()
    print(aa)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')




