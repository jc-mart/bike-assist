import cv2 as cv
import numpy as np

def grayscale():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Camera couldn't be opened.")
        exit()

    while True:
        # Captures frame-by-frame
        ret, frame = cap.read()

        # If frame is retrieved, ret is True
        if not ret:
            print("Can't recieve frame (stream end?). Aborting.")
            break

        # Grayscales input
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def flip():
    cap = cv.VideoCapture(0)

    # Specify video codec and create video writing object
    fourcc = cv.VideoWriter.fourcc(*'X264')
    # Filename, video codec, fps, resolution
    out = cv.VideoWriter('/home/carlitos/Downloads/output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Can't recieve frame (stream end?). Aborting.")
            break

        # Flip and write out
        frame = cv.flip(frame, 0)
        out.write(frame)
        cv.imshow('frame', frame)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    grayscale()
    # flip()
