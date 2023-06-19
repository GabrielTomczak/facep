import cv2
import mediapipe as mp
import math

# Função para calcular a distância entre dois pontos
def calcular_distance(point1, point2):
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Inicialização do MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Carregar o modelo de pontos de referência
model = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Carregar image de exemplo
image = cv2.imread('photo.jpg')

# Converter image para RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Processar a image
result = model.process(image_rgb)

# Verificar se foram encontrados pontos de referência
if result.multi_face_landmarks:
    for face_landmarks in result.multi_face_landmarks:
      # mp_drawing.draw_landmarks(
      #   image, face_landmarks,
      #   landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
      #   connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
      # )

      # Definir pontos de referência para calcular a distância
      # 2 - Nariz
      # 3 - Testa
      # 33 - Olho esquerdo
      # 40 - boca esquerdo
      # 261 - olho direito
      # 270 - boca direito
      point1 = face_landmarks.landmark[2]
      point2 = face_landmarks.landmark[222]


      # Converter coordenadas normalizadas para coordenadas da image
      height, width, _ = image.shape
      point1_px = int(point1.x * width), int(point1.y * height)
      point2_px = int(point2.x * width), int(point2.y * height)

      # Desenhar pontos de referência na image
      cv2.circle(image, point1_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point2_px, 5, (0, 255, 0), -1)

      # Calcular e exibir a distância entre os pontos
      distance = calcular_distance(point1_px, point2_px)
      print(distance)
      cv2.putText(image, f'Distancia: {distance:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('MediaPipe Face Landmarks', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
