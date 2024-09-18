print("Hello World")
# comments
'''
abcd 
efgh
comments only
'''

print('''
      And I'd give up forever to touch you
'Cause I know that you feel me somehow
You're the closest to heaven that I'll ever be
And I don't wanna go home right now
And all I can taste is this moment
And all I can breathe is your life
And sooner or later, it's over
I just don't wanna miss you tonight
      ''')

import os
print(os.listdir())



a = '''rakshita'''
b = 234
c = True
d = 34.45
e = None

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#typecasting
a = "23"
a = int(a)
print(a + 5)

#input function -- prints as string

a = input('enter something')
print(a)


b = input('enter something b:')
b = int(b)
print(type(b)) 


c = input("enter first")
d = input("enter second")
c = int(c)
d = int(d)
print((c+d)/2)

a = input("enter no for square: ")
a = int(a)
print(a*a)


#STRING
a = "helloo"
b = "bye"
print(a + b)
print(a[3])
print(a[0:3]) # --> only 0,1,2 -- 3 index is excluded = slicing string
print(a[0:4:2]) # --> skip slicing
c = "abcdefghijk"
print(c[0::3])

statement = "and I'd give up forever to touch you, Cause I know that you feel me somehow"
# print(len(statement))
# print(statement.endswith("nopes")) #tellss kisse end hora hai 
# print(statement.count("o"))
print(statement.capitalize())
print(statement.find("give"))
# print(statement.replace("give", "hello"))


# mydict = {
#     "kitaab" : "book",
#     "gaana" : "song",
#     "pankha" : "fan"
# }
# print("options are", mydict.keys())
# a = input("enter the hindi word\n")
# print("meaning is: ", mydict[a])

# num1 = int(input("ENter num1: "))
# num2 = int(input("ENter num2: "))
# num3 = int(input("ENter num3: "))
# num4 = int(input("ENter num4: "))
# num5 = int(input("ENter num5: "))
# num6 = int(input("ENter num6: "))
# num7 = int(input("ENter num7: "))
# num8 = int(input("ENter num8: "))

# s ={num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)

# s = {8, "8"}
# print(s)

# a = int(input("enter the age: "))

# if(a>=18):
#     print("yes")
# # if(a<18):
# #     print("not greater")
# else:
#     print("lesser")



# color = input("enter color: ")
# noun = input("enter noun: ")
# hero = input("enter hero: ")

# print("roses are " + color)
# print(noun + "are blue")
# print("i love " + hero)




# def cube(num):
#     return num*num*num

# result = int(input("enter num: "))
# print(cube(result))



'''better calculator'''

# num1 = float(input("enter first num: "))
# operator = input("enter operator: ")
# num2 = float(input("enter second num: "))

# if (operator == "+"):
#     print(num1 + num2)
# elif (operator == "-"):
#     print(num1 - num2)
# elif (operator == "*"):
#     print(num1 * num2)
# elif (operator == "/"):
#     print(num1 / num2)
# else:
#     print("Invalid")





'''secret game guess'''

# secret_word = "dog"
# guess = ""
# count = 0
# limit = 3
# out_of_guess = False

# while (guess != secret_word and not(out_of_guess)):
#     if (count < limit):
#             guess = input("Enter the word: ")
#             count += 1
#     else:
#           out_of_guess = True


# if out_of_guess:
#       print("out of guesses")
# else:
#       print("Win!")


'''translator'''

# def translator(phrase):
#     translate = ""
#     for vowel in phrase:
#         if vowel in "AEIOUaeiou":
#             translate = translate + "g"
#         else:
#             translate = translate + vowel
#         return translate
    


# print(translator(input("enter the phrase: ")))



'''tryandexcept'''


try:
    value = 10/0
    number = int(input("enter a num: "))
    print(number)
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("invalid")