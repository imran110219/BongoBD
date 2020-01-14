def print_depth(data):
    counter = 1
    key_depth(data, counter)

def key_depth(data, counter=1):
    for key, value in data.items():
        print(key, counter)
        if isinstance(value, dict):
            key_depth(value, counter+1)


a = {'key1': 1,
     'key2': {
         'key3': 1,
         'key4': {
             'key5': 4
            }
        }
     }


print_depth(a)
