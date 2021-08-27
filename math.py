f = open("MyFile.txt", "w")

f.write("Hello")
f.write(" ")
f.close()

f = open("MyFile.txt", "a")
f.write("World")
f.close()

f= open("MyFile.txt", "r")
line = f.readline()
print(line)

with open("MyFile.txt", "r") as f :
    line2 = f.readline()
    print(line2)