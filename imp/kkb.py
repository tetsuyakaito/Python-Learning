

n = int(input("Enter your no:"))
print(" press 0 if you want all sum \n press 1 if you want even sum \n press 2 if you want odd sum ")

choice = int(input("enter your no:"))

#M
# if(choice == 0):
#     sum = 0
#     for i in range(n+1):
#         if 1==1:
#         sum = sum + i
#         print(sum)
#     print("your answer is: ", sum)

# else:

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
        
def calc(n , ch):
    sum = 0
    for i in range(1,n+1):
        if(i%2 == 0 and ch==1 )or(i%2 !=0 and ch ==2)or ( ch == 0):
            sum = sum + i
            print(i , end="+")
    print("= ", sum)

calc(n,choice)
    
    
