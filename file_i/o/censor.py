words = ["donkey" , "bad" , "ganda" , "die"]

with open("para.txt" , "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, f"*"*len(word))

with open("para.txt" , "w") as f:
    f.write(content)

