#Make an array
atr_lab_members=["Chris","Bailey","Mustafa","Derron","Sean","Sophie"]

#Go through each element, without knowing where it is in the array
for member in atr_lab_members:
    print(member)

#Get the length of the array, aka how many elements there are
number_of_members=atr_lab_members.__len__()

#Do this for each number in the range of 0 to number_of_members-1
for index in range(number_of_members):
    member=atr_lab_members[index]
    print(f"{index}: {member}")

