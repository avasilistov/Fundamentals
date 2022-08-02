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