#SUJAY MALADI
#CODE CLAUSE INTERNSHIP | PROJECT 2: IMAGE TO PENCIL SKETCH

import cv2

def image_to_pencil_sketch(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    
    # Blur the inverted image using GaussianBlur
    blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)
    
    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    
    # Blend the grayscale image with the inverted blurred image using the color dodge blend mode
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    # Display the original image and the pencil sketch
    cv2.imshow('Original Image', image)
    cv2.imshow('Pencil Sketch', pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Provide the path to your image file
image_path = 'C://Users//sujay//Downloads//McLaren.jpg'

# Convert the image to pencil sketch
image_to_pencil_sketch(image_path)