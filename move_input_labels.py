import os
import argparse

def main():
    directory = os.getcwd()+ '/' + args.directory +'/'
    new_directory = os.getcwd() + '/input_labels/'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    offender = 'input'
    for filename in os.listdir(directory):
        if offender in filename:
            print(filename)
            os.rename(directory+filename, new_directory+filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', dest='directory', type=str, help='Name of the directory in which to remove our inputs.')
    args = parser.parse_args()

    main()