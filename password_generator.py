import random 
import string 

print('Welcome to password generator !')

def generator():
	length = int(input('Enter length: '))
	s1 = string.ascii_lowercase
	s2 = string.ascii_uppercase
	s3 = string.digits
	s4 = string.punctuation
	
	list = s1 + s2 + s3 + s4
	
	temp = random.sample(list, length)
	
	password = ''.join(temp)
	
	print(password)
	
generator()