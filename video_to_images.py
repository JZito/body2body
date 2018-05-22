import cv2
import os
import argparse

def main():

    if not os.path.exists(args.directory):
        os.makedirs(args.directory)
    vidcap = cv2.VideoCapture(args.filename)
    success,image = vidcap.read()
    count = 0
    success = True
    path = os.getcwd() + "/" + args.directory + "/"
    while success:
      fn = 'frame'+str(count).zfill(8)+'.jpg'
      cv2.imwrite(os.path.join(path,fn), image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='filename', type=str, help='Name of the video file.')
    parser.add_argument('--dir', dest='directory', type=str, help='Name of the directory in which to save.')
    args = parser.parse_args()

    main()
