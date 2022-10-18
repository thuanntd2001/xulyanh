
import pygame
import cv2
import faceRecognition
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
                if event.key == pygame.K_RETURN:
                    if MENU.state == 5:
                        # --- show file ------
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()
                    if MENU.state == 3:
                        # --- phat hien khuon mat ------
                        cv2.imshow("Original",cv2.resize(faceRecognition.faceDectection(img), (screen_width, screen_height)))
                        print(url)
                        waiter()
                    if MENU.state == 0:

                        # --- duyet file ------
                        url=duyet()
                        img=cv2.imread(url)
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()

                    elif MENU.state == 1:
                        # --- Khu nhieu ------
                        imgKN=khuNhieu.medianBlur(img)
                        imgKN=khuNhieu.gaussianBlur(img)
                        cv2.imshow("Khu nhieu",imgKN)
                        waiter()
                        cv2.imwrite("output/denoise/khuNhieu_"+url[-2:0]+".jpg",imgKN)
                    elif MENU.state == 2:
                        # --- phat hien canh ------
                        imgEdge=edge.canny(img)
                        cv2.imshow("edge",imgEdge)
                        waiter()
                        cv2.imwrite("output/edge/timCanh_."+url[-2:0]+"jpg",imgEdge)
        screen.blit(bg,(0,0))
        MENU.update(screen)
        
        pygame.display.update()

        
        
        clock.tick(20)
       
    pygame.quit()