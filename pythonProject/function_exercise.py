def name_print(user_input):
    return user_input + 'Ram'


name = input("Please enter name")
print(name_print(name))

l=int(input("Enter length"))
w=int(input("enter width"))
h=int(input("enter height"))

def calc_prism_vol(len,wid,hgt):return len*wid*hgt

print("volume of prism is"+ str(calc_prism_vol(l,w,h)))