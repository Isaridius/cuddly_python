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
Dictionary Example
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
    