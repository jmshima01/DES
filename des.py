from sys import argv

class Des():
    def __init__(self, plaintext, key):
        self.key = bin(int(key,16))[2:].zfill(64)
        self.plaintext = bin(int(plaintext,16))[2:].zfill(64)
        self.IP = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
        ]
        self.PC1 = [
        [57, 49, 41, 33, 25, 17, 9],
        [1, 58, 50, 42, 34, 26, 18],
        [10, 2, 59, 51, 43, 35, 27],
        [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15],
        [7, 62, 54, 46, 38, 30, 22],
        [14, 6, 61, 53, 45, 37, 29],
        [21, 13, 5, 28, 20, 12, 4]
        ]
        self.PC2 = [
        [14, 17, 11, 24, 1, 5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]
        ]
        self.EXP = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]

        self.S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        
        self.P = [16, 7, 20, 21,29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

        self.K1 = self.__part_a()
        self.L_0, self.R_0 = self.__part_b()
        self.E_R0 = self.__part_c()
        self.A = self.__part_d()
        self.B = self.__part_e_and_f()
        self.P_B = self.__part_g()
        self.R_1 = self.__part_h()
        
        self.round_1_ciphertext = self.__part_i()

    def __part_a(self):
        pc1 = []
        for r in self.PC1:
            for v in r:
                pc1.append(v-1)
        
        pc1_key = [0]*56
        for i,v in enumerate(pc1):
            pc1_key[i] = self.key[v]
        
        pc1_key = ''.join(pc1_key)
    
        C = pc1_key[:28]
        D = pc1_key[28:]
    
        lcs = lambda b, n: bin(b<<n|b>>(64-n))[2:].zfill(28)
        C = lcs(int(C,2),1)
        D = lcs(int(D,2),1)
        
        C_D = C+D
   
        pc2 = []
        for r in self.PC2:
            for v in r:
                pc2.append(v-1)

        pc2_key = [0]*48

        for i,v in enumerate(pc2):
            pc2_key[i] = C_D[v]
        
        pc2_key = ''.join(pc2_key)
        K1 = pc2_key

        return K1

    def __part_b(self):
        sub = []
        for r in self.IP:
            for v in r:
                sub.append(v-1)

        ip_str = [0]*64
        for i,v in enumerate(sub):
            ip_str[i] = self.plaintext[v]
    
        ip_str = ''.join(ip_str)

        L_0 = ip_str[:32]
        R_0 = ip_str[32:]
        
        return L_0, R_0

    def __part_c(self):
        exp = [i-1 for i in self.EXP]

        E_R0 = [0]*48
        for i,v in enumerate(exp):
            E_R0[i] = self.R_0[v]
        E_R0 = ''.join(E_R0)
        return E_R0

    def __part_g(self):
        P = [i-1 for i in self.P]
        P_B = [0]*32
        for i,v in enumerate(P):
            P_B[i] = self.B[v]
        P_B = ''.join(P_B)
        return P_B
        
    def __part_h(self):
        R_1 = int(self.P_B,2) ^ int(self.L_0,2)
        R_1 = bin(R_1)[2:].zfill(32)
        return R_1

    def __part_d(self):
        A = int(self.E_R0,2) ^ int(self.K1,2)
        A = bin(A)[2:].zfill(48)

        return A
    
    def __sbox_sub(self,A_i,n):
            j = int(A_i[1:5],2)
            i = A_i[0]+A_i[-1]
            i = int(i,2)
            return bin(self.S[n][i][j])[2:].zfill(4)
        
    def __part_e_and_f(self):
        A_groups = []
        for i in range(0,48,6):
            A_groups.append(self.A[i:i+6])
        
        B = ""
        for i in range(8): # for all 8 S boxes
            B+=self.__sbox_sub(A_groups[i],i)
        
        return B

    def __part_g(self):
        P = [i-1 for i in self.P]
        P_B = [0]*32
        for i,v in enumerate(P):
            P_B[i] = self.B[v]
        P_B = ''.join(P_B)
        return P_B
        
    def __part_h(self):
        R_1 = int(self.P_B,2) ^ int(self.L_0,2)
        R_1 = bin(R_1)[2:].zfill(32)
        return R_1

    def __part_i(self):
        L_1 = self.R_0
        return L_1 + self.R_1
    
    def to_hex(self,bin_str):
        return hex(int(bin_str,2))
    
    def print_round1(self):
        print(f"plaintext: {self.to_hex(self.plaintext)}")
        print(f"key: {self.to_hex(self.key)}")
        print("-----------------")
        print(f"Part (a):     K1={self.to_hex(self.K1)}")
        print(f"Part (b):    L_0={self.to_hex(self.L_0)} R_0={self.to_hex(self.R_0)}")
        print(f"Part (c):  E[R0]={self.to_hex(self.E_R0)}")
        print(f"Part (d):      A={self.to_hex(self.A)}")
        print(f"Parts (e/f):   B={self.to_hex(self.B)}")
        print(f"Part (g):   P(B)={self.to_hex(self.P_B)}")
        print(f"Part (h):    R_1={self.to_hex(self.R_1)}")
        print(f"Part (i): Ciphertext={self.to_hex(self.round_1_ciphertext)}")


if __name__ == "__main__":
    
    if len(argv) < 3:
        print("Usage: python3 des.py plaintext_hex key_hex")
        exit(-1)
    
    des = Des(plaintext=argv[1],key=argv[2])
    des.print_round1()