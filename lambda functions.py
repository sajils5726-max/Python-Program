area=lambda a:a*a
side= int(input("Enter the side of square:"))
print("area of square is:",area (side))
area=lambda l,b:l*b
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle:",area(l,b))
tarea=lambda c,b:0.5*c*b
c=int(input("Enter the breadth of the triangle:"))
h=int(input("Enter the height of the triangle:"))
print("Area is:",tarea(c,b))
