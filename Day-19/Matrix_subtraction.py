rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

A=[]
print("Enter the elements of first matrix: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

B=[]
print("Enter the elements of second matrix: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

print("First Matrix: ",A)
print("Second Matrix: ",B)

ch=int(input("Enter 1 for (A-B)\nEnter 2 for (B-A):"))

C=[]
if (ch==1):
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(A[i][j]-B[i][j])
        C.append(row)
    print("Difference of matrix: ",C)

elif (ch==2):
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(B[i][j]-A[i][j])
        C.append(row)
    print("Difference of matrix: ",C)

else:
    print("INVALID INPUT")


