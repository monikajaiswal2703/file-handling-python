mon_file= open("write and read4.txt","w")
mon_file.write("my name is monika jaiswal")
mon_file.close()

r_file=open("write and read4.txt","r")
b=r_file.read(10)
print(b)
r_file.close()