def greet_user(user_name):
    '''Display a simple greeting'''
    print(f'Hello {user_name}')

greet_user(input('What is yout name?\n'))

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_designs(unprinted, completed):
    while unprinted:
        completed.append(unprinted.pop())
    print(completed)
print(unprinted_designs)

print_designs(unprinted_designs[:], completed_models)
