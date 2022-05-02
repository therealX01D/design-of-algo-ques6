import math
ct=0
def printc(str):
    global ct
    ct+=1
    print(str)
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        printc(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
    else:    
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        printc(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
def TowerOfHanoi4(n , p, q, r,s):
    if n == 0 :
        return 
    elif n==1:
        printc(f"Move disk 1 from rod {p} to rod {q}")
        return 
    else:    
        TowerOfHanoi4(n-2, p , r , s ,q )
        printc(f"Move disk {n-1} from rod {p} to rod {s}" )
        printc(f"Move disk {n} from rod {p} to rod {q}")
        printc(f"Move disk {n-1} from rod {s} to rod {q}")
        TowerOfHanoi4(n-2,  r , q , p ,s)
def TowerOfHanoi4Algo1( i,  j,  a,  b,  c,  d) :
    m = j - i + 1
    k = math.floor(m / 2);                                                              
    TowerOfHanoi4(m - k, a, d, b, c)
    TowerOfHanoi(k, a, b, c)
    TowerOfHanoi4(m - k, d, b, a, c)
def TowerOfHanoi4Algo2( i,  j,  a,  b,  c,  d, k):
    m = j - i + 1
    if (m <= k):
        TowerOfHanoi(m, a, b, c)
    else:
        TowerOfHanoi4(m - k, a, d, b, c)
        TowerOfHanoi(k, a, b, c)
        TowerOfHanoi4(m - k, d, b, a, c)
def TowerOfHanoi4Algo3( i,  j,  a,  b,  c,  d):
    m = j - i + 1
    k = math.floor(math.sqrt(2 * m))
    TowerOfHanoi4(m - k, a, d, b, c)
    TowerOfHanoi(k, a, b, c)
    TowerOfHanoi4(m - k, d, b, a, c)
if __name__ == '__main__':
    n = 8
    Dm = [None  for _ in range(n + 1)]
    Dm3= [None  for _ in range(n + 1)]
    #TowerOfHanoi(n, 'A', 'C', 'B')
    print("-----------------------------------------------------") 
    ct=0 
    TowerOfHanoi4(8, 'A', 'D','B', 'C') 
    print("number of steps is",ct)
    print("-----------------------------------------------------")
    ct=0   
    TowerOfHanoi4Algo1(1,n,'A','D','B','C')
    print("number of steps is",ct)
    print("-----------------------------------------------------")
    ct=0 
    #ToH42(1,n,'A','B','C','D',4)
    TowerOfHanoi4Algo2(1,n,'A','D','B','C',4)
    print("number of steps is",ct)
    print("-----------------------------------------------------") 
    ct=0
    TowerOfHanoi4Algo3(1,n,'A','D','B','C')
    print("number of steps is",ct)
    # define DP array
    
    # Call for kProfit to calculate max profit