import cv2

def cartoonizeImage(img):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply median filter to the grayscale image
    blur = cv2.medianBlur(img_gray, ksize=5)
    # Detect edges in the image and threshold it
    edges = cv2.Laplacian(blur, cv2.CV_8U, ksize=5)

    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    sigma_color = 300
    sigma_space = 300
    size = 5

    # Apply bilateral filter the image multiple times
    img_small = cv2.bilateralFilter(img, size, sigma_color, sigma_space)
    # Add the thick boundary lines to the image using 'AND' operator
    dst = cv2.bitwise_and(img_small, img_small, mask=mask)

    return dst