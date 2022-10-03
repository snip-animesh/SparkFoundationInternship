## Author : Animesh Sarkar Tusher ##

# Importing our Libraries
from cv2 import cv2
import pandas as pd

# Defining path of necessary files
img_path = r'D:\python Code\Spark Foundation Internship\Task_2_ColorIdentification\Resources\test.jpg'
csv_path = r'D:\python Code\Spark Foundation Internship\Task_2_ColorIdentification\Resources\colors.csv'
img = cv2.imread(img_path)

# Reading csv file and giving name of each column
index = ["color", "color_name", "hex", "R", "G", "B"]
colors_file = pd.read_csv(csv_path, names=index, header=None)

FLAGS = False
R = G = B = X_POS = Y_POS = 0


# function to get x,y coordinates of mouse double click
def get_coordinates(event, x, y, flags, param):
    global B, G, R, X_POS, Y_POS, FLAGS
    if event == cv2.EVENT_LBUTTONDBLCLK:
        X_POS = x
        Y_POS = y

        B, G, R = img[y, x]

        B = int(B)
        G = int(G)
        R = int(R)
        FLAGS = True


# Get the color name
def get_color_name(R, G, B):
    minimum = 1000000
    cname = None
    for i in range(len(colors_file)):
        diff = abs(R - int(colors_file.loc[i, "R"])) + abs(G - int(colors_file.loc[i, "G"])) + abs(
            B - int(colors_file.loc[i, "B"]))
        if diff <= minimum:
            minimum = diff
            cname = colors_file.loc[i, "color_name"]
    return cname


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", get_coordinates)

while True:

    cv2.imshow("Image", img)
    if FLAGS:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (700, 60), (B, G, R), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(R, G, B) + ' R=' + str(R) + ' G=' + str(G) + ' B=' + str(B)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA, cv2.FONT_HERSHEY_SIMPLEX)

        # For very light colours we will display text in black colour
        if R + G + B >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA, cv2.FONT_HERSHEY_SIMPLEX)

        FLAGS = False

    # Break the loop when user hits 'q' key
    if cv2.waitKey(1)  == ord('q'):
        break

cv2.destroyAllWindows()
