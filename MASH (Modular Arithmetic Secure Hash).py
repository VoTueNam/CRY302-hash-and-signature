#Name: Vo Tue Nam 	ID: CE140557
import math
import random
import sage
from sympy import *



"""2. a)	Write a function that takes a bitlenght n and generates 
a modulus N of bitlength n and g less than N and relatively prime to it."""
print("a)	Write a function that takes a bitlenght n and generates a modulus N")
print(" of bitlength n and g less than N and relatively prime to it")
print("\nGiven,"
"\nN > n, n is prime"
"\nN > g, g is prime")

print("\n PLEASE SEE MY CODE  \n")

def generate_modN(n):
	m = (int) (n / 2)
	p = 1
	while (p < 2^(m-1)):
		p = random_prime(2^m,1000)
	q = 1
	while (q < 2^(m-1)):
		q = random_prime(2^m,1000)
	N = p*q
	g = p
	while g == p or g == q:
		g = random_prime(2,1000)
	return (N,g)

def random_prime(m,c):
    n = random.randint(m,c)
    while not isprime(n):
        n = random.randint(m,c)
    return n

print()




"""b)	Show the output of your function from part (a) for a few outputs. """
print("b) 	Show the output of your function from part (a) for a few outputs.")

print("We have n = 60 and generate module N and g is: ",generate_modN(60))
print("We have n = 29 and generate module N and g is: ",generate_modN(29))
print("We have n = 38 and generate module N and g is: ",generate_modN(38))
print("We have n = 76 and generate module N and g is: ",generate_modN(76))
print()





"""c)	Using N, g, n as arguements write a function to perform the hashing."""
print("c)	Using N, g, n as arguements write a function to perform the hashing.")

print("\n PLEASE SEE MY CODE  \n")

def hash1(N,g,n):
	def generate_hash(N,g,n):
		H = (g**n) % N
		return H 
	
	if(n<100000):
		return generate_hash(N,g,n)
	else:
		add_n = n % 100000
		n = n - add_n
		add_result = generate_hash(N,g,add_n)
		n = int(n / 100000)
		g= generate_hash(N,g,n)
		result = generate_hash(N,g,100000)
		Final = (add_result * result) % N
		return Final

print()






""""d)	N = 600107, g = 154835, n = 239715 """
print("d)	N = 600107, g = 154835, n = 239715\n")
print("   H = g^n mod N = ", hash1(600107,154835,239715))



print()


"""e)	N = 548155966307, g = 189830397891, n = 44344313866 """
print("e)	N = 548155966307, g = 189830397891, n = 44344313866\n")
print("   H = g^n mod N = ", hash1(548155966307,189830397891,44344313866))

print()


"""f)	N = 604766153, g = 12075635, n = 443096843 """
print("f)	N = 604766153, g = 12075635, n = 443096843\n")
print("   H = g^n mod N = ", hash1(604766153,12075635,443096843))


print()




"""g)	Write a function that creates a collision given p and q.  
Show that your function works for a couple of examples. """
print("g)	Write a function that creates a collision given p and q. Show that your function works for a couple of examples.")

def collision_I(i):
	print("Have have n = ", i)
	print("And generate:")
	(N,g) = generate_modN(i)
	print("N = ", N)
	print("g = ", g)
	
	print("H = g^n mod N = ", hash1(N,g,i))

print("\nExamples 1: ")
collision_I(29)

print("\nExamples 2: ")
collision_I(54)

print("\nExamples 3: ")
collision_I(96)

