# DES 1 Round
(a) Derive K1 the first-round subkey
(b) Derive L0, R0.
(c) Expand R0 to get E[R0], where E[⋅] is the expansion/permutation table in DES.
(d) Calculate A = E[R0] ⊕ K1
(e) Group the result from (d) into sets of 6 bits and evaluate the corresponding 8 S-box
substitutions.
(f) Concatenate the result from (e) to get a 32-bit result, B.
(g) Apply the permutation P to get P (B), where P (⋅) is the permutation table in DES.
(h) Calculate R1 = P (B) ⊕ L0.
(i) Write down the ciphertext.