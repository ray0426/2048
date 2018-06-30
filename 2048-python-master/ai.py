def input_Layer(mat):
    X = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            X.append(mat[i][j])
    return (X,len(mat)*len(mat))
