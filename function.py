def greeting_user(fname,lname):
    print(f"Hi {fname} {lname} !")
    print("How are you?")

 
print("start")
greeting_user("Lois")
# we can add positional argument, this means position of the argument can shifted around
# greeting_user(lname= "tracy", fname="Andrew")
print("end")