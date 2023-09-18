
# Visual Odometry

This is a Python implementation of Visual Odometry using OpenCV and PyTransform3D. Visual Odometry is a fundamental technique in computer vision and robotics that estimates the motion of a camera by analyzing the sequence of images it captures.

## Overview

This implementation uses the following components and libraries:

- OpenCV: Used for keypoint detection, feature matching, and essential matrix computation.
- PyTransform3D: Utilized for handling transformations, rotations, and camera poses.
- Matplotlib: Used for 3D visualization of camera poses.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- Numpy
- PyTransform3D
- Matplotlib

You can install these dependencies using `pip`:

```bash
pip install opencv-python numpy pytransform3d matplotlib
```



## Usage
```bash
git clone https://github.com/yourusername/visual-odometry.git
cd visual-odometry
python visual_odometry.py
```

You can specify the dataset directory in the data_dir variable within the main function. The code will load the camera calibration, ground truth poses, and images from the specified directory and perform visual odometry.


## Dataset

This implementation assumes that you have a dataset structured as follows:

    calib.txt: Camera calibration parameters.
    poses.txt: Ground truth camera poses.
    image_l/: Directory containing image frames.

You can use the KITTI dataset or any other dataset following a similar structure.
## Visualization

The code includes visualization of the estimated camera poses in 3D space. You can customize the visualization parameters in the main function.
![fig1](https://github.com/KiaRational/VisualOdometry/blob/main/Figure_1.png)
![fig1_html](https://github.com/KiaRational/VisualOdometry/blob/main/Figure_1.png)

