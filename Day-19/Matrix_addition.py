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

print("First array: ",A)
print("Second array: ",B)

C=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
    C.append(row)

print("Sum of matrix: ",C)