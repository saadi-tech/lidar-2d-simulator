# 2D Lidar Simulator
## Description
`map_Generator.py` is a python script that generates a simulated lidar-scan for a given position in the provided map. It uses Bresenham ray-cast algorithm to simulate a 2d lidar on a given position in the map. It creates the near-to-realistic scan simulation (with Guassian Noise) using the obstacles from the map.

## Application
- It has been successfully employed to address the challenge of localizing a "kidnapped robot". The approach involves taking the original laser scan and generating multiple simulated scans at various positions within the provided map. These simulated scans are then compared to the original scan using ORB features, and the best-matching simulated scan is used to find the transformation between real scan and best-matching simulated scan, this transformation is further used to estimate the pose of the real robot in the given map.

For more information, you can check out the [kidnapped_robot_solver](https://github.com/saadi-tech/kidnapped_robot_finder) repository.


## Installation
1. Requires python3, numpy and openCV.

## Usage
1. Replace the absolute path to the map file in "map_generator.py".
2. Run the map_generator.py, and GUI window will show the map.
3. Left-click on any position on the map will simulate a robot on that position, and draw simulated scan around the robot.

## Usage Demo
Here are some screenshots of the lidar simulation in action:

![Screenshot 1](/media/image_1.png)


![Screenshot 2](/media/image_2.png)


![Screenshot 3](/media/image_3.png)

Feel free to get in touch. :) 