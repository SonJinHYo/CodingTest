import numpy as np

def checkMM(brr,M):
    for i in range(M,2*M):
        for j in range(M,2*M):
            if brr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    M = len(lock)
                
    brr = [[0]*(3*M) for _ in range(3*M)]
    
    for i in range(M):
        for j in range(M):
            brr[i+M][j+M] = lock[i][j]
            
    for i in range(1,2*M):
        for j in range(1,2*M):
                    
            for k in range(4):
                arr = (np.rot90(np.array(key),k)).tolist()
                for row in range(m):
                    for col in range(m):
                        brr[row+i][col+j] += arr[row][col]
                        
                if checkMM(brr,M):
                    return True
                    
                for row in range(m):
                    for col in range(m):
                        brr[row+i][col+j] -= arr[row][col]
    
    return False
        
