

matrix=[]


def print_matrix(matrix,n):
    print()
    for l in range(n):
        for k in range(n):
            if matrix[l][k]== -0.0:
                print(0,end="|")
            else:
                print(matrix[l][k],end="|")
        print()
        
    print()
def find_deter(matrix):
    
    deter=float(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
    return deter


def find_determinant(deter_list,matrix):
    determinant = float(matrix[0][0]*deter_list[0] + matrix[0][1]*deter_list[1] + matrix[0][2]*deter_list[2])
    return determinant
    
def cofactor_matrix(matrix):
    cofactor=[]
    var=1
    chk=True
    for s in range(3):
        empty=[]
        for g in range(3):
            
            first = [sublist[:] for sublist in matrix]
                
            del first[s]
            for sublist in first:
                sublist.pop(g)
        
            empty.append(var*find_deter(first))
            var=var*-1
        if chk:
            determinant = find_determinant(empty,matrix)
            chk = False
            
        cofactor.append(empty)

        
    return cofactor,determinant
     
def transpose_matrix(matrix,n):
    transpose=[sublist[:] for sublist in matrix]
    for i in range(n):
        for j in range(n):
            transpose[i][j]=int(matrix[j][i])
            
        
    return transpose

def find_inverse(adjoint,deter):
    inverse=[]
    for element in adjoint:
        a=[]
        a=[float(x/deter) for x in element]
        
        inverse.append(a)
        
    return inverse


def main(matrix):
    print("The given program can calculate the cofactor , adjoint and inverse matrix of a given matrix\n")
    print("Please enter the elements of matrix \n")
    
    while True:
        chk=False
        print()
        for i in range(3):
            a=[]
            j=0
            while j<3:
                  
                  try:
                      element = float(input(f"enter element in row {i+1} and column {j+1}: "))
                  except:
                      print("\nPlease enter an number \n ")
                      continue
                  a.append(float(element))
                  j=j+1              
            matrix.append(a)
        print("\nThe given matrix is: ")        
        print_matrix(matrix,3)        
        cofactor,determinant=cofactor_matrix(matrix)
        
        adjoint=transpose_matrix(cofactor,3)
        
        print("The cofactor matrix of the given matrix is: ")
        print_matrix(cofactor,3)

        print("The adjoint matrix of the given matrix is: ")
        print_matrix(adjoint,3)
        print(f"The determinant of the given matrix is {determinant} \n")
        if determinant==0:
            print("determinant is zero, unable to find inverse \n")
        else:
            print("The inverse matrix of the given matrix is: ")
            print_matrix(find_inverse(adjoint,determinant),3)
        out=input("Do you wish to continue(y/n): ").lower()
        if out=="n":
            exit()
    

main(matrix)
