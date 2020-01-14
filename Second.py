import builtins

class Person:
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

def print_depth(data):
    counter = 1
    key_depth(data, counter)

def object_depth(data, counter=1):
    print('first_name:', counter + 1)
    print('last_name:', counter + 1)
    print('father:', counter + 1)
    if isinstance(data.father, Person):
        object_depth(data.father, counter + 1)

def key_depth(data, counter=1):
    for key, value in data.items():
        print(key, counter)
        if isinstance(value, dict):
            key_depth(value, counter+1)
        if isinstance(value, Person):
            object_depth(value, counter)

a = {'key1': 1,
     'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b,
        }
    }
}

print_depth(a)
