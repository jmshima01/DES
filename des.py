from sys import argv
def printBin(s):
    c = 0
    print("0b ",end="")
    for i in s:
        if c==4:
            c=0
            print(" ",end="")
        c+=1
        print(i,end="")
    print()


if __name__ == "__main__":
    if len(argv) < 3:
        print("err")
        exit(-1)
    
    key = bin(int(argv[2],16))[2:].zfill(64)
    block = bin(int(argv[1],16))[2:].zfill(64) # assuming 0x0123456789ABCDEF
    print("key: ",end="")
    printBin(key)
    print("plaintext: ",end="")
    printBin(block)

    # +++++++++++++++ GEN BLOCK (b) +++++++++++++++
    IP = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
        ]
    
    for i in range(len(IP)):
        for j in range(len(IP[0])):
            IP[i][j] -= 1
    
    sub = []
    for i in IP:
        for j in i:
            sub.append(j)


    ip_str = [0]*64
    c = 0
    for i in sub:
        ip_str[c] = str(block[i])
        c+=1
    ip_str = ''.join(ip_str)
    print("0b"+ip_str)

    L_0 = ip_str[:32]
    R_0 = ip_str[32:]
    print()
    print(f"L_0={L_0}")
    print(f"R_0={R_0}") 
    PL_0 = "0b"+L_0
    PR_0 = "0b"+R_0
    print(f"L_0={hex(int(PL_0,2))}")
    print(f"R_0={hex(int(PR_0,2))}")  

    if "0101101000000000010110100000000000111100111100000011110000001111" == ip_str:
        print("yay")
    
    # ++++++++++++++ GEN K1 (a) ++++++++++++++
    PC1 = [
        [57, 49, 41, 33, 25, 17, 9],
        [1, 58, 50, 42, 34, 26, 18],
        [10, 2, 59, 51, 43, 35, 27],
        [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15],
        [7, 62, 54, 46, 38, 30, 22],
        [14, 6, 61, 53, 45, 37, 29],
        [21, 13, 5, 28, 20, 12, 4]
    ]
    pc1 = []
    for i in range(8):
        for j in range(7):
            pc1.append(PC1[i][j])
    print()
    print("++++++++++++++++++++++++++++++++++++")
    print()
    
    pc1 = [i-1 for i in pc1]
    print(pc1)
    pc1_key = [0]*56
    c = 0
    for i in pc1:
        pc1_key[c] = key[i]
        c+=1
    pc1_key = ''.join(pc1_key)
    printBin(pc1_key)
    print(len(pc1_key))
    C = pc1_key[:28]
    D = pc1_key[28:]
    print(f"C: {C}")
    print(f"D: {D}")

    lcs = lambda b, n: bin(b<<n|b>>(64-n))[2:].zfill(28)
    C = lcs(int(C,2),1)
    D = lcs(int(D,2),1)

    print(C+D)
    r = C+D
    if r == "11010001111110001000100101000010001000100111110100101100":
        print("yay2")
        
    PC2 = [
        [14, 17, 11, 24, 1, 5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]
    ]
    pc2 = []
    for i in PC2:
        for j in i:
            pc2.append(j-1)
    print(pc2)
    print(len(pc2))
    pc2_key = [0]*48
    c=0

    for i in pc2:
        pc2_key[c] = r[i]
        c+=1
    
    pc2_key = ''.join(pc2_key)
    print(pc2_key)

    if pc2_key == "011110000011001111000011001000001101101001110000":
        print("k1 yay")
    
    K1 = pc2_key
    print(hex(int(K1,2)))



    # ====== part c ============
    print("==================")
    print()
    print(len(R_0))

    EXP_Table = "32 1 2 3 4 5 4 5 6 7 8 9 8 9 10 11 12 13 12 13 14 15 16 17 16 17 18 19 20 21 20 21 22 23 24 25 24 25 26 27 28 29 28 29 30 31 32 1".split(" ")
    EXP = list(map(int,EXP_Table))
    EXP = [i-1 for i in EXP]
    print(EXP)

    E_R0 = [0]*48
    for i,v in enumerate(EXP):
        E_R0[i] = R_0[v]
    E_R0 = ''.join(E_R0)
    print(E_R0)

    if "100111111001011110100000000111111000000001011110" == E_R0:
        print("yay3")
    print(hex(int(E_R0,2)))

    # ================ part d ====================
    print()
    print("-------------------------------------")
    print()
    print(E_R0)
    print("^")
    print(K1)
    print(" = ")
    A = int(E_R0,2) ^ int(K1,2)
    A = bin(A)[2:].zfill(48)
    print(f"A: {A}")
    if A == "111001111010010001100011001111110101101000101110":
        print("yay4")
    
    print(hex(int(A,2)))

    # ==================== part e ==================

    

