import cv2
import mediapipe as mp
import math
import numpy as np

def calcDistance (point1, point2):
  return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def calcThird(third, trme):
  thirdValue = third * 100
  trmeValue = thirdValue / trme
  return trmeValue

def faceHeightAnalysis(faceHeight):
  if (faceHeight < 75):
    print('Altura: Face longa - Indica preenchimento de malar.')
  elif (faceHeight > 75):
    print('Altura: Face curta - Indica preenchimento de terço inferior.')

def faceWidthAnalysis(sex, faceWidth):
  if (faceWidth < 75 and sex == "female"):
    print('Largura: Zi zi muito grande - Indica prenchimento mandibula/mento.')
  elif (faceWidth > 75 and sex == "female"):
    print('Largura: Go go muito grande - Indica preenchimento zigomatico/malar.')
  elif (faceWidth < 75 and sex == "male"):
    print('Largura: Zi zi muito grande - Indica prenchimento mandibula/mento.')
  elif (faceWidth > 75 and sex == "male"):
    print('Largura: Face com tamanho ideal.')

def lowerThirdAnalysis(sex, third):
  if (sex == "male" and third > 36):
    print('Destacar terço médio Zi zi/Go go.')
  elif (sex == "male" and third < 36):
    print('Destacar')
  elif (sex == "female" and third > 33):
    print('Destacar terço médio Zi zi/Go go.')
  elif (sex == "female" and third < 33):
    print('Destacar')

def middleThirdAnalysis(sex, third):
  if (sex == "male" and third > 30):
    print('Destacar terço inferior.')
  elif (sex == "male" and third < 30):
    print('Destacar molar CK3.')
  elif (sex == "female" and third > 33):
    print('Destacar terço inferior.')
  elif (sex == "female" and third < 33):
    print('Destacar molar CK3.')

def upperThirdAnalysis(sex, third):
  if (sex == "male" and third > 34):
    print('Destacar terço médio e inferior.')
  elif (sex == "male" and third < 34):
    print('Destacar terço médio e inferior.')
  elif (sex == "female" and third > 34):
    print('Destacar terço Destacar terço médio e inferior.')
  elif (sex == "female" and third < 34):
    print('Destacar terço médio e inferior.')


faceModel = mp.solutions.face_mesh
model = faceModel.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

image = cv2.imread('images/photo.jpg')
original_width, original_height = image.shape[:2]

new_width = 450
new_height = 600

resized_image = cv2.resize(image, (new_width, new_height))
image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

processedModel = model.process(image_rgb)

if processedModel.multi_face_landmarks:
    for face_landmarks in processedModel.multi_face_landmarks:
      #trme - Testa ao queixo (Face)
      point1 = face_landmarks.landmark[10]
      point2 = face_landmarks.landmark[175]

      #Zizi - Orelha
      point3 = face_landmarks.landmark[34]
      point4 = face_landmarks.landmark[264]

      #Gogo - Mandibula
      point5 = face_landmarks.landmark[58]
      point6 = face_landmarks.landmark[288]

      #SnN - Nariz e sobrancelha
      point7 = face_landmarks.landmark[2]
      point8 = face_landmarks.landmark[9]

      height, width, _ = resized_image.shape
      point1_px = int(point1.x * width), int(point1.y * height)
      point2_px = int(point2.x * width), int(point2.y * height)
      point3_px = int(point3.x * width), int(point3.y * height)
      point4_px = int(point4.x * width), int(point4.y * height)
      point5_px = int(point5.x * width), int(point5.y * height)
      point6_px = int(point6.x * width), int(point6.y * height)
      point7_px = int(point7.x * width), int(point7.y * height)
      point8_px = int(point8.x * width), int(point8.y * height)

      cv2.circle(resized_image, point1_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point2_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point3_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point4_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point5_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point6_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point7_px, 5, (0, 255, 0), -1)
      cv2.circle(resized_image, point8_px, 5, (0, 255, 0), -1)

      trmeDistance = calcDistance(point1_px, point2_px)
      ziziDistance = calcDistance(point3_px, point4_px)
      gogoDistance = calcDistance(point5_px, point6_px)
      snnDistance  = calcDistance(point7_px, point8_px)
      lowerThird   = calcDistance(point2_px, point7_px)
      middleThird  = calcDistance(point7_px, point8_px)
      upperThird   = calcDistance(point1_px, point8_px)

      focal_length = 22

      trme         = trmeDistance * focal_length / width
      zizi         = ziziDistance * focal_length / width
      gogo         = gogoDistance * focal_length / width
      snn          = snnDistance  * focal_length / width
      lowerThird   = lowerThird   * focal_length / width
      middleThird  = middleThird  * focal_length / width
      upperThird   = upperThird   * focal_length / width

      faceHeight = (zizi / trme) * 100
      faceWidth  = (gogo / zizi) * 100

      lower  = calcThird(lowerThird, trme)
      middle = calcThird(middleThird, trme)
      upper  = calcThird(upperThird, trme)

      print(f'\nTrme_zizi: {faceHeight:.2f} %')
      faceHeightAnalysis(faceHeight)
      print(f'\nZizi_Gogo: {faceWidth:.2f} %')
      faceWidthAnalysis("male", faceWidth)
      print('\n')
      print(f'Terço inferior: {lower:.0f} %')
      lowerThirdAnalysis("male", lowerThird)
      print('\n')
      print(f'Terço meio: {middle:.0f} %')
      middleThirdAnalysis("male", middleThird)
      print('\n')
      print(f'Terço superior: {upper:.0f} %')
      upperThirdAnalysis("male", upperThird)
      print('\n')

cv2.imshow('Análise Facial', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
