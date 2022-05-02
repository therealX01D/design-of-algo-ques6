import math
def TowerOfHanoi(n , from_rod, to_rod, aux_rod,din): # trivial 3 pegs dynamic programming solution to be used in algo 1 ,algo2 ,algo3
    if n == 1:
        return 1
    elif din[n] is not None:
        #print("Move disk 1 from rod ", from_rod , " to rod " , to_rod )
        return din[n]
    else:    
        din[n]= TowerOfHanoi(n-1, from_rod, aux_rod, to_rod,din)+1+TowerOfHanoi(n-1, aux_rod, to_rod, from_rod,din)
        return din[n]
def TowerOfHanoi4(n , p, q, r,s,Din):
    if n == 0 :
        return 0
    elif n==1:
        return 1
    elif Din[n] is not None:
        #print("Move disk 1 from rod ", from_rod , " to rod " , to_rod )
        return Din[n]
    else:    
        Din[n]=TowerOfHanoi4(n-2, p , r , s ,q ,Din)+3+TowerOfHanoi4(n-2,  r , q , p ,s,Din)
        return Din[n]
def TowerOfHanoi4Algo1( i,  j,  a,  b,  c,  d,Din,D3) :
    m = j - i + 1
    k = math.floor(m / 2);                                                              
    return TowerOfHanoi4(m - k, a, d, b, c,Din)+TowerOfHanoi(k, a, b, c,D3)+TowerOfHanoi4(m - k, d, b, a, c,Din)
def TowerOfHanoi4Algo2( i,  j,  a,  b,  c,  d, k,Din,D3):
    m = j - i + 1
    if (m <= k):
        return TowerOfHanoi(m, a, b, c,D3)
    else:
        Din[0]=0
        Din[1]=1
        return TowerOfHanoi4(m - k, a, d, b, c,Din)+TowerOfHanoi(k, a, b, c,D3)+TowerOfHanoi4(m - k, d, b, a, c,Din)
def TowerOfHanoi4Algo3( i,  j,  a,  b,  c,  d,Din,D3):
    m = j - i + 1
    k = math.floor(math.sqrt(2 * m))
    return TowerOfHanoi4(m - k, a, d, b, c,Din)+TowerOfHanoi(k, a, b, c,D3)+TowerOfHanoi4(m - k, d, b, a, c,Din)
if __name__ == '__main__':
    n = 8
    Dm = [None  for _ in range(n + 1)]
    Dm3= [None  for _ in range(n + 1)]
    #TowerOfHanoi(n, 'A', 'C', 'B')
    print("-----------------------------------------------------")   
    print("number of steps is",TowerOfHanoi4(8, 'A', 'D','B', 'C',Dm))
    Dm = [None  for _ in range(n + 1)]
    Dm3= [None  for _ in range(n + 1)]
    print("-----------------------------------------------------")   
    print("number of steps is",TowerOfHanoi4Algo1(1,n,'A','B','C','D',Dm,Dm3))
    Dm = [None  for _ in range(n + 1)]
    Dm3= [None  for _ in range(n + 1)]
    print("-----------------------------------------------------")
    ct=0 
    #ToH42(1,n,'A','B','C','D',4)
    print("number of steps is",TowerOfHanoi4Algo2(1,n,'A','B','C','D',4,Dm,Dm3))
    Dm = [None  for _ in range(n + 1)]
    Dm3= [None  for _ in range(n + 1)]
    print("-----------------------------------------------------") 
    ct=0
    print("number of steps is",TowerOfHanoi4Algo3(1,n,'A','B','C','D',Dm,Dm3))
 