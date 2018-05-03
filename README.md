# Body2Body HD

Making someone someone else

## How

These instructions will allow you to create a hi-def digital puppet from existing source video. You can transpose someone else's likeness, essentially their "puppet", onto your own video performance "puppeteer".

### Prerequisites

Requires Ubuntu 16.04, [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), [OpenCV](https://opencv.org/),[Pytorch](https://pytorch.org/) and [Pix2PixHD](https://github.com/NVIDIA/pix2pixHD).

### Create images from your videos

You only need OpenCV to convert your source video to image frames and vice-versa. The simplest way to install OpenCV is with [Anaconda](http://www.anaconda.org)

```
conda install -c conda-forge opencv 
```

then export your video to images. Run the following script for both your training puppet and testing puppeteer. Use the directory name ```train_B``` for your source puppet and ```test_B``` for the video of your puppeteer. 

```
python video_to_images.py --file your_puppet_filename.mp4 --dir train_B
```

If you don't have Anaconda and/or OpenCV, just find some software that will export your videos to a series of images and place them in the proper directories.

### Capture poses from your images
Navigate to your OpenPose directory 

```
cd openpose
```

and use OpenPose to extract the skeleton from your directory of images. Use ```train_A``` as the directory for your posed puppet and ```test_A``` for your posed puppeteer:

```
./build/examples/openpose/openpose.bin --disable_blending --face --hand --image_dir /path/to/your/images/train_B  --write_images /path/to/export/images/train_A
```

We use the flags ```--disable_blending``` to remove the original source and give us our pure skeleton on a black background and ```--face --hand``` to get a skeleton that includes, not surprisingly, face and hands.



### Launch a screen

If we're training in the cloud, we want to launch a 'screen'. Enter 

```
screen
```

and we can keep our training running when disconnected. If you reconnect, just enter

```
screen -r
```

to return to your training in progress.

### Train your puppet

Clone the Pix2PixHD repo:

```
git clone https://github.com/NVIDIA/pix2pixHD.git
```

Then make a folder for your data inside  ```pix2pixHD/datasets```

```
cd pix2pixHD/datasets && mkdir project_name
```

Move your training and testing directories to your newly created project directory. Your data must be arranged in the ```train_A```, ```train_B```, ```test_A``` format as described earlier. Navigate back to the base of the pix2pixHD directory, it's time to start training.

```
python train.py --name project_name --label_nc 0 --no_instance --use_dropout --no_flip
```

```--label_nc 0``` and ```--no_instance``` tells pix2pix to stick to the RGB image values for its training labels while the ```--use_dropout``` flag now returns false, as we don't want to use dropout. Training is nearly as effective without dropout and it prevents the model's output from developing a flickering, random characteristic that's unpleasant for video. ```--no_flip``` in this case actually means yes, flip- basically whether or not to flip images during training is up to you and the effect you are trying to achieve.

### Watch your model train

Ensure you've arranged your data correctly and check out the results of your model's training in progress in Pix2PixHD's ```checkpoints``` directory. They're pretty cool looking. 

### Test your puppeteer

When your model is sufficiently trained, or has reached a sensible checkpoint, test out your puppeteer. 

```
python test.py --name project_name --how_many 1000
```

```how_many``` is how many images you want to run your test on. Check the ```results``` directory to see your model's output.

###Make a video

When your model is done outputting images, you can remove your input labels from your results dir.

```
python move_input_labels.py --dir pix2pixHD/results/project_name/test_latest/images
```

Once your directory is left with its synthesized images, turn the contents of that directory into a video.

```
python create_video.py --dir pix2pixHD/results/project_name/test_latest/images --output puppeteer.mp4 --fps 30 --ext jpg
```

Congratulations, you are now a neural puppeteer. Make something weird. 


## Authors

* **Jeff Zito** - [Artificial Nature](https://www.artificialnature.io)


## Acknowledgments

* [the Nvidia team](https://github.com/NVIDIA/pix2pixHD)
* Dat Tran for his [face2face-demo](https://github.com/datitran/face2face-demo) and Karol Majek for the inspiration in mentioning OpenPose in his [face2face-demo](https://github.com/karolmajek/face2face-demo) fork.github.com/datitran/face2face-demo) and Karol Majek for the inspiration in mentioning OpenPose in his [face2face-demo](https://github.com/karolmajek/face2face-demo) fork.