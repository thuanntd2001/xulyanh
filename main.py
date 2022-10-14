import pygame
import cv2
from giaoDien import Menu as Menu,screen_width,screen_height,waiter

from duyetFile import duyet
import khuNhieu


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
                        # --- duyet file ------
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()
                        run=True
                    if MENU.state == 0:
                        # --- duyet file ------
                        url=duyet()
                        img=cv2.imread(url)
                        cv2.imshow("Original",img)
                        print(url)
                        waiter()
                        run=True

                    elif MENU.state == 1:
                        # --- Khu nhieu ------
                        imgKN=khuNhieu.medianBlur(img)
                        cv2.imshow("Khu nhieu",imgKN)
                        waiter()
                        run=True
                    elif MENU.state == 2:
                        run=False
        screen.blit(bg,(0,0))
        MENU.update(screen)
        
        pygame.display.update()

        
        
        clock.tick(20)
       
    pygame.quit()