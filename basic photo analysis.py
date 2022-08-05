import cv2


def resize():
    scale_percent=input("Scale percent:")
    width = int(img.shape[1] * int(scale_percent) / 100)
    height = int(img.shape[0] * int(scale_percent) / 100)
    dim = (width, height)
    img2 = cv2.resize(img,dim,interpolation = cv2.INTER_NEAREST)
    print("image resized")
    main()
    
def blurring():
    bulchoise=input("1 blur,2 median blur,3 gaussian blur:")
    if bulchoise=="1":
        k1=input("K size 1:")
        k2=input("K size 2:")
        img2=cv2.blur(img,(int(k1),int(k2)))
        cv2.imshow("Blur",img2)
        cv2.waitKey(0)
    elif bulchoise=="2":
        k=input("K size:")
        img2=cv2.medianblur(img,k)
        cv2.imshow("Blur",img2)
        cv2.waitKey(0)
    elif bulchoise=="3":
        k=input("K size:")
        img2=cv2.GaussianBlur(img, (5,5),0)
        cv2.imshow("Blur",img2)
        cv2.waitKey(0)
    else:
        print("Not found")
    save=input("For save image type y:")
    if save=="y":
        file=input("filename:")
        cv2.imwrite(file,img2)
    else:
        print("-------")
        
def color():
    colchoise=input("1 gray,2 lab,3 hsv:")
    if colchoise=="1":
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray",img2)
        cv2.waitKey(0)
    elif colchoise=="2":
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
        cv2.imshow("Lab",img2)
        cv2.waitKey(0)
    elif colchoise=="3":
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow("Hsv",img2)
        cv2.waitKey(0)
    else:
        print("Not found")
    save=input("For save image type y:")
    if save=="y":
        file=input("filename:")
        cv2.imwrite(file,img2)
    else:
        print("-------")

def contours():
    conchoise=input("1 canny,2 find contours and draw:")
    if conchoise=="1":
        tmin=input("treshold min:")
        tmax=input("treshold max:")
        img2=cv2.Canny(img,20,30)
        cv2.imshow("Canny",img2)
        cv2.waitKey(0)
    elif conchoise=="2":
        img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contours = np.zeros(img.shape)
        img2=cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
        cv2.imshow("Contours",)
        cv2.waitKey(0)
    else:
        print("Not found")
    save=input("For save image type y:")
    if save=="y":
        file=input("filename:")
        cv2.imwrite(file,img2)
    else:
        print("-------")
        
def main():        
    islem=input("1 resize options,2 blurring options,3 color options,4 contours \n")
    if islem=="1":
        resize()

    elif islem=="2":
        blurring()

    elif islem=="3":
        color()

    elif islem=="4":
        contours()
image=input("image:")
img=cv2.imread(image)
main()
