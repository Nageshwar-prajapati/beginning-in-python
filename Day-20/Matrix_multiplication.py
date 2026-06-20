rows1=int(input("Enter the rows of first matrix: "))
cols1=int(input("Enter the columns of first matrix: "))

rows2=int(input("Enter the rows of second matrix: "))
cols2=int(input("Enter the columns of second matrix: "))

if(cols1!=rows2):
    print("Operation Incompatible.")
    exit()


A=[]
print("Enter the elements of first matrix: ")
for i in range(rows1):
    row=[]
    for j in range(cols1):
        row.append(int(input()))
    A.append(row)

B=[]
print("Enter the elements of second matrix: ")
for i in range(rows2):
    row=[]
    for j in range(cols2):
        row.append(int(input()))
    B.append(row)

print("First Matrix: ",A)
print("Second Matrix: ",B)

C=[]
for i in range(rows1):
    row=[]
    for j in range(cols2):
        sum=0
        for k in range(cols1):
            sum+=A[i][k]*B[k][j]
        row.append(sum)
    C.append(row)

print("Multiplication of matrix: ",C)
