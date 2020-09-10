def add_matrices():
	m1_size = list(map(int, input("Enter the size of first matrix: ").split()))
	print("Enter first matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	m2_size = list(map(int, input("Enter the size of second matrix: ").split()))
	print("Enter second matrix:")
	m2 = [list(map(float, input().split())) for x in range(m2_size[0])]

	if m1_size == m2_size:
		result = [[m1[r][c] + m2[r][c] for c in range(m1_size[1])] for r in range(m1_size[0])]

		print("The result is:")
		print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))
	else: print("The operation cannot be performed.")


def multiply_matrix_by_const():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(int, input().split())) for x in range(m1_size[0])]
	const  = int(input("Enter constant: "))

	result = [[m1[r][c] * const for c in range(m1_size[1])] for r in range(m1_size[0])]

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))


def multiply_matrices():
	m1_size = list(map(int, input("Enter the size of first matrix: ").split()))
	print("Enter first matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	m2_size = list(map(int, input("Enter the size of second matrix: ").split()))
	print("Enter second matrix:")
	m2 = [list(map(float, input().split())) for x in range(m2_size[0])]

	if m1_size[1] == m2_size[0]:
		result = [[sum(m1[i][ii] * m2[ii][j] for ii in range(m1_size[1])) for j in range(m2_size[1])] for i in range(m1_size[0])]

		print("The result is:")
		print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))
	else: print("The operation cannot be performed.")


def main_diagonal():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	result = [[m1[c][r] for c in range(m1_size[0])] for r in range(m1_size[1])]

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))


def side_diagonal():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	result = [[m1[-c - 1][-r - 1] for c in range(m1_size[0])] for r in range(m1_size[1])]

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))


def vertical_line():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	result = [[m1[r][-c - 1] for c in range(m1_size[1])] for r in range(m1_size[0])]

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))	


def horizontal_line():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	result = [[m1[-r - 1][c] for c in range(m1_size[1])] for r in range(m1_size[0])]

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))


def transpose_matrix():
	print("1. Main diagonaln\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
	option = input("Your choice: ")
	if option == "1":
		main_diagonal()
	if option == "2":
		side_diagonal()
	if option == "3":
		vertical_line()
	if option == "4":
		horizontal_line()


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 1:
    	return m[0][0]
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


def calculate_determinant():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	if m1_size[0] != m1_size[1]:
		print("The operation cannot be performed.")
	else:
		result = getMatrixDeternminant(m1)

	print("The result is:")
	print(result)
	print()


def transposeMatrix(m):
    return map(list,zip(*m))


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if determinant == 0:
    	return "This matrix doesn't have an inverse."
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def inverse_matrix():
	m1_size = list(map(int, input("Enter the size of matrix: ").split()))
	print("Enter matrix:")
	m1 = [list(map(float, input().split())) for x in range(m1_size[0])]

	result = getMatrixInverse(m1)

	print("The result is:")
	print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in result]))


while True:
	print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
	choice = input("Your choice: ")
	if choice == "1":
		add_matrices()
	if choice == "2":
		multiply_matrix_by_const()
	if choice == "3":
		multiply_matrices()
	if choice == "4":
		transpose_matrix()
	if choice == "5":
		calculate_determinant()
	if choice =="6":
		inverse_matrix()
	if choice == "0":
		break