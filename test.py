import cv2


def main():
    stream = cv2.VideoCapture(0)
    while True:
        grapped, frame = stream.read()
        cv2.imshow("test", frame)
        key = cv2.waitKey(30)
        if key == ord("q") or key == ord("Q"):  # keyboard control
            break


if __name__ == "__main__":
    main()
