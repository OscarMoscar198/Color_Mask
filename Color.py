import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('example3.jpg')

# Definir rango de color azul en el espacio de color HSV
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([140, 255, 255])

# Convertir la imagen de BGR a HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Filtrar los colores azules en el rango definido
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Encontrar contornos de objetos azules
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen original y la máscara
cv2.imshow('Original', image)
cv2.imshow('Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
