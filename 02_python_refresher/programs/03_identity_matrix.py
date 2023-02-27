# Write a function to create an identity matrix
#  1 0 0
#  0 1 0
#  0 0 1

def get_identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        print(row)
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    matrix_size = int(input("Enter the size of the matrix: "))
    get_identity_matrix(matrix_size)


            