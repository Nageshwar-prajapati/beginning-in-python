n=int(input("Enter the order of matrix: "))

A=[]
print("Enter the elements of matrix: ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)

lsum,rsum,diag=0,0,0
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            diag+=A[i][j]

        if(i==j):
            lsum+=A[i][j]

        if(i+j==n-1):
            rsum+=A[i][j]

print("Matrix: ",A)
print("Left diagonal sum: ",lsum)
print("Right diagonal sum: ",rsum)
print("Diagonal sum: ",diag)