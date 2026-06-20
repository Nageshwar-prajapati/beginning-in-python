rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

A=[]
print("Enter the elements of matrix: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

B=[]
for i in range(cols):
    row=[]
    for j in range(rows):
        row.append(A[j][i])
    B.append(row)

print("Matrix: ",A)
print("Transpose of Matrix: ",B)