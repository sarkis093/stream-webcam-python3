import cv2
import requests
import numpy as np

url = 'http://localhost:9090/shot.png'

webcam = cv2.VideoCapture(0)
validacao, frame = webcam.read()

img = requests.get(url)
img_arr = np.array(bytearray(img.content), dtype=np.uint8)
img_orig = cv2.imdecode(img_arr, -1)

cv2.imshow("Video da Webcam", frame)
cv2.namedWindow('IPcamera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('IPcamera', 300, 300)

# if webcam.isOpened():
#     validacao, frame = webcam.read()
#     while validacao:
#         validacao, frame = webcam.read()
#         cv2.imshow("Video da Webcam", frame)
#         key = cv2.waitKey(5)
#         if key == 27: # ESC
#             break
#     #cv2.imwrite("FotoLira.png", frame)

# webcam.release()
# cv2.destroyAllWindows()