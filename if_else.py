
# # a = int(input("enter your no:"))
# # b= int(input("enter your no"))
# # c= int(input("enter your no"))
# # d= int(input("enter your no"))

# # if(a>b and a>c and a>d):
# #     print(a)

# # elif(b>a and b>c and b>d):
# #     print(b)

# # elif(c>a and c>b and c>d):
# #     print(c)

# # else:
# #     print(d)

# # a = input("Enter your username:")
# # b = len(a)
# # if(len(a)<10):
# #     print("username is less than 10")


# # list = ["Harry" , "Garry" , "Larry" , "Parry"]

# # a = input("inter your name:")

# # if(a in list):
# #     print("your name is in the list")


# # marks = int(input("Enter your marks:"))

# # if(marks<50):
# #     print("your got C grade")

# # elif(50<=marks<70):
# #      print("B")
# # elif(70<=marks<90):
# #     print("A")
# # elif(90<=marks<100):
# #     print("EX")

# # print(" ")

# # no = int(input("Enter your number:"))


# # for i in range(10):
# #     print(i*no)


# # l = ["Harry", "Soham", "Sachin", "Rahul"]

# # for name in l:
# #     if(name.startswith("S")):
# #         print(f"Hello {name}")

# n = int(input("Enter your no:"))
# # # i=1
# # # while(i<11):3
# # #     print(f"{no} X {i} {i*no}")
# # #     i += 1
    
# # for i in range(2 , n):
# #     if((n%i) == 0):
# #         print("no is not prime:")
# #         break

# # for i in range(1 ,n+1):
# #     # print(" "*(n-i), end="")
# #     print("*"*(2*i-1), end="")
# #     print("")
    
    
# # print("nigam", end="")
# # print("aditya", end="")

# for i in range(1 ,n+1):
#     # print(" "*(n-i), end="")
#     if(i%2 == 0):
#         print("* *",)
      
#     else:
#          print("*"*(3*i), end="")
         

# n = int(input("enter your no:"))

# for i in range(2, n):
#     if(n%i==0):
#         print("A")
#         break
     
# i=1
# product = 1
# while(i<n+1):
#     product = product*i
#     i = i + 1

# print(product)

# for i in range(n):
    
#     print("*"*(i))



# def greeting(name="NIL" , ending="Thank you"):
#     print("Hello " + name)
#     return "done"

# a = greeting("Harry")
# b = greeting("Aditya")


# # print(a)
# # print(b)
# def calc(n , ch):
#     sum = 0
#     for i in range(1,n+1):
#         if(i%2 == 0 and ch==1 )or(i%2 !=0 and ch ==2)or ( ch == 0):
#             sum = sum + i
#             print(i , end="+")
#     print("= ", sum)


# n = int(input("Enter your no:"))
# print(" press 0 if you want all sum \n press 1 if you want even sum \n press 2 if you want odd sum ")

# choice = int(input("enter your no:"))
# if(choice == 0):
#     sum = 0
#     for i in range(n+1):
#         if 1==1:
#         sum = sum + i
#         print(sum)
#     print("your answer is: ", sum)

# else:
# calc(n,choice)
# elif(choice ==1):
#     sum = 0
#     for i in range(n+1):
#         if(i%2 == 0):
#             sum = sum + i
#             print(i , end="+")
#     print("= ", sum)

# elif(choice==2):
#     sum = 0
#     for i in range(n+1):
#         if(i%2 != 0):
#             sum = sum + i
#             print(sum)
#     print("your answer is: ", sum)
        
    
def sum(n):
    if(n<=1):
        return 1

    return sum(n-1) + n     



print(sum(5))


def pattern(n):
    if(n<=1):
        return 1
    
    print("*" * n)
    pattern(n-1)
    
print(pattern(10))


def in_to_cm(c):
    i = 2.5*c
    return i



answer = in_to_cm(5)
print(answer)


def table(n):
    for i in range(1,11):
        print(f"")





st = "Aditya is a good boy"


f = open("newfile.txt" , "w")


print(f.write("How are you?"))