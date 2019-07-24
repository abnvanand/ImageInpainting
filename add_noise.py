import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
def noisy(noise_typ,image):
    if noise_typ == "gauss":
        row,col,ch= image.shape
        mean = 0
        # var = 0.1
        sigma = 50
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        prob=0.05
        output = np.zeros(image.shape,np.uint8)
        thres = 1 - prob 
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = np.random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
        return output

def main():
    path = 'black_white/'
    files = os.listdir(path)
    os.mkdir("salt & pepper")
    path2=os.getcwd()+"/salt & pepper/"
    for index,file in enumerate(files):
        img=cv2.imread(path+file)
        out=noisy("s&p",img)
        # plt.imshow(out)
        # plt.title('Noisy image')
        # plt.show()
        cv2.imwrite(path2 +  str(index) +".jpg",out)

main()