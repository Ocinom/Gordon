phones = {
    'brand 1' : 'model 1',
    'brand 2' : 'model 2',
    'brand 3' : 'model 3'
}

def mod_desc(brand, desc):
    if brand not in phones.keys():
        print('Brand does not exist in the dictionary. Try again.')
    phones[brand] = desc

def del_brand(brand):
    if brand not in phones.keys():
        print('Brand does not exist in the dictionary. Try again.')
        return
    phones.pop(brand)

def add_brand(brand):
    if brand in phones.keys():
        print('Brand already exists in the dictionary. Nice try.')
        return
    phones[brand] = 'NULL'


while True:

    choice = input("""
    Choose from 0, 1, 2, 3, and 4:
    0: Quit
    1 : Print the dictionary
    2 : Modify the description of a brand
    3 : Delete a brand from the list
    4 : Add a brand to the list
    """)
    if choice == '0':
        break
    elif choice == '1':
        for key in phones.keys():
            print(key + ', ' + phones[key])
    elif choice == '2':
        brand = input('Type the brand you would like to modify:  ')
        desc = input('Type the description you would like to modify it to:  ')
        mod_desc(brand, desc)
    elif choice == '3':
        brand = input('Type the brand you would like to remove:  ')
        del_brand(brand)
    elif choice == '4':
        brand = input('Type the brand you would like to add:  ')
        add_brand(brand)
    else:
        print('Invalid input detected. Please select an input from 0 - 4')