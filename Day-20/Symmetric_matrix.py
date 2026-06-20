n=int(input("Enter the order of matrix: "))

A=[]
print("Enter the elements of matrix: ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)

found=0
for i in range(n):
    for j in range(n):
        if(A[i][j]!=A[j][i]):
            found=1
            break

if(found):
    print("Unsymmetric matrix.")
    
else:
    print("Symmetric matrix.")