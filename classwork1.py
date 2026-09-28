#write a program to read a text file and displays the number of lines in a file
# f=open("k.txt","w")
# f.writelines(["hello\n","world\n"])
# f.close()
# f=open("k.txt","r")
# s=f.readlines()
# print(len(s))
# f.close()

#write a program to display the number of words in a file
# f=open("k.txt","w")
# f.write("hello\n"),
# f.write ("world\n")
# f.close()
# f=open("k.txt","r")
# s=f.read()
# print(len(s.split()))
# f.close()

#write a program to update the second line in a file
# f=open("k.txt","r")
# s=f.readlines()
# s[1]="python\n"
# print(s)
# f.close()
# f=open("k.txt","w")
# f.writelines(s)
# f.close()

#write a program t display last 5 lines in a file
# f=open("k.txt","r")
# s=f.readlines()
# print(s[-5:])
# f.close()

#write a program to search a particular word in a file
# f=open("k.txt","r")
# s=f.read()
# word=input()
# if word in s:
#     print("yes")
# else:
#     print("no")
#

#write a program to find number of letters,digits,and spaces in a file
# digit_cnt=0
# letter_cnt=0
# space_cnt=0
# f=open("k.txt","r")
# s=f.read()
# for i in s:
#     if i.isalpha():
#         letter_cnt+=1
#     elif i.isdigit():
#         digit_cnt+=1
#     elif i.isspace():
#         space_cnt+=1
# print("Letters:", letter_cnt)
# print("Digits:", digit_cnt)
# print("Spaces:", space_cnt)

#reverse the lines in a file
# f = open("k.txt", "r")
# s = f.readlines()
# x=s[::-1]
# print(x)
# f.close()
# f=open("k.txt","w")
# f.writelines(x)
# f.close()

#a file total_students.txt contains the names of all students in a class and a file passed_students.txt contains name sof students passed the exam
#write a python program to read the names from both files
# f1=open("total_students","r")
# f2=open("passed_students.txt","r")
# total=f1.readlines()
# passed=f2.readlines()
# print("total students:",total)
# print("passed students:",passed)
# #find the students who did not passed
# print("students who did not passed:")
# for i in total:
#     if i not in passed:
#         print(i,end="")
#write their names to a neq file named failed_students.txt one name per line
# f3=open("failed_students.txt","w")
# for i in total:
#     if i not in passed:
#         f3.write(i)
# f1.close()
# f2.close()
# f=open("k.txt","a+")
# f.write("python")
# s=f.read()
# print(s)
#seek and tell
# f=open("k.txt","a+")
# print("first position",f.tell())
# f.write("python")
# print("second position",f.tell())
# f.seek(0)
# print("third position",f.tell())
# f.read()
import os
os.remove("k.txt")
 











