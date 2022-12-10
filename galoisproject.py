import galois

prims = { 

'163' : 'x^163 + x^7 + x^6 + x^3 + 1', #primitive
'233' : 'x^233 + x^74 + 1', #primitive
'239' : 'x^239 + x^5 + x^4 + x^3 + x^2 + x + 1', #'x^239 + x^36 + 1'
'277' : 'x^277 + x^7 + x^5 + x^4 + x^2 + x + 1', #'x^277 + x^12 + x^6 + x^3 + 1',
'283' : 'x^283 + x^12 + x^7 + x^5 + 1', #primitive
'409' : 'x^409 + x^87 + 1', #primitive
'571' : 'x^571 + x^10 + x^5 + x^2 + 1', #primitive

}


def add(a,b,m,isbin):

	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = GF(a)
	b = GF(b)
	if isbin:
		return bin(int(a+b))[2:]
	else:
		return hex(int(a+b))[2:]
	
def sub(a,b,m,isbin):

	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = GF(a)
	b = GF(b)
	if isbin:
		return bin(int(a-b))[2:]
	else:
		return hex(int(a-b))[2:]
	
def multiply(a,b,m,isbin):
	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = GF(a)
	b = GF(b)
	if isbin:
		return bin(int(a*b))[2:]
	else:
		return hex(int(a*b))[2:]
	
def divide(a,b,m,isbin):
	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = GF(a)
	b = GF(b)
	if isbin:
		return bin(int(a/b))[2:]
	else:
		return hex(int(a/b))[2:]

def modulo(a,m,isbin):
	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = galois.Poly([int(x) for x in bin(a)[2:]],galois.GF2)
	mod = GF.irreducible_poly
	a=a%mod
	if isbin:
		return bin(int(a))[2:]
	else:
		return hex(int(a))[2:]


def invert(a,m,isbin):
	GF = galois._fields._factory._GF_extension(2,m,irreducible_poly_ = prims[str(m)] ,alpha=2, verify=False)
	a = GF(a)
	if isbin:
		return bin(int(a**-1))[2:]
	else:
		return hex(int(a**-1))[2:]