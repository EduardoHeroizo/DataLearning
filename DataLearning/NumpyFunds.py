# Conhecimentos numpy 01
import numpy as np 

# Cria um array em ordem de 20 a 10. 
def criaArrayOrdem():
    arr = np.linspace(10,20,11)
    return arr

# Cria uma matriz 3x3 em ordem. 
def criaMatriz3x3():
    arr = np.linspace(1,9,9)
    arr = arr.reshape(3,3)
    return arr

# Cria uma matriz de zeros 2x4. 
def criaMatrizeros():
    arr = np.zeros((2,4))
    return arr

# Indexação e Slicing Matriz. 
def indexsliceMatriz():

    arr = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

    res = []
    
    # Pega a segunda linha inteira.
    res.append(arr[1,:])
    # Pega a primeira coluna inteira. 
    res.append(arr[:,0])
    # Subarray contendo elementos [20,30,50,60].
    res.append(arr[0:2, 1:3])
    # Inverte as linhas.
    res.append(arr[::-1,:])
    # Inverte as colunas.
    res.append(arr[:,::-1])
    
    return res

# Utilza Flatten ou Ravel (Transforma multidimensional em 1D).
def transforma1d():
      arr = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
      
      arrnovo = arr.flatten()

      return arrnovo

# Utiliza conhecimentos de elementWise(Operações para elementos individualmente) e Broadcasting(Operação matriz shape distinto).
def elementWise_Broadcasting():
    
    X = np.array([[1, 2, 3],
              [4, 5, 6]])
    Y = np.array([10, 20, 30])  

    res = []

# Teste por risco de erro, mas nesse caso de shape (2x3, 1x3) é um caso ideal para Broadcast.
    try: 
       C = X + Y 
    except ValueError: 
        print("Não são compatíveis para Broadcasting")
    
    Produto2 = X * 2 
    Maiores3 = X > 3 
    Maiores3 = Maiores3.astype(int)
    
    res.append(C)
    res.append(Produto2)
    res.append(Maiores3)

    return res

# Utiliza aplicação de produto matricial (combinando entradas e pesos), linha somada é resultante. 
# Podemos utilizar operador @. 
def produtoMatricial():
    
    res = []
    
    A = np.array([[1, 2],
                [3, 4]])
    
    B = np.array([[5, 6],
                [7, 8]])
    
    res.append(np.dot(A,B))
    
    return res
    
# Asserts - com respostas das funções -> 
# Foi utilizado método .tolist() , pois é a forma de transformar array(Numpy) em lista(Python).
# criaArrayOrdem
assert criaArrayOrdem().tolist() == [10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.]  

# criaMatriz3x3
assert criaMatriz3x3().tolist() == [[1,2,3],[4,5,6],[7,8,9]]  

# criaMatrizeros
assert criaMatrizeros().tolist() == [[0,0,0,0],[0,0,0,0]]  

# indexsliceMatriz
res_index = indexsliceMatriz()
assert res_index[0].tolist() == [40,50,60]  # segunda linha
assert res_index[1].tolist() == [10,40,70]  # primeira coluna
assert res_index[2].tolist() == [[20,30],[50,60]]  # subarray
assert res_index[3].tolist() == [[70,80,90],[40,50,60],[10,20,30]]  # linhas invertidas
assert res_index[4].tolist() == [[30,20,10],[60,50,40],[90,80,70]]  # colunas invertidas

# transforma1d
assert transforma1d().tolist() == [10,20,30,40,50,60,70,80,90]  

# elementWise_Broadcasting
res_elem = elementWise_Broadcasting()
assert res_elem[0].tolist() == [[11,22,33],[14,25,36]]  
assert res_elem[1].tolist() == [[2,4,6],[8,10,12]]  
assert res_elem[2].tolist() == [[0,0,0],[1,1,1]]  

# produtoMatricial
res_prod = produtoMatricial()
assert res_prod[0].tolist() == [[19,22],[43,50]]  
    