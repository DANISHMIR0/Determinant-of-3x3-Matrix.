print("--> R = Row, C = Colum <--")
print("!! Its 3x3 Matrix's  To Find |A| !!")
a = int(input("Enter The R1xC1 No. (9) : "))
b = int(input("Enter The R1xC2 No. (8) : "))
c = int(input("Enter The R1xC3 No. (7) : "))
d = int(input("Enter The R2xC1 No. (6) : "))
e = int(input("Enter The R2xC2 No. (5) : "))
f = int(input("Enter The R2xC3 No. (4) : "))
g = int(input("Enter The R3xC1 No. (3) : "))
h = int(input("Enter The R3xC2 No. (2) : "))
i = int(input("Enter The R3xC3 No. (1) : "))
x = (e*i-h*f)
y = (d*i-g*f)
z = (d*h-g*e)
aa = x*a
bb = y*b
cc = z*c
Det = aa-bb+cc
print("Det of Given Matrix Is: ", [Det])
