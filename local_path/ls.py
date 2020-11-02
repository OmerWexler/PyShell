import os 

def main(argv):
    if len(argv) != 2:
        print('An incorrect number of arguments was supplied.')
        return

    dir_ = argv[1]
    dir_to_list = ''

    if dir_ == '.':
        dir_to_list = os.getcwd()

    elif os.path.exists(os.path.join(os.getcwd(), dir_)):
        dir_to_list = os.path.join(os.getcwd(), dir_)

    elif os.path.exists(dir_):
        dir_to_list = dir_

    else:
        print(f'Directory {dir_} not found.')
        return 
        
    for inner in os.listdir(dir_to_list):
        print(inner)

if __name__ == '__main__':
    main(os.sys.argv)