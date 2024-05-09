###################### part 1 ###########################

def triangle (x,y,z):
    if x+y>z and x+z>y and y+z>x:
        print("ესეთი სამკუთხედი არსებობს")
    else:
        print("ასეთი გვერდების მქონე სამკუთხედი ვერ იარსებებს")
triangle(5,6 ,6)

######################## part 2 ############################

def names_family(name_string):
    name=name_string.split( )
    print(name)
name="nia deme nanuka"
names_family(name)


