'''
Recursion needs 3 things:
  1. Base case
  2. Working towards the base case
  3. Call out

Gets really messy if f(x) and g(x) calls each other in an f(g)). So f(f(x)) is much simpler.

Linear search recursively.
BASE CASES: It can have 1 item, or even no items.



def f(a_list, target): 

*** BASE CASE
#be careful, you can get stuck in an infitine recursion look
  if not a_list: 
#trusy falsy values
    return False 
  #this is our error, we haven't found the list. This is extremely important I think? Mr Park just said that if we didn't get it we fucked up.
  elif len(a_list) == 1:
    if a_list[0] == target:
      return True
    else:
      return False
*** BASE CASE

*** WORKING TOWARDS BASE CASE
ebe:
  current = a_list.pop() #A list got smaller by a single thing, and current is the popped value.
  if current == target:
    return True
  else:
    return f(a_list, target) #This says check the list with that last value again with the smaller list, which goes smaller and smaller.
