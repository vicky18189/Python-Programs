# import re
# data = "I am. a. Disco Dancer, You are a Disco Dancer." ##< > : ; ' , . / ; ' [ ] \ - = < > ? : { } | _ + ! @ # $ % ^ & * ( ) ` ~ "
# PATTERN = re.compile(r'''([^,./;'[\\\]\-=<>?:"{}|_+!@#$%^&*()`~])+''')
# print (PATTERN.split(data))

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    u = i[0].isupper()
    l = i[0].islower()
    if u == True:
        a += i[0].upper() + " "
    elif l == True:
        a += i[0].lower() + i[1:].lower() + " "
print(a)        
