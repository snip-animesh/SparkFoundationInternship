# Importing Libraries
import easyocr
import cv2
from matplotlib import pyplot as plt

# Define the location of the image
DIR=r'D:\python Code\Spark Foundation Internship\Task_1_OpticalCaracterRecognition\Resources\2.JPG'
# Reading the image
img=cv2.imread(DIR)

# Making object of easyocr module
reader = easyocr.Reader(['en'])
# Reading the Text
result = reader.readtext(DIR)

# Opening/Creating a text file to write the texts on it
with open('texts.txt','w') as fp:
    # Marking the texts on the image
    for res in result:
        cv2.rectangle(img,tuple(res[0][0]), tuple(res[0][2]), (0,255,0), 1)
        # Writing the texts on text file
        fp.write(res[1])
        fp.write('\n')
fp.close()

# Showing the image
plt.imshow(img)
plt.show()