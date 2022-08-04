cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car != 'subaru':
        print(car.lower())
    else:
        print(car.title())

banned_users = ['andrew', 'bob', 'john']
user = 'mary'
if user not in banned_users:
    print(f'{user.title()}, you can post a response.')

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry, we don\'t have {requested_topping}')


