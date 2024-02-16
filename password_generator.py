import string
import random
 #storing the characters
a= list(string.ascii_lowercase)
b= list(string.ascii_uppercase)
c = list(string.digits)
d = list(string.punctuation)

#get the length of [assword from user
m = input("Enter the length of the password:")

#check the user input is number or not
while True:
    try:
        input_num = int(m)
        if input_num < -1:
            print("please enter the positive number")
            m = input("Enter the length of password:")
        else:
            break
    except:
        print("Enter the number only")
        m = input("Enter the length of password:")
        

#shuffle all character
random.shuffle(a)
random.shuffle(b)
random.shuffle(c)
random.shuffle(d)

#calculate 30% 20% of number of characters
a1 = round(input_num *(30/100))
a2= round(input_num * (20/100))
#generate the password
result =[]
for x in range(a1):
    result.append(a[x])
    result.append(b[x])

for x in range(a2):
    result.append(c[x])
    result.append(d[x])
#shuffle result
random.shuffle(result)

#display result
password = "".join(result)
print("Your Password: ",password)
    
    
              
