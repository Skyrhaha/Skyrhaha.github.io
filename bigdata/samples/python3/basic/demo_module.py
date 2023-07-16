# 模块测试

_privateVar = '我是私有变量'
__golbalVar = '我是全局变量'

def hello():
	print('hello, world!')

if __name__ == '__main__':
	print(f'我{__name__}被直接执行')
else:
	print(f'我{__name__}被别的模块调用执行')