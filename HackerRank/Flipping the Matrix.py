matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

quadrante = int(len(matrix)/2)

# print(len(matrix))
# print(matrix[0])
# matrix[0].reverse()
# print(matrix[0])

pos = list()


for num in matrix:
    for ind, x in enumerate(num):
        print(f'{matrix.index(num)} | {ind}  = {x}')