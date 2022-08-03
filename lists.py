bicycles = ['track', 'connadole', 'redline']
print(bicycles)
print(bicycles[0].title())
message = f'My first bicycle was {bicycles[-2].upper()}'
print(message)
bicycles[0] = 'bugatti'
print(bicycles)
# adding elements
bicycles.append('honda')
bicycles.append('yamaha')
print(bicycles)
# inserting elemets
bicycles.insert(0, 'suzuki')
print(bicycles)
# deleting elements
del bicycles[0]
print(bicycles)
popped = bicycles.pop()
print(popped)
print(bicycles)
first_owned = bicycles.pop(2)
print(bicycles, first_owned)
bicycles.remove('honda')
print(bicycles)
# sorting list
bicycles.append('avalache')
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles))
print(bicycles)
bicycles.reverse()
print(bicycles)
# finding the lenght of a List
print(len(bicycles))
# looping lists
for bicycle in bicycles:
    print(bicycle)
numbers_list = []
for value in range(1,10):
    numbers_list.append(value)
print(numbers_list)
numbers_list = []
print(numbers_list)
numbers_list = list(range(2,11,2))
print(numbers_list)
squar_num = []
for num in numbers_list:
    squar_num.append(num**2)
print(squar_num, max(squar_num), min(squar_num), sum(squar_num))
# List comprehensions
squares = [value**3 for value in range(1,12)]
print(squares)
numbers_list = list(range(1,1000001))
print(numbers_list)
print(max(numbers_list), min(numbers_list), sum(numbers_list))
odd_numbers = list(range(1,21,2))
print(odd_numbers)
cube_num = [num**3 for num in range(1,10)]
print(cube_num)
# Slicing a list
