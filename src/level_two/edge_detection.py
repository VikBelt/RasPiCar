
#Import the Needed Libraries
import numpy as np
import logging
import cv2
logging.basicConfig(level = logging.INFO) 

#########################################################################################
#                               LINE DETECTION PROCESSS                                 #
#########################################################################################


# edge detection function
def edge_detection(image):
    hsvImage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #bgr to hsv
    lowerArray = np.array([60,40,40])
    upperArray = np.array([150,255,255])
    maskedImg = cv2.inRange(hsvImage,lowerArray,upperArray) #blue mask
    edges = cv2.Canny(maskedImg,200,400) #edge detection
    return edges

def crop_image(image):
    height, width = image.shape
    mask = np.zeros_like(image)
    region = np.array([[
        (0, height * 1 / 2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask,region,255)
    cropped = cv2.bitwise_and(image,mask) #want to bit-mask to hide this
    return cropped

# Function for Line Detection
def line_detection(cropped):
    angle = np.pi/180 #radian angle
    threshold = 10
    p = 1 #rho
    line = cv2.HoughLinesP(cropped,p,angle,threshold,np.array([]), minLineLength=8, maxLineGap=4)
    return line

# Make a Helper Function
def create_points(image,line):
    height, width = image.shape
    slope, intercept = line
    y1 = height  
    y2 = int(y1 * 0.5)  # make points from middle of the frame down

    # bound the coordinates within the frame
    x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
    x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
    points = [[x1, y1, x2, y2]]
    return points

# Function to get the lane lines from 
def lane_lines(image,lines):
    lanes = []
    # null case
    if lines is None: 
        logging.warning("there are no line segments")
        return lanes

    height, width = image.shape
    left_fit = []
    right_fit = []
    #lanes on left/right 2/3 of the screen
    left_bound = width * (2/3)
    right_bound = width * (1/3) 

    for segment in lines:
        for x1,y1,x2,y2 in segment:
            #infinite slope case
            if x1 == x2:
                logging.warning("skipping: infinite slope")
                continue
            #get a fit line for a segment    
            fit_line = np.polyfit((x1,x2),(y1,y2),1) # y = mx + b
            slope = fit_line[0]
            intercept = fit_line[1]
            #left slope check
            if slope < 0:
                if x1 < left_bound and x2 < left_bound:
                    left_fit.append((slope,intercept))
            
            #right slope check
            else:
                if x1 > right_bound and x2 > right_bound:
                    right_fit.append((slope,intercept))
    
    left_avg = np.average(left_fit, axis = 0)
    if len(left_fit) > 0:
        lanes.append(create_points(image, left_avg))

    right_avg = np.average(right_fit, axis = 0)
    if len(right_fit) > 0:
        lanes.append(create_points(image, right_avg))
    
    return lanes

# Function for Full Lane Detection
def lane_detection(image):
    # go through the object detection process
    edges = edge_detection(image)
    cropped = crop_image(edges)
    line_segments = line_detection(cropped)
    lanes = lane_lines(cropped, line_segments)
    
    return lanes
# Function to show lines
def show_lines(image, lines, line_color=(0, 255, 0), line_width=8):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1 , y1), (x2, y2), line_color, line_width)
    line_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return line_image


###################################################################
#                          MAIN SCRIPT                            #
###################################################################


def main():
    #Image Test
    image = cv2.imread('E:\CVFolower\Capture.PNG')
    lines = lane_detection(image)
    lane_image = show_lines(image,lines)
    cv2.imshow("final", lane_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
