import cv2
import numpy as np

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilSketch(image):
    # Define Kernel
    kernel_sharpening = np.array([[0, -1,0],
                                  [-1,5, -1],
                                  [0, -1, 0]])
    # Sharpen an Image
    sharpened = cv2.filter2D(image, -1, kernel_sharpening)
    # Convert Image into Gray Scale
    image_gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
    # Blur Gray Image for smootheress
    img_smoothing = cv2.GaussianBlur(image_gray,(0,0),sigmaX=5,sigmaY=0) #smooting the inverted image.
    # Inverse an Image
    img_invert = cv2.bitwise_not(img_smoothing)
    # Apply Dodge on image for pencil Sketch
    final_img = dodgeV2(image_gray, img_invert)
    return final_img

# def main():
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         image = pencilSketch(frame)
#
#         cv2.imshow("Img", cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA))
#         key = cv2.waitKey(1)
#         if key == ord("q"):
#             break
    cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()