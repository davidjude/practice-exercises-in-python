#creating a function
#def my_function(fname,lname):#number of argument
#    print(fname + " " + lname)
#my_function("emil","dave")


def my_function(*kids):#we use asteris* when we dont know the number of item we are using
    print("the youngest child is" + kids[2])

my_function("emil","tobias","linus")