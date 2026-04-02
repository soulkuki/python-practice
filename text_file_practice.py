import os
from pathlib import Path

operationMap = {
	'read': 'r',
	'write': 'w',
	'append': 'a',
}

currentDir = Path(__file__).parent
path1 = os.path.join(os.path.dirname(__file__), 'demo.text')
path2 = f'{Path(__file__).parent}/demo.text'

print(f'当前路径os: {path1}')
print(f'当前路径pathlib: {path2}')

def read(file):
	fullContent = file.read()
	contentSize = len(fullContent)
	contentLines = fullContent.split('\n')
	filePosition = file.tell()
	file.seek(0)
	fiveContentSize = file.read(5)
	file.seek(0)
	firstLineContent = file.readline()
	secondLineContent = file.readline()
	allLineContent = file.readlines()
	file.seek(0)
	for line in file:
		print(f'每行内容: {line.strip()}')

	print(f'完整内容: \n{fullContent}')
	print(f'内容长度: {contentSize}')
	print(f'内容行数: {contentLines}')
	print(f'文件指针位置: {filePosition}')
	print(f'前5个字符: {fiveContentSize}')
	print(f'第一行内容: {firstLineContent}')
	print(f'第二行内容: {secondLineContent}')
	print(f'所有行内容: {allLineContent}')
def pratice(operation):
	with open(path2, operationMap[operation], encoding='utf-8') as file:
		match operation:
			case 'read':
				read(file)
			case 'write':
				write(file)
			case 'append':
				append(file)
			case _:
				print('不支持的操作: ', operation)
def main():
	try:
		pratice('read')
		# pratice('write')
		# pratice('append')
	except Exception as e:
		if isinstance(e, FileNotFoundError):
			print('demo.text文件不存在')
		elif isinstance(e, UnicodeDecodeError):
			print('demo.text文件编码错误')
		elif isinstance(e, IOError):
			print('demo.text文件读取错误')
		elif isinstance(e, PermissionError):
			print('demo.text文件权限错误')
		elif isinstance(e, OSError):
			print('demo.text文件系统错误')
		else:
			print('error: ', e)
	finally:
		print('结束')
		
main()

