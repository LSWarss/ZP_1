import cv2 as cv
import imutils


hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

image = cv.imread('street.jpeg')

image = imutils.resize(image, width=min(1200, image.shape[1]))

(regions, _) = hog.detectMultiScale(
    image, winStride=(4, 4), padding=(4, 4), scale=1.05)

counter = 0
for (x, y, w, h) in regions:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    counter += 1

print(f'On the image are {counter} person')

# Showing the output Image
cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
