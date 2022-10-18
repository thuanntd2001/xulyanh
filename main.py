
import pygame
import cv2
from giaoDien import Menu as Menu,screen_width,screen_height,waiter
from duyetFile import duyet
import khuNhieu
import edge


if __name__ == '__main__':

    pygame.init()
    screen=pygame.display.set_mode((screen_width,screen_height))
    url="assert/bg1.jpeg"
    img=cv2.imread(url)

    pygame.display.set_caption("Xử lý ảnh")
    clock=pygame.time.Clock()
    clock=pygame.time.Clock()
    bg=pygame.image.load('assert/bg2.jpeg').convert()

    MENU=Menu(('Tải ảnh','Khử nhiễu','Phát hiện biên/cạnh ','Phát hiện khuôn mặt','Nhận diện khuôn mặt','Xem ảnh gốc'))
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
                        img=cv2.imread(url)
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()

                    elif MENU.state == 1:
                        # --- Khu nhieu ------
                        #imgKN=khuNhieu.medianBlur(img)
                        imgKN=khuNhieu.gaussianBlur(img)
                        cv2.imshow("Khu nhieu",imgKN)
                        waiter()
                        cv2.imwrite("output/denoise/khuNhieu.jpg",imgKN)
                    elif MENU.state == 2:
                        # --- phat hien canh ------
                        imgEdge=edge.canny(img)
                        cv2.imshow("edgeSobelx",edge.sobelX(img))
                        cv2.imshow("edgeSobely",edge.sobelY(img))
                        cv2.imshow("edgeCanny",imgEdge)

                        waiter()
                        cv2.imwrite("output/edge/timCanh_."+url[-2:0]+"jpg",imgEdge)
                    elif MENU.state == 3:# cai cua m o day
                        # --- phat hien khuon mat ------
                        #dong duoi la2 show cai hinh phat hien khuon mat ra!!!
                        #cv2.imshow("Phat hien khuon mat",cv2.resize(faceRecognition.faceDectection(img), (screen_width, screen_height)))
                        #nhung ma m bo r nen lam lai chut di ok ko??
                        print(url)
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