'''
A set is an unordered collection with no duplicate elements in Python 

    sets are {}

    Set is a mathematical way to describe collection of different unique objects.
    By following the operations and characteristics of the mathematical set, we can utilize such data structure in our Python code.
    The mathematical definition of the set can read in more details here.
    Sets can only contain immutable data type (Commonly Strings and Integers)
    

    We can convert 
    lists and tuples into sets by using the set() function

    As sets have no duplicates, they're the fastest to check and index and blahlbalbalba
    Due to its unordered nature of a set, there is no concept of indexing or slicing with a set.
    Set is however iterable.
    Sets are mutable; therefore, we can add and remove values
    There are also methods much lists that can affect the original sets as well




    Much like its mathematical counterpart, sets in Python 3 can utilize its vast operators to help us do complex calculations.
    Most of these operators will have a method counterpart because sets are mutable.
        UNION: |
            # Union Example:
                set1 = set('hello')
                set2 = set('world')

                result = set1 | set2 # | is the union operator ... all the members of both set are combined to a single set
                # Recall that: there are no duplicates
                print('set1 union set 2:', result)
        INTERSECTION: & Items/members that only exist in both
            # Union Example:
                set1 = set('hello')
                set2 = set('world')

                result = set1 & set2 # & is the intersection operator
                print('Intersection of set1 and set2:', result)
        DIFFERENCE: - Items that only exist in the first set and not the second
            # Difference Example:
                set1 = set('hello')
                set2 = set('world')

                result1 = set1 - set2 # - is the difference operator ... this is set1 difference set2
                result2 = set2 - set1 # set2 difference set1

                print('set1 - set2:', result1)
                print('set2 - set1:', result2)
        SYMMETRIC DIFFERENCE: ^ Members that only exist in one or the other set, but not both
            # Symmetric Difference Example:
                set1 = set('hello')
                set2 = set('world')

                result = set1 ^ set2 # ^ is the symmetric difference operator

                print('Symmetric Difference of:', result)
        PROPER SUBSETS: < A proper subset of B  is if all members of A is found in B. But A can't be the exact same.
            # Proper Subset Example:
                set1 = {1,2,3}
                set2 = {1,2,3,4}
                set3 = {1,2,3}
                set4 = set('hello')

                print('Is set1 proper subset of set2?:', set1 < set2) # < is the proper subset operator
                print('Is set1 proper subset of set3?:', set1 < set3)
                print('Is set1 proper subset of set4?:', set1 < set4)
        SUBSETS: A Proper of B is A < B, but A can equal be if we do A <= B
                print('Is set1 a subset of set2?:', set1 <= set2) # <= is the subset operator
                print('Is set1 a subset of set3?:', set1 <= set3) # Notice the difference in value here
                print('Is set1 a subset of set4?:', set1 <= set4)
        PROPER SUPERSETS: > or == A is a superset of B if A > B or A == B
            # Superset Example:
                set1 = {1,2,3,4}
                set2 = {1,2,3,4}
                set3 = {1,2,3}
                set4 = set('hello')

                print('Is set1 superset of set2?:', set1 >= set2) # >= is the proper superset operator
                print('Is set1 superset of set3?:', set1 >= set3)
                print('Is set1 superset of set4?:', set1 >= set4)
    Disjoint: A set behavior property
        Two sets are considered disjointed when they don't share aything
        A and B are sets
        if A & B are empty, A and B are considered disjointed.
        we can check this in pythin with setA.isdisjoint(setB)
        DISJOINT: setA.isdisjoint(setB)
            # Disjoint Example
                # .isdisjoint() is a set method to check for such property between two sets.

                set1 = {1,2,3,4}
                set2 = {5,6,7}
                set3 = {1,2,3,4,5}

                print('set1 intersect set2:', set1 & set2) # Output is an empty set
                print('set1 intersect set3:', set1 & set3) # Output is an non-empty set
                print('--')
                print('set 1 disjoint set 2 check:', set1.isdisjoint(set2)) # Therefore .isdisjoint() evaluates to True
                print('set 1 disjoint set 3 check:', set2.isdisjoint(set3))
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                set1 intersect set2: set()
                set1 intersect set3: {1, 2, 3, 4}
                --
                set 1 disjoint set 2 check: True
                set 1 disjoint set 3 check: False
    Set operators as Methods
        # Union
            a = set('abracadabra')
            b = set('alacazam')

            a.union(b)
            print('Union:', a)

            # Intersection
            a = set('abracadabra')
            b = set('alacazam')

            a.intersection(b)
            print('Intersection:', a)

            # Difference
            a = set('abracadabra')
            b = set('alacazam')

            a.difference(b)
            print('Difference:', a)

            # Symmeteric Difference
            a = set('abracadabra')
            b = set('alacazam')

            a.symmetric_difference(b)
            print('Symmetric Difference:', a)

            # Subset
            a = set('abracadabra')
            b = set('alacazam')

            print('Subset:', a.issubset(b))

            # Superset
            a = set('abracadabra')
            b = set('alacazam')

            print('Superset:', a.issuperset(b))
            print('--')

            # There are no proper subset/superset methods

            # copy
            a = set('abracadabra')
            b = a.copy()
            c = a

            a.add('z')
            print('.copy() examples:')
            print('set a:', a)
            print('set b:', b)
            print('set c:', c)


        