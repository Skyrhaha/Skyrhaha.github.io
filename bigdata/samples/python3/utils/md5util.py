import hashlib

def getMD5(plaintext:str):

	# 方式一
	md5=hashlib.md5()
	md5.update(plaintext.encode('utf-8'))
	cipher = md5.hexdigest()

	# 方式二
	# cipher = hashlib.md5(bytes(plaintext, encoding='utf-8')).hexdigest()

	return cipher

if __name__ == '__main__':
	print(getMD5('123456')) # => e10adc3949ba59abbe56e057f20f883e