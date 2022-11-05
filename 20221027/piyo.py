import cv2
import numpy as np


p_original = np.float32([[380, 391], [590, 391], [322, 457], [668, 457], ])
p_trans = np.float32([[388, 391], [598, 391], [388, 580], [598, 580]])
M = cv2.getPerspectiveTransform(p_original, p_trans)


def preprocessing(pp):
    img = np.zeros([1024, 1024], dtype=np.uint8)
    for i, j in pp:
        img[284+int(j), int(i)] = 255
    img = cv2.warpPerspective(img, M, (1000, 1000))
    _, img = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(img)

    return centroids


if __name__ == '__main__':
    for i in range(100):
        pp = np.loadtxt(f"pp/pp_{i}.csv", delimiter=',')
        res = preprocessing(pp=pp)
        np.savetxt(f"pp3/pp_{i}.csv", res[1:], delimiter=',')
