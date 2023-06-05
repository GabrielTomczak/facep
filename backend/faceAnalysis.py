from imutils import face_utils
import dlib
import cv2
import math
from PIL import Image

class FaceAnalysis():
    def __init__(self, name):
        self.name = name

    def calculateDistance(self, x1, y1, x2, y2):
        a = x2 - x1
        b = y2 - y1
        distance = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return distance

    def px_to_cm(self, pixels, ppcm):
        centimeters = pixels / ppcm
        return centimeters

    def getImageResolution(self, camera):
        width    = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height   = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        ratio    = camera.get(cv2.CAP_PROP_POS_AVI_RATIO)
        duration = camera.get(cv2.CAP_PROP_POS_MSEC) / 1000
        frames   = ratio * duration * camera.get(cv2.CAP_PROP_FPS)
        ppcm     = (width/frames) * 2.54
        return ppcm

    def getImagePixels(self, camera, image):
        width    = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height   = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        ratio    = camera.get(cv2.CAP_PROP_POS_AVI_RATIO)
        duration = camera.get(cv2.CAP_PROP_POS_MSEC) / 1000
        frame    = image
        height, width, channel = frame.shape
        num_pixels = width * height * channel
        return num_pixels

face = FaceAnalysis("teste")
model = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model)
camera = cv2.VideoCapture(0)
# cv2.imwrite("face.jpg", image)
# if ret:
while True:
    # ppcm = face.getImageResolution(camera)
    ret, image = camera.read()
    pixels = face.getImagePixels(camera, image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        for (x, y) in shape:
            cv2.circle(image, (x,y), 2, (0, 255, 0), -1)
            # cv2.circle(image, (shape[8]), 2, (0, 255, 0), -1)
            # cv2.circle(image, (shape[33]), 2, (0, 255, 0), -1)

        x1, y1 = shape[8]
        x2, y2 = shape[33]
        print("Distância: %.2f" % face.calculateDistance(x1, y1, x2, y2))

    cv2.imshow("Output", image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
