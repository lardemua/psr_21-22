#!/usr/bin/env python
import cv2
import numpy as np


def main():
    # Load image
    image_rgb = cv2.imread('../images/atlas2000_e_atlasmv.png')

    # EX 2 a) and b)

    # convert rgb to gray
    # image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    # Alternative 1: Opencv Thresholding
    # retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    #
    # # Alternative 2: Numpy Thresholding
    # print(type(image_gray))
    # print(image_gray.shape)
    # print(image_gray.dtype)
    #
    # image_np_thresholded = image_gray > 128
    #
    # print(type(image_np_thresholded))
    # print(image_np_thresholded.shape)
    # print(image_np_thresholded.dtype)
    # image_np_thresholded = image_np_thresholded.astype(np.uint8)
    #
    # # Display image
    # window_name = 'my_window'
    # cv2.imshow(window_name, image_thresholded)
    #
    # np_window_name = 'my_np_window'
    # cv2.imshow(np_window_name, image_np_thresholded)
    # cv2.waitKey(0)

    # EX 2 a) and b)
    image_b, image_g, image_r = cv2.split(image_rgb)

    _, image_b_thresholded = cv2.threshold(image_b, 128, 255, cv2.THRESH_BINARY)
    _, image_g_thresholded = cv2.threshold(image_g, 128, 255, cv2.THRESH_BINARY)
    _, image_r_thresholded = cv2.threshold(image_r,128, 255, cv2.THRESH_BINARY)

    image_output = cv2.merge((image_b_thresholded, image_g_thresholded, image_r_thresholded))

    # Display image
    window_name = 'my_window'
    cv2.imshow(window_name, image_output)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
