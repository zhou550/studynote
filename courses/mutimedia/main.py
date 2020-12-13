import cv2
import numpy as np
from math import sqrt
stride=10
def otsu_binarization(img: np.ndarray, th=128):
    max_sigma, max_t = 0, 0
    H, W = img.shape

    # determine threshold
    for _t in range(1, 255):
        v0 = img[np.where(img < _t)]
        u0 = np.mean(v0) if len(v0) else 0
        w0 = len(v0) / (H * W)
        v1 = img[np.where(img >= _t)]
        u1 = np.mean(v1) if len(v1) else 0
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 * (u0 - u1) ** 2
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t
    # Binarization
    print('Threshold >>', max_t)
    th = max_t
    out = img.copy()
    out[out < th] = 0
    out[out >= th] = 255
    return out
def blpf(img, D0, W=None, N=2, type='lp', filter='butterworth'):
    '''
    频域滤波器
    Args:
        img: 灰度图片
        D0: 截止频率
        W: 带宽
        N: butterworth和指数滤波器的阶数
        type: lp, hp, bp, bs即低通、高通、带通、带阻
        filter:butterworth、ideal、exponential即巴特沃斯、理想、指数滤波器
    Returns:
        imgback：滤波后的图像
    '''
    # 离散傅里叶变换
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    # 中心化
    dtf_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)  # 计算频谱中心
    mask = np.ones((rows, cols, 2))  # 生成rows行cols列的2纬矩阵
    for i in range(rows):
        for j in range(cols):
            D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if (filter.lower() == 'butterworth'):
                if (type == 'lp'):
                    mask[i, j] = 1 / (1 + (D / D0) ** (2 * N))
                elif (type == 'hp'):
                    mask[i, j] = 1 / (1 + (D0 / D) ** (2 * N))
                elif (type == 'bs'):
                    mask[i, j] = 1 / (1 + (D * W / (D ** 2 - D0 ** 2)) ** (2 * N))
                elif (type == 'bp'):
                    mask[i, j] = 1 / (1 + ((D ** 2 - D0 ** 2) / D * W) ** (2 * N))
                else:
                    assert ('type error')
            elif (filter.lower() == 'ideal'):  # 理想滤波器
                if (type == 'lp'):
                    if (D > D0):
                        mask[i, j] = 0
                elif (type == 'hp'):
                    if (D < D0):
                        mask[i, j] = 0
                elif (type == 'bs'):
                    if (D > D0 and D < D0 + W):
                        mask[i, j] = 0
                elif (type == 'bp'):
                    if (D < D0 and D > D0 + W):
                        mask[i, j] = 0
                else:
                    assert ('type error')
            elif (filter.lower() == 'exponential'):  # 指数滤波器
                if (type == 'lp'):
                    mask[i, j] = np.exp(-(D / D0) ** (2 * N))
                elif (type == 'hp'):
                    mask[i, j] = np.exp(-(D0 / D) ** (2 * N))
                elif (type == 'bs'):
                    mask[i, j] = np.exp(-(D * W / (D ** 2 - D0 ** 2)) ** (2 * N))
                elif (type == 'bp'):
                    mask[i, j] = np.exp(-((D ** 2 - D0 ** 2) / D * W) ** (2 * N))
                else:
                    assert ('type error')
    fshift = dtf_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])  # 计算像素梯度的绝对值
    img_back = np.abs(img_back)
    img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
    return img_back
img=cv2.imread("1233.png")
cv2.imshow("img",img)
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
b1=blpf(b,50)
g1=blpf(r,50)
cv2.imshow("b1",b1)
cv2.imshow("r1",g1)
img[:, :, 0]= b1
img[:, :, 1]= g1
cv2.imshow("IImg",img)
B=np.zeros((100,100),dtype=np.float)
sumValue=0
for i in range(r.shape[0]//stride):
    for j in range(r.shape[1]//stride):
        sum=0
        for k in range(stride):
            for l in range(stride):
                sum+=r.item(i*10+k,j*10+l)
        B[i][j]=sum/100
        sumValue=sumValue+B[i][j]
cv2.imshow("B",B)
cv2.waitKey(0)
avgValue=sumValue/((r.shape[0]//stride)*(r.shape[1]//stride))
for i in range(r.shape[0]//stride):
    for j in range(r.shape[1]//stride):
        if(B[i][j]<=avgValue):
            for k in range(stride):
                for l in range(stride):
                    r[i*10+k][j*10+l]=0
        else:
            attept=np.zeros((10,10))
            for k in range(stride):
                for l in range(stride):
                    attept[k][l]=r[i*10+k][j*10+l]
            # cv2.imshow("attept",attept)
            # cv2.waitKey(0)
            otsu_binarization(attept)
            for k in range(stride):
                for l in range(stride):
                    r[i*10+k][j*10+l]=attept[k][l]
cv2.imshow("r",r)
cv2.waitKey(0)

