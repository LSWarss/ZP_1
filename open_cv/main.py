import cv2
import imutils
import argparse


def detect(frame):
    bounding_box_cordinates, _ = HOGCV.detectMultiScale(
        frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y - 10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, f'Total Persons : {person-1}',
                (40, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
    cv2.imshow('output', frame)

    return frame


def detectByPathImage(path, output_path):
    image = cv2.imread(path)

    image = imutils.resize(image, width=min(1200, image.shape[1]))

    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def humanDetector(args):
    image_path = args["image"]

    if image_path is not None:
        print('[INFO] Opening Image from path.')
        detectByPathImage(image_path, args['output'])


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", default=None,
                           help="path to Image File ")
    arg_parse.add_argument("-o", "--output", type=str,
                           help="path to optional output image file")
    args = vars(arg_parse.parse_args())

    return args


if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    humanDetector(args)
0
