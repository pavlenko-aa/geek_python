class Matrix:
    def __init__(self, mat: list):
        self.mat = mat

    def __str__(self):
        result = ""
        for el_mat in self.mat:
            result += " ".join(map(str, el_mat))
            result += "\n"
        return result

    def __add__(self, other):
        result = []
        for i in range(len(self.mat)):
            line = []
            for j in range(len(self.mat[i])):
                line.append(self.mat[i][j] + other.mat[i][j])
                if len(line) == len(self.mat):
                    result.append(line)
                    line = []
        return Matrix(result)


my_mat = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
my_mat2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Матрица 1:\n{my_mat}")
print(f"Матрица 2:\n{my_mat2}")
print(f"Суммированная матрица:\n{my_mat + my_mat2}")

