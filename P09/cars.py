cars = {
    'Ford' : 'Mustang',
    'Nissan' : 'Sunny',
    'Toyota' : 'Corolla',
    'Bugatti' : 'Veyron'
}

def add_car(make: str, model: str):
    cars[make] = model

while True:
    choice = input(
    """
    Here are some cars.

    To display the cars, select 1.
    To add a car, select 2.

    To quit, select 0\n
    """)
    if choice == '1':
        for key in cars.keys():
            print(key + ', ' + cars[key])
    elif choice == '2':
        make = input('Type the make of your car: ')
        model = input('Type the model of your car: ')
        add_car(make, model)
    elif choice == '0':
        break
    else:
        print('Invalid input detected. Please type 0, 1, or 2')