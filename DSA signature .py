#Name: Vo Tue Nam	ID: CE140557
from sympy import *
import random


def DSA_verify(p, q, g, y, H, r, s):

    w = pow(s,-1,q)
    print("w= ",w)

    u1 = H*w % q
    print("u1= ",u1)

    u2 = (r*w) % q
    print("u2= ",u2)

    v = (g**u1 * y**u2)%p %q
    print("r= ",r)
    print("v= ",v)
    return (v == r)


def DSA_generate_domain_parameters():
    g = 1
    while (1 == g):
        # first find a q    
        q = 1
        q = randprime(2**15,2**16)
        # next find a p    
        p = 1
        while (not isprime(p)):
            p = (2**47 + random.randint(1,2**45)*2)*q + 1 
        h = random.randint(2,p-1)

        g = pow(h,int((p-1)/q),p)
    return (p, q, g)


def DSA_generate_keypair(p, q, g):
    x = random.randint(2,q-1)
    y = pow(g,x,p)
    #y = y.lift()
    return (x,y)


def DSA_sign(p, q, g, x, H):
    k = random.randint(2,q-1)
    r = int(pow(g,k,p)) % q
    kinv = pow(k,-1,q)
    s = kinv*(H + x*r) % q
    return (r, s)


'''3. Assume that we are using DSA with domain parameters: 
p = 7,877,914,592,603,328,881
q = 44449
g = 2,860,021,798,868,462,661
Use these domain parameters to determine if the signatures are valid in parts (a)-(c)'''

print("\n3.Use these domain parameters to determine if the signatures are valid in parts ")
print("\np = 7,877,914,592,603,328,881"
"\nq = 44449"
"\ng = 2,860,021,798,868,462,661\n")

p = 7877914592603328881
q = 44449
g = 2860021798868462661



print("\na. ")
y = 3798043471854149631
H = 59367
r = 31019
s = 43556
print("y= ",y)
print("H= ",H)
print("r= ",r)
print("s= ",s)
print("DSA verify is: ",DSA_verify(p, q, g, y, H, r, s))


print("\nb. ")
y = 1829820126190370021
H = 77241
r = 24646
s = 43556
print("y= ",y)
print("H= ",H)
print("r= ",r)
print("s= ",s)
print("DSA verify is: ",DSA_verify(p, q, g, y, H, r, s))


print("\nc. ")
y = 4519088706115097514
H = 48302
r = 36283
s = 32514
print("y= ",y)
print("H= ",H)
print("r= ",r)
print("s= ",s)
print("DSA verify is: ",DSA_verify(p, q, g, y, H, r, s))
    
print("\nPerform a signing operation in parts (d)-(e)")

print("\nd. ")
x = 8146
H = 22655
print("x= ",x)
print("H= ",H)
print("signature (r,s) = ", DSA_sign(p,q,g,x,H))

print("\ne. ")
x = 1548
H = 32782
print("x= ",x)
print("H= ",H)
print("signature (r,s) = ", DSA_sign(p,q,g,x,H))




'''
4. The purpose of this problem is to implement a DSA signature verification function. 
'''

print("\n4. The purpose of this problem is to implement a DSA signature verification function. ")
print("\na. Implement a function that takes domain parameters p, q, and g.  Also, a Hash value H (in {1, 2, …, p-1}) a public key y, and a signature (r,s).")

print("\n   PLEASE SEE MY FUNCTION in my code: DSA_verify")

print("\nb. Use the function you wrote in part (a) as well as the functions from the DSA examples to simulate a DSA signature and verify like in the examples.")

print("\nExample: p=283,q=47,g=60,y=158,H=41 ,r=19,s=30")
print("DSA verify is: ",DSA_verify(283, 47, 60, 158, 41, 19, 30))



'''
5. DSA Example. Using Sage, we can perform a DSA sign and verify:
'''

print("\n5. DSA Example. We can perform a DSA sign and verify:")


S = DSA_generate_domain_parameters()
print("(p , q , g = )", S)
D = DSA_generate_keypair(S[0], S[1], S[2])
print("(X,Y) = ", D)
H = random.randint(2,S[0]-1)
RS = DSA_sign(S[0], S[1], S[2], D[0], H)
print("(r,s) = ",RS)
print(DSA_verify(S[0], S[1], S[2],D[1],H,RS[0],RS[1]))
'''
6. The following functions implement DSA domain parameter generation, key generation, and DSA Signing.
'''
print("\n6. The following functions implement DSA domain parameter generation, key generation, and DSA Signing.")

print("\n   PLEASE SEE MY FUNCTION in my code:" 
    "\nDSA_generate_domain_parameters" 
    "\nDSA_generate_keypair" 
    "\nDSA_sign")

S = DSA_generate_domain_parameters()
D = DSA_generate_keypair(S[0], S[1], S[2])
H = random.randint(2,S[0]-1)
print("\nGeneration signature (r,s) = ",DSA_sign(S[0], S[1], S[2], D[0], H))
