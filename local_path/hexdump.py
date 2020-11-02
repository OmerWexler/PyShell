import os
import time

def main(argv):
    if len(argv) != 2:
        print('An incorrect number of arguments was supplied.')
        return
    
    file_name = argv[1] 
    try:
        with open(file_name, 'rb') as file:
            for i in range(0, os.path.getsize(file_name)):
                if i % 8 == 7:
                    print(file.read(1).hex(), end='\n')
                elif i % 8 == 0:
                    print(f'{int(i / 8)}. {file.read(1).hex()}', end='  ')
                else: 
                    print(file.read(1).hex(), end='  ')
    except Exception as e:
        print(e)
    print()


if __name__ == '__main__':
    main(os.sys.argv)