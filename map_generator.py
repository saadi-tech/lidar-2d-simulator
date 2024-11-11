import cv2
import numpy as np
import math

path = "/home/saad/Desktop/"
map_image = cv2.imread(path + "map_image.png")

# Resize the image while maintaining aspect ratio
width = 700
height = int(map_image.shape[0] * width / map_image.shape[1])
map_image = cv2.resize(map_image, (width, height))
lidar_range = 400 #px


def bresenham_ray_cast(image, x0, y0, angle):
    x0, y0 = int(x0), int(y0)
    angle_rad = math.radians(angle)
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)

    x, y = x0, y0
    while 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
        if image[int(y), int(x)] < 100:
            return int(x), int(y)
        x += dx
        y += dy
    return x-dx, y-dy

def get_lidar_points(bw_image, x0, y0, add_noise = True):
    mean = 0
    std_dev = 1.42
    angle_resolution = 1 #Degrees.
    angle_range = np.arange(0, 360,angle_resolution) #array of all angles in degrees.
    lidar_points = []
    for i in range(angle_range.shape[0]):
        noise_x = np.random.normal(mean, std_dev)
        noise_y = np.random.normal(mean, std_dev)

        point = bresenham_ray_cast(bw_image, x0, y0, angle_range[i])
        if add_noise:
            noisy_x = point[0] + noise_x
            noisy_y = point[1] + noise_y
            lidar_points.append([int(noisy_x), int(noisy_y)])
        else:
            lidar_points.append(point)

    return lidar_points


# Function to handle mouse click events
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        map_to_show = map_image.copy()
        # Draw a BLUE circle at the location of the click (ROBOT POSITION)
        cv2.circle(map_to_show, (x, y), 10, (255, 0, 0), -1)

        lidar_points = get_lidar_points(cv2.cvtColor(map_image, cv2.COLOR_BGR2GRAY), x, y)
        for point in lidar_points:
            cv2.circle(map_to_show, (point[0], point[1]), 2, (0, 0, 255), -1)
            #cv2.imshow('Image', map_to_show)
            #cv2.waitKey(0)

        cv2.imshow('Image', map_to_show)


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

# Display the image
cv2.imshow('Image', map_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
