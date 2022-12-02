import sys

import cv2
import numpy as np
from tqdm import tqdm


HW = 22
P = 5


def is_same(ij, r):
    for a in range(-(HW+P)//4, (HW+P)//4+1):
        for b in range(-(HW+P)//4, (HW+P)//4+1):
            if (ij[0]+a, ij[1]+b) in r:
                return True
    return False


if __name__ == '__main__':
    dir_in = sys.argv[1]
    dir_out = sys.argv[2]
    start = int(sys.argv[3])
    end = int(sys.argv[4])

    th = 0.987

    for i in tqdm(range(start, end)):
        img = cv2.imread(dir_in + f"{i}.bmp", 1)
        r_list = []
        result2 = np.zeros([1, 2], dtype=np.uint8)

        for j in range(1216):
            tracer_img = cv2.imread(f"./iwasa/{j}.bmp", 1)
            result = cv2.matchTemplate(img, tracer_img, cv2.TM_CCORR_NORMED)
            res_th_j, res_th_i = np.where(result > th)

            if res_th_i is None:
                continue
            else:
                res_th_i = res_th_i[:, np.newaxis]
                res_th_j = res_th_j[:, np.newaxis]
                tmp = np.hstack([res_th_i, res_th_j])
                result2 = np.vstack([result2, tmp])

        result2 = result2[1:]

        for n in tqdm(range(result2.shape[0])):
            i, j = result2[n, 0], result2[n, 1]
            if is_same((i, j), r_list):
                continue
            r_list.append((i, j))

        np.savetxt(dir_out + f"{i}.csv", r_list, delimiter=',', fmt="%d", header="(i, j) of upper left coordinates.")
