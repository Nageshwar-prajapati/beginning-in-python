rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

A=[]
print("Enter the elements of first matrix: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

rsum=[]
for i in range(rows):
    sum=0
    for j in range(cols):
        sum+=A[i][j]
    
    rsum.append(sum)

for i in range(rows):
    print(f"Row {i+1} sum: {rsum[i]}")
