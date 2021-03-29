
# create a 3x2 matrix
rows =3
columns= 2
mylist = [[0 for x in range(columns)] for x in range(rows)]


for i in range(rows):
     for j in range(columns):
         mylist[i][j] = f'{i},{j}'
         
print( mylist)


