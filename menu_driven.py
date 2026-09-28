def file_read():
    filename=input("enter filename")
    f=open(filename,"r")
    s=f.read()
    print(s)
    f.close()
print("menudriven.file operations")
print("1.file read")
print("2.file write")
print("3.file append")
print("4.file search")
print("5.file delete")
print("6.exit")
ch=int(input("enter the choice"))
if ch==1:
    file_read()
    pass
elif ch==2:
    pass
elif ch==3:
    pass
elif ch==4:
    pass
elif ch==5:
    pass
else:
    exit()