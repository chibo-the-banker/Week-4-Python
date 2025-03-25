#reading and appending line to hello file
file=open("hello.txt","r")
print(file.read())
file=open("hello.txt","a")
file.write("\n \n \n This is the new addition")

file=open("hello.txt","r")
print(file.read())

#creating newHello file
newfile=open("newHello.txt","x")
newfile=open("newHello.txt","w")
newfile.write("This is the new file")
#error shows if file was not created
try:
    newfile= newfile=open("newHello.txt","r")
    print(newfile.read())

except FileNotFoundError:
    print("This file does not exist.")

finally:
    for data in file:
        newfile.write(data)

#newHello appended file opens on command
newfile= newfile=open("newHello.txt","r")
print(newfile.read())

