import uuid

def getUUID():
	return str(uuid.uuid1())

if __name__ == '__main__':
	print(getUUID())