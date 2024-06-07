import cv2
import numpy as np

def count_dark_objects(threshold_value):
    # Read the image in grayscale
   
    image_path=r'C:\Users\Toshiba\Downloads\14.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding to segment dark objects
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Invert the binary image to highlight dark objects
    inverted_binary_image = cv2.bitwise_not(binary_image)

    # Find contours in the inverted binary image
    contours, _ = cv2.findContours(inverted_binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image (for visualization)
    original_image = cv2.imread(image_path)
    cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)

    # Count the number of dark objects
    dark_object_count = len(contours)

    # Display the original image with contours
    cv2.imshow('Contours', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return dark_object_count

# Example usage
image_path = 'dark_objects.jpg'  # Path to the image containing dark objects
threshold_value = 100  # Adjust based on the darkness of the objects

# Count dark objects in the image
dark_object_count = count_dark_objects(threshold_value)
dark_object_count=dark_object_count-4
print("Number of dark objects:", dark_object_count)