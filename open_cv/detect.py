import cv2
import imutils


class Detector():

    def __init__(self) -> None:
        self.HOGCV = cv2.HOGDescriptor()
        self.HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame):
        bounding_box_cordinates, _ = self.HOGCV.detectMultiScale(
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

    def detectByPathImage(self, path, output_path):
        image = cv2.imread(path)

        image = imutils.resize(image, width=min(1200, image.shape[1]))

        result_image = self.detect(image)

        if output_path is not None:
            cv2.imwrite(output_path, result_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def humanDetector(self, args):
        image_path = args["image"]

        if image_path is not None:
            print('[INFO] Opening Image from path.')
            self.detectByPathImage(image_path, args['output'])
