import cv2
import numpy as np
import requests

url = "http://192.168.1.23/photo.jpeg" 

while True:
    try:
        # Get the image from the ESP32-CAM
        response = requests.get(url)
        img_array = np.array(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        # Display the image
        cv2.imshow('ESP32-CAM', img)

        # Save the image
        filename = f"insect.jpg"
        cv2.imwrite(filename, img)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"Error: {e}")
        break

# Cleanup
cv2.destroyAllWindows()

# http://192.168.1.23/photo.jpeg