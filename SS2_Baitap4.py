#A)
for i in ["*"]:
     print (i * 20)

#B)
n = int (input ('Nhập n: '))
for i in ["*"]:
     print (i*n)

#C)
n = int (input ("Nhập n: "))
for i in range (n):
     if i % 2 != 0:
         print ("*", end = " ")
     elif i % 2 ==0:
         print ("x", end = " ")

#D)
print ("\n")
n = int (input ('Nhập n: '))
m = int (input ('Nhập m: '))

for i in range (m):
    print ()
    for i in range (n):
         print ("*", end = " ")
      

