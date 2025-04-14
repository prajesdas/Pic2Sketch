import cv2
from pencilSketch import pencilSketch
from Cartonizing import cartoonizeImage

def main():
    source = 0
    cap = cv2.VideoCapture(source)
    cur_char = -1
    prev_char = 1
    window_name = "Cartoonize"  # The default window name

    while True:
        frame = cv2.imread("porche.jpg")
        # if ret == False:
        #     break
        frame = cv2.resize(frame, (0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)
        if c == 27:
            break

        if c > -1 and c != prev_char:
            cur_char = c
            cv2.destroyWindow(window_name)  # Close the previous window

        if cur_char == ord('s'):
            window_name = "Cartoonize"
            cv2.imshow(window_name, cartoonizeImage(frame))
        elif cur_char == ord('c'):
            window_name = "Pencil Sketch"
            cv2.imshow(window_name, pencilSketch(frame))
        else:
            cv2.imshow("Cartoonize", frame)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()