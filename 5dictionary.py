''' 
a dictionary is a datatype that stores (key, value) pairs
common operations:
    adding a pair
    removing a pair
    modifying an existing pair
    looking up a value associated with the pair
Dictionary
    Dictionaries also use {} like sets, but their format is drastically different
Keys
    Keys are unique addresses for a dictionary value's location
    Properties:
        Immutable
        Unique: Newest duplicate superceeds the previous declaration
Values
    Values of a dictionary within a key can be any type
Updating a dictionary
    We can:
        Modify existing values by referencing the key
        Add new values by creating a new key
        Overwrite a value at an existing key by referencing and recreating the value for it.
Dictionary FULL Example
            sammy = {
                'username': 'sammy',
                'online': True,
                'followers': 42
            }

            # There are 3 items: each with their unique addresses and value
            # Accessing
            print('Sammy dict:', sammy)
            print('Username:', sammy['username'])
            print('Online Status:', sammy['online'])
            print('Follower Count:', sammy['followers'])
Deletion
    We can delete a key, hence deleting the value
    We can empty the ENTIRE dictionary
    We can DELETE the ENTIRE dictionary (not used often)
# Deletion Example
    sammy = {
        'username': 'sammy',
        'online': True,
        'followers': 42
    }

    del sammy['followers'] # del is a keyword used to help us to execute a removal
    print('followers key deleted:', sammy)

    sammy.clear() # {} is considered an empty dict
    print('emptying out a dictionary', sammy)
    print('--\n\n')

    del sammy
    print('Deleting sammy, should create an error when referenced again', sammy)
Membership
    We can use the in and not in operators to check if a key exists
# Membership Example

    sammy = {
        'username': 'sammy',
        'online': True,
        'followers': 42
    }

    print('Checking for key username:', 'username' in sammy)
    print('Checking if followers is not a key:', 'followers' not in sammy)
Built in functions' interactions with dictionaries
    funct(dictionary))
    we can put the dictionary within the () of a function to do that thing.
# Built-in FUnction Interactions
    sammy = {
        'usernane': 'sammy',
        'online': True,
        'followers': 42
    }

    print('size of dic', len(sammy))
    print('largest key', max(sammy))
    print('dic to list:', list(sammy))
Duplicating a Dictionary and Copy Keys Only
    We can delete the values associated with each key in a dictionary, making it blank. Neat!
# Duplicate a Dictionary Example
    sammy = {
        'username': 'sammy',
        'online': True,
        'followers': 42
    }

    sammy_copy1 = sammy.copy()
    sammy_copy2 = sammy

    sammy['verified'] = True

    print('sammy_copy1:', sammy_copy1)
    print('sammy_copy2:', sammy_copy2)
    print('--')

    # Duplicate keys only

    tammy = tammy.fromkeys(sammy) # Notice that all key's values are None ... aka empty

    print('tammy dict:', tammy)
Dictionary Methods
    Dictionaries have methods we can use.
    Let A and B be a dictionary
    A.keys() returns a sequence of keys/addresses in A
    A.values() returns a sequence of values in A
    A.items() returns a sequence of ('key','value')
    A.update(B) extends A with the dictionary of key,value pairs of B
# Dictionary Method Examples

    sammy = {
        'username': 'sammy',
        'online': True,
        'followers': 42
    }

    sammy_hidden = {
        'pwd' : 'qwerty',
        'location' : 'Toronto, Ontario'
    }

    # printing all the keys of a dict
    print('Sammy Dict Keys:', sammy.keys()) # notice how it prints

    sammy_keys = list(sammy.keys()) # we can listify the .keys() returned
    print('List of sammy_keys', sammy_keys)
    print('--')

    # printing all the values of a dict
    print('Sammy Dict Values:', sammy.values())
    print('Sammy Dict Values as a list:', list(sammy.values()))
    print('--')

    # printing key, value pair of a dict
    print('Sammy Dict key, value pairs:', sammy.items())
    print('Sammy Dict key, value pairs as a list:', list(sammy.items()))
    print('--')

    # getting a value from a dict
    print('Sammy followers value:', sammy.get('followers'))
    print('Same as:', sammy['followers'])
    print('--')

    # updating / extending a dictionary
    sammy.update(sammy_hidden)

    print('Sammy extended with its hidden values:', sammy)
Iterating a Dictionary
    There's three methods
    Iterating the Keys
    Iterating the Vlaues
    Iterating the Key, Value pairs by unpacking
# Iteration Example 1: Keys
    sammy = {
        'username': 'sammy',
        'online': True,
        'followers': 42
    }

    for k in sammy.keys(): #only checks keys
        print('Current key:', k)
    print('--\n')

    # Iteration Example 2: Values

    for v in sammy.values():
        print('Current value:', v)
    print('--\n')

    # Iteration Example 3: Key, Value Pair

    for k, v in sammy.items():
        print('Current Key:', k)
        print('Current Value:', v)
        print()
dict() Constructor Dictionary Comprehension
    We can turn other datatypes into dictionaries
    simiarly to other lists, tuples, and sets, dictionaries can also support comphrehension
    We have to specify where the keys and the values are tho
# dict () Example
    example_data = [
        ('one', 3),
        ('two', 3),
        ('three', 5)
    ]

    data_dict = dict(example_data)
    print('data_dict:', data_dict)
    print('--')

    # Dictionary Comprehension
    # Goal: Take string numerals and assign them with their integer square
    # - keys : string numerals
    # - values: integer squares

    example_data2 = ['1', '2', '3', '4', '5']

    data2_dict = {x : int(x)**2 for x in example_data2}

    print('data2_dict:', data2_dict)