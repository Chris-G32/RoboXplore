#### Bad

length = 10
width = 20
area = length * width
print(area)

length = 15
width = 10
area = length * width
print(area)

length = int(input('Enter a length:'))
width = int(input('Enter a width:'))
area = length*width
print(area)

#### Better

def printArea(length, width):
    print(length * width)

printArea(10, 20)
printArea(10, 15)
length = int(input('Enter a length:'))
width = int(input('Enter a width:'))
printArea(length, width)    

