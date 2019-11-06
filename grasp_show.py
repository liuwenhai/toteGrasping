import cv2
import numpy as np
from math import *

def plot_grasp(img,grasp_pos,grasp_ang,grasp_wid,color=(0, 0, 255),thickness=1):
    num = grasp_pos.shape[0]
    for i in range(num):
        x,y = grasp_pos[i]
        angle = degrees(grasp_ang[i])
        width = grasp_wid[i]/2.
        plotGrasp(img,(x,y),angle,r1=width,color=color,thickness=thickness)
    return img

def plotGrasp(rgb,point,angle,r1=25,r2=7,color=(0, 0, 255),thickness=1):
    p1 = getEndPt(point,angle,r1)
    p2 = getEndPt(point,angle,-r1)
    p11 = getEndP(p1,angle,r2)
    p12 = getEndP(p1,angle,-r2)
    p21 = getEndP(p2,angle,r2)
    p22 = getEndP(p2,angle,-r2)
    # print cv2.__version__
    # pdb.set_trace()

    cv2.line(rgb, p1,p2, color = color, thickness=thickness,lineType=cv2.LINE_8)
    cv2.line(rgb, p11, p12, color = color, thickness=thickness,lineType=cv2.LINE_8)
    cv2.line(rgb, p21, p22, color = color, thickness=thickness,lineType=cv2.LINE_8)
    cv2.circle(rgb, (int(point[0]),int(point[1])), 1, color = color, thickness=-1,lineType=cv2.LINE_8)

def getEndP(point,angle,r):
    x0, y0 = point
    x1, y1 = x0 + r * sin(radians(angle)), y0 - r * cos(radians(angle))
    return (int(x1),int(y1))

def getEndPt(point,angle,r):
    x0, y0 = point
    x1, y1 = x0 + r * cos(radians(angle)), y0 + r * sin(radians(angle))
    return (int(x1),int(y1))



if __name__ == "__main__":
    color_dir = 'heightmap_color/000002.png'
    label_dir = 'label_gPPN/000002_good.npy'

    color_img = cv2.imread(color_dir)
    label = np.load(label_dir)
    colorshow = plot_grasp(color_img, label[:,:2], label[:,3], label[:,4], color=(255, 0, 0),
                           thickness=2)  # black,sort

    cv2.imshow('labelShow',color_img)
    cv2.waitKey()
