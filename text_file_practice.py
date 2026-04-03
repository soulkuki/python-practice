import os
from pathlib import Path

operationMap = {
	'read': 'r',
	'write': 'w',
	'append': 'a',
}
firstLineContent = ''

currentDir = Path(__file__).parent
path1 = os.path.join(os.path.dirname(__file__), 'demo.text')
path2 = f'{Path(__file__).parent}/demo.text'

print(f'当前路径os: {path1}')
print(f'当前路径pathlib: {path2}')

def read(file):
	global firstLineContent
	for index, line in enumerate(file, start=1):
		print(f'第{index}行内容: {line.strip()}')
	file.seek(0)
	for index, line in enumerate(file, start=1):
		if 'python' in line:
			print(f'包含python的是第{index}行的内容: {line.strip()}')
	file.seek(0)
	fullContent = file.read()
	contentSize = len(fullContent)
	contentLines = fullContent.split('\n')
	filePosition = file.tell()
	file.seek(0)
	fiveContentSize = file.read(5)
	file.seek(0)
	firstLineContent = file.readline().strip()
	secondLineContent = file.readline().strip()
	file.seek(0)
	allLineContent = file.readlines()
	newLineContent = firstLineContent.replace('python', 'java')
	isPython = 'python' in firstLineContent
	isJavaStart = firstLineContent.startswith('java')
	isLanguageEnd = secondLineContent.endswith('编程语言')
	

	print(f'完整内容: \n{fullContent}')
	print(f'内容长度: {contentSize}')
	print(f'内容行数: {contentLines}')
	print(f'文件指针位置: {filePosition}')
	print(f'前5个字符: {fiveContentSize}')
	print(f'第一行内容: {firstLineContent}')
	print(f'第二行内容: {secondLineContent}')
	print(f'所有行内容: {allLineContent}')
	print(f'修改后的第一行内容: {newLineContent}')
	print(f'第一行是否包含python: {isPython}')
	print(f'第一行是否以java开头: {isJavaStart}')
	print(f'第二行是否以编程语言结尾: {isLanguageEnd}')

def write(file):
	file.write(firstLineContent)

def pratice(operation, path = path2):
	with open(path, operationMap[operation], encoding='utf-8') as file:
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
		pratice('write', f'{currentDir}/target.text')
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
