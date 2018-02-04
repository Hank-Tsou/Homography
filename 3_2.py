import cv2 # opencv-python
import numpy as np # use numpy library as np for array object
import find_points # import function from assignment 2_1-c (find four corner points)

source_img = cv2.imread("pool.jpg") # Read the image.
source_pts_selection = input('1. precise corner points 2. detected corner points: ') # select points source

#---------------------------------------------------------------------#
# Source image down-left point --> Desination image top-left point    #
# Source image top-left point --> Desination image top-right point    #
# Source image top-right point --> Desination image down- right point #
# Source image down-right point --> Desination image down-left point  #
#---------------------------------------------------------------------#

# destination image size
des_height = 450 
des_width = 800

### create a list of destinaiton points
des_pts = np.empty((0,2)) 
des_pts = np.append(des_pts, [(0,0)], axis=0) # top-left point
des_pts = np.append(des_pts, [(des_width-1,0)], axis=0) # top-right point
des_pts = np.append(des_pts, [(des_width-1,des_height-1)], axis=0) # down-right point
des_pts = np.append(des_pts, [(0,des_height-1)], axis=0) # down-left point

### create a list of source points
src_pts = np.empty((0,2))

if source_pts_selection == 1: # slecte the precise corner points
    src_pts = np.append(src_pts, [(68,870)], axis=0) # down-left point
    src_pts = np.append(src_pts, [(844,514)], axis=0) # top-left point
    src_pts = np.append(src_pts, [(1445,552)], axis=0) # top-right point
    src_pts = np.append(src_pts, [(1290,1046)], axis=0) # down-right point

if source_pts_selection == 2: # slecte the detected corner points from "find_points.py"  
    # res = all detected points, point_selection = selected four points
    res, point_selection = find_points.find_4_point(source_img) 
    for i in range(4): # append four points into src_pts (source points)
        src_pts = np.append(src_pts,[(res[point_selection[i],2],res[point_selection[i],3])],axis=0)


# call function "cv2.findHomography" to find homography
tform, _ = cv2.findHomography(src_pts, des_pts)
 
# source image --> transform matrix --> destination image
result_img = cv2.warpPerspective(source_img, tform,(des_width, des_height))
#----------------------------------------------------#
# 1 parameter = original image                       #
# 2 parameter = transformation matrix                #
# 3 parameter = width and height of the output image #
#----------------------------------------------------#

#cv2.imwrite("Image1.jpg", result_img) # output result image 
cv2.imshow("result_img", result_img) # show result image
cv2.waitKey(0) # system pause 