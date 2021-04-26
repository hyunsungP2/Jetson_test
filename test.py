import cv2


def main():
    stream = cv2.VideoCapture(0, cv2.CAP_V4L2)
    while True:
        graped, img = stream.read()
        cv2.imshow("test", img)
        key = cv2.waitKey(30)
        if key == ord("q") or key == ord("Q"):  # keyboard control
            break


if __name__ == "__main__":
    main()
