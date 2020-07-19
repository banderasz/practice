from random import randint
import pandas as pd

def create_cost_matrix(N, k, maxval, name):
    matrix = list()
    for row in range(N):
        matrix.append(list())
        for column in range(k):
            matrix[row].append(randint(0, maxval))

    df = pd.DataFrame(matrix)
    writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, header=False)
    writer.save()

def read_matrix(path):
    return pd.read_excel(path, header=None)