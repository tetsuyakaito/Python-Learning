# #make a program which first capital and small for given things writing
# #how many words of particual counting and repeating
# #

# # with open("poem.txt" , "r") as f:
# #     content = f.read()
# #     print(content)


# def game():
#     import random
#     print("welcome to game")
#     score = random.randint(1,60)
#     f =  open("Hiscore.txt" , "r+")
#     hiscore = f.read()
#     # print(hiscore)
#     # print(score)

#     if(score >= int(hiscore)):
#         # with open("Highscore.txt" , "w") as f:
#         f.seek(0)
#         f.write(str(score))
#         print(score)



# game()

'''tables'''

# def table(n):
#     f = open(f"tables/table_{n}" , "w")
#     for i in range(1,11):
#         table = f"{n} X {i} = { n*i}"
    
       
#         # with open(f"tables/table_{i}" , "a") as f:
#         f.write(table)
#         f.write("\n")
        

        
# for n in range(2,21):
#     table(n)

    
with open("para.txt", "r") as f:
    content = f.read()

with open("para_copy.txt", "r") as f:
    content_ =f.read()

if(content == content_):
    print("identical")

# if(content.find("python")):
#     print("This file contain python")



    

