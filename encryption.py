import fractions

def findRelativePrime(z, min=2):
	for i in range(min, min + 1000):
		if fractions.gcd(z, i) == 1:
			return i
	assert False, 'relative prime of z could not be found'

def find_D(e, z, min=0):
	for i in range(min, 1000000):
		if (e * i) % z == 1:
			return i
	assert False, 'd value could not be found'
		

p = 379
q = 541

n = p*q
z = (p - 1) * (q - 1)
e = findRelativePrime(z)
d = find_D(e, z)

print 'private key:', (n, e)
print 'public key:', (n, d)

# The message must be an integer less than n-1. Convert an English message into a binary string,
# and then convert that binary string into an integer. As long as these conversion methods are a bijective mapping, and
# the recipiant is using the same methods as you, then everything will work out!
message = 32423
print 'message (must be < ' + str(n) + '-1):', message

encrypted_message = (message**e) % n
print 'encrypted message:', encrypted_message

decrypted_message = (encrypted_message**d) % n
print 'decrypted message:', decrypted_message

