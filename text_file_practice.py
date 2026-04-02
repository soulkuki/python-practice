import os
from pathlib import Path

currentDir = Path(__file__).parent
demoPath1 = os.path.join(os.path.dirname(__file__), 'demo.text')
demoPath2 = f'{Path(__file__).parent}/demo.text'

print(f'当前路径os: {demoPath1}')
print(f'当前路径pathlib: {demoPath2}')

def read(path):
    
    with open(path, 'r', encoding='utf-8') as file:
        print(f'完整内容: {file.read()}')
def main():
    try:
        read(demoPath2)
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
