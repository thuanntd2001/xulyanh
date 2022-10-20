
import pygame
import cv2
from giaoDien import Menu as Menu,screen_width,screen_height,waiter
from duyetFile import duyet
import khuNhieu
import edge
import faceDetect


if __name__ == '__main__':

    pygame.init()
    screen=pygame.display.set_mode((screen_width,screen_height))
    url="assert/bg1.jpeg"
    img=cv2.imread(url)

    pygame.display.set_caption("Xử lý ảnh")
    clock=pygame.time.Clock()
    clock=pygame.time.Clock()
    bg=pygame.image.load('assert/bg2.jpeg').convert()

    MENU=Menu(['Tải ảnh','Khử nhiễu','Phát hiện biên/cạnh ','Phát hiện khuôn mặt','Nhận diện khuôn mặt','Xem ảnh gốc'])
    screen=pygame.display.set_mode((screen_width,screen_height))

    run=True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            MENU.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # trong nay la xu ly giao dien
                    
                    if MENU.state == 0:# la cai dau tien 'tai anh'

                        # --- duyet file ------
                        url=duyet()
                        MENU.items[0]= 'URL: '+ url
                        img=cv2.imread(url)
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()

                    elif MENU.state == 1:
                        # --- Khu nhieu ------
                        imgKN_0=khuNhieu.gaussianBlur(img)

                        imgKN_1=khuNhieu.medianBlur(img)
                        imgKN_2=khuNhieu.gaussianBlur(imgKN_1)
                        cv2.imshow("Khu nhieu",imgKN_2)
                        waiter()

                        cv2.imwrite("output/denoise/khuNhieu.jpg",imgKN_2)
                        cv2.imwrite("output/denoise/khuNhieu_median.jpg",imgKN_1)
                        cv2.imwrite("output/denoise/khuNhieu_gauss.jpg",imgKN_0)
                    elif MENU.state == 2:
                        # --- phat hien canh ------
                        imgGray=edge.grayscale(img)
                        imgEdge=edge.canny(imgGray)
                        img1=edge.sobelX(imgGray)
                        img2=edge.sobelY(imgGray)

                        cv2.imshow("edgeCanny",imgEdge)

                        waiter()
                        cv2.imwrite("output/edge/timCanh_edgeSobelX.jpg",img1)
                        cv2.imwrite("output/edge/timCanh_edgeSobelY.jpg",img2)
                        cv2.imwrite("output/edge/timCanh_edgeCanny.jpg",imgEdge)

                    elif MENU.state == 3:# cai cua m o day
                        # --- phat hien khuon mat ------
                        detectImg=faceDetect.faceDetect(img)
                        cv2.imshow("faceDetect",detectImg)
                        cv2.imwrite("output/faceDetect/Faces.jpg",detectImg)

                        waiter()
                    elif MENU.state == 4:# cai nay la nhan dien khuon mat. m biet dung xml ko khoi cai database
                        # --- phat hien khuon mat ------
                        #dong duoi la2 show cai hinh phat hien khuon mat ra!!!
                        #cv2.imshow("Phat hien khuon mat",cv2.resize(faceRecognition.faceDectection(img), (screen_width, screen_height)))
                        #nhung ma m bo r nen lam lai chut di ok ko??
                        print(url)
                        waiter()
                    elif MENU.state == 5:
                        # --- show file ------
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()

        screen.blit(bg,(0,0))
        MENU.update(screen)
        
        pygame.display.update()

        
        
        clock.tick(20)
       
    pygame.quit()