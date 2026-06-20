rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

A=[]
print("Enter the elements of first matrix: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

Csum=[]
for i in range(cols):
    sum=0
    for j in range(rows):
        sum+=A[j][i]
    
    Csum.append(sum)

for i in range(cols):
    print(f"column {i+1} sum: {Csum[i]}")
