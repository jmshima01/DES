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
        
        
        