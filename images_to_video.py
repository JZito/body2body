import cv2
import argparse
import os


def main():
    dir_path = os.getcwd()+'/'+args.directory+'/'
    ext = args.extension
    output = args.output

    images = []
    for f in os.listdir(dir_path):
        if f.endswith(ext):
            images.append(f)

    # Determine the width and height from the first image
    image_path = os.path.join(dir_path, images[0])
    frame = cv2.imread(image_path)
    cv2.imshow('video',frame)
    height, width, channels = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, args.fps, (width, height))

    count = 0
    for image in images:
        count += 1
        print(count)
        image_path = os.path.join(dir_path, image)
        frame = cv2.imread(image_path)

        out.write(frame) # Write out frame to video

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

    print("The output video is {}".format(output))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "--ext", dest='extension',  required=False, default='jpg', help="image extension type default is 'jpg'.")
    parser.add_argument("--output", dest='output',  required=False, default='output.mp4', help="output video file name")
    parser.add_argument( "--dir", dest='directory',  required=False, default='.', help="image directories")
    parser.add_argument("--fps",  dest='fps', type=int, required=False, default='24', help="frames per second")
    args = parser.parse_args()

    main()