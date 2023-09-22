#Exit when input is 0
number=0
entry=None
while entry is not 0:
    print("Enter a number to add or 0 to stop")
    #Make the string a number, this is called casting
    entry=input()
    entry=int(entry)
    number=entry+number
print(number)