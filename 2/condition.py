# first_name="Ekramul"

# size=len(first_name)

# if size==0:
#     print("This field can not be empty")
# else:
#     print("Success")


name=input("Enter Your Name:")
email=input("Enter Your Email:")

name_size=len(name)
email_size=len(email)

if name_size==0 or email_size==0:
    print("This Field can not be empty")
else:
    print("Success")
