#### Bad
a = 10
b = 20
c = a * b

print('Area:', c)

#### Better
width = 10
length = 20
area =  width * length

print('Area:', area)


#### A more complex example

# Adds an object an array safely
# If the object already exists in the array, it will not
# be added and the function returns False. If the object
# does not exist in the array, then it gets added and the
# function returns true
def add_object_to_array_safely(self, object_to_add):
    if(self._array.contains(object_to_add)):
        print("Object already in array!")
        return False
    self._array.append(object_to_add)
    return True