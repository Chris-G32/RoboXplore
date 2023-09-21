#This takes the average of two numbers
def average(left,right):
    return (left+right)/2

#This removes spaces from the string
def delete_spaces(string):
    SPACE=" "
    spaceless_str=""
    for i in string:
        if i is not SPACE:
            spaceless_str+=i
    return spaceless_str

#This removes tabs
def delete_tabs(string):
    tabless_string=""
    TAB="\t"
    for i in string:
        if i is not TAB:
            tabless_string+=i
    return tabless_string
#This gets rid of all whitespace
#Whitespace is any character that serves to space other characters out, so spaces, tabs, enters
def delete_whitespace(inp):
    inp=delete_spaces(inp)
    inp=delete_tabs(inp)
    return inp


print(average(1,2))

string="\tAT\tR  L\ta\tb"
print(string)
no_whitespace=delete_whitespace(string)
print(no_whitespace)