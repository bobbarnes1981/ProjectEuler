import math

def solution(target):
	prime = 2
	primes = [prime]
	prime += 1
	primes.append(prime)
	while prime + 2 < target:
		prime += 2
		is_prime = True
		sqrt_prime = math.sqrt(prime)
		for p in primes:
			if p > sqrt_prime:
				break
			if prime % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(prime)
	print(sum(primes))

if __name__ == '__main__':
	solution(2000000)