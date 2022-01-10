#question1
print("Q U E S T I O N  1")
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
avg=(num1+num2+num3)/3
print("the average of the given numbersis:" , avg)

#question2
print("Q U E S T I O N  2")
gross_income=float(input("enter gross income:"))
#given standard deductions is 10000
standard_ddc=10000
dependents=int(input("enter the number of dependents:"))
#deduction for each dependent is 3000
dependent_ddc=3000
#tax rate is 20%
txr=20/100
taxable_income=gross_income-standard_ddc-(dependent_ddc*dependents)
tax=taxable_income*txr
print("tax:",tax)

#question3
print("Q U E S T I O N  3")
a=int(input("enter the SID:"))
name=str(input("enter name:"))
gnd=str(input("enter gender F for female, M for male, U for unknown:"))
d=str(input("enter course name:"))
cgp=float(input("enter CGPA:"))
print("SID  NAME GENDER COURSENAME CGPA")
print(a,name,gnd,d,cgp)

#question 4
print("Q U E S T I O N  4")
mark1=int(input("enter marks of student 1:"))
mark2=int(input("enter marks of student 2:"))
mark3=int(input("enter marks of student 3:"))
my_list=[mark1 , mark2 , mark3]
print("list:")
print(my_list)
print("sorted list in decreasing order:")
my_list.sort(reverse=True)
print(my_list)

#question5
print("Q U E S T I O N  5")
my_list=['red','green','white','black','pink','yellow']
print("given list:",my_list)
#part a
print("part a")

#removing the fourth element which is 'black'

my_list.remove('black')
print("new list after removing the fourth element:")
print(my_list)

#part b
print("part b")

#to replace the nth term we write {my_list[n-1]='new value'}

my_list[3]='purple'
my_list[4]='purple'
print("new list after replacing black and pink with purple:")
print(my_list)