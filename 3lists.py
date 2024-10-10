'''
Lists are mutable, which is the BIG difference.

    lists are []

    You can alter them by
    Index
    Copying list to another variable (need to use .copy to not affect original)
    Sort them
    Add item to the end with .append
        .insert(location, item)
    Combine them with
        .extend(list)
        use the + operator
        generate new list with +=
    Remove them with
        .remove(target) removes the first instance
        .pop(target_index) will delete and RETURN the value
        .clear() to empty out the listt
        del can delete an entire instance of a list (deletes objects but that comes later)
        del list[1] can also delete a certain index 
        del list[0:3] can delete by slicing too
    MAJOR DANGER: Deletion During Iteration
    For loops never recheck the value of the list
    Use while loops and index-based deletion
    Make a copy of the list, execute deletion on the copy



    Searching and reversing
    .index(target, start, end) finds the first occurence. Start and end are just borders and they aren't required 100% 
    .count(target) method counts the number of times target occurs.
    .reverse() will reverse the order of the items in the list



    list comprehension is when we want to directly make a list ### this makes no sense lol
        A Square Bracket containing an expression that describes the list
        One or more For clause to explain its members
        Then a zero or more if clauses depending on the complexity of the list





















