userReply = input("do you need to ship a package? (enter yes or no) ")
if userReply == "yes":
    print("we will help you in ship a package")
else:
    print("please come back when you need to ship a package. thank you")
userReply = input("would you like to buy a stamp, buy a envelop, or a copy? (enter stamp, envelop, copy) ")
if userReply == "stamp":
    print("we have collection of stamp")
elif userReply == "envelop":
    print("we have different types of envelop")
elif userReply == "copy":
    copies = input("how many copies would you like? (enter a number) ")
    print("here is {} copy.".format(copies))
else :
    print("thank you shop agian")
    
