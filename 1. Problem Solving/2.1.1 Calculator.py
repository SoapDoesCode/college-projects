a = 0 # initial decleration
b = 0 # initial decleration
c = 0 # initial decleration

a = int(input("What should variable A equal?\nA = ")) # get input for A
b = int(input("What should variable B equal?\nB = ")) # get input for B
c = int(input("What should variable C equal?\nC = ")) # get input for C

x = (a * b) + c # calculate a * b + c
y = (b + c) / a # calculate (b + c) FLOOR DIV a
z = x // y # calculate x FLOOR DIV y
w = x % y # calculate x MOD y

x += y # add y to x

print(f"""Output:
X = {x}
Y = {y}
Z = {z}
W = {w}""") # output the X, Y, Z, W values