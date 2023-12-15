
from audioop import reverse
from math import radians
from tkinter import N
from turtle import Screen
import pygame
import sys
import random

pygame.init();# Khởi tạo Pygame
ScreenWidth, ScreenHeight = 500, 300;# Thiết lập kích thước của cửa sổ
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight));#Tạo cửa sổ 
pygame.display.set_caption("AdventureLife =) "); #Thiết lập cap cho màn hình

# Thiết lập màu sắc (RGB)
white = (211, 211, 211)
black = (255, 255, 255)
square_color1 = (0, 128, 255)
square_color2 = (255, 200, 50)
square_color3 = (0, 0, 0)
square_color4 = (12, 20, 150)

changed = False;
CellSize = 50;# Thiết lập thông số hình vuông
ScreenMargin = 10;#Thiết lập độ dày lề
LineMatrix = 5;# Khoẳng cách các Cell
NumberCell = 5;# So o ngang va doc 
row = 5; #Hàng
colum = 5; #Cột
Coordinates = 0; #Toạ độ
a = 0;
eventMove = 0;

MatrixTable = [
    [2, 0, 0, 0, 0],
    [2, 0, 2, 0, 0],
    [2, 0, 0, 0, 0],
    [2, 0, 2, 0, 0],
    [2, 0, 0, 0, 0],
]

def Swap(a,b):
    temp = a;
    a = b;
    b = temp;
    return a,b


def PrintMatrixTable(MatrixTable):
    for row in MatrixTable:
        for element in row:
            print(element, end=" ")
        print()
     
def MoveCell(MatrixTable, eventMove):
    if eventMove == 1 :  # Up
        for j in range(5):
            for i in range(1, 5):
                while i > 0 and MatrixTable[i][j] != 0:
                    if MatrixTable[i-1][j] == 0:
                        MatrixTable[i-1][j], MatrixTable[i][j] = MatrixTable[i][j], MatrixTable[i-1][j]
                        i -= 1
                    elif MatrixTable[i-1][j] == MatrixTable[i][j]:
                        MatrixTable[i-1][j] *= 2
                        MatrixTable[i][j] = 0
                        break
                    else:
                        print("Error: eventMove 1 (up) is wrong!")
                        break          
    elif eventMove == 2:  # Down
        for j in range(5):
            for i in reversed(range(4)):
                while i < 4 and MatrixTable[i][j] != 0:
                    if MatrixTable[i+1][j] == 0:
                        MatrixTable[i+1][j], MatrixTable[i][j] = MatrixTable[i][j], MatrixTable[i+1][j]
                        i += 1
                    elif MatrixTable[i+1][j] == MatrixTable[i][j]:
                        MatrixTable[i+1][j] *= 2
                        MatrixTable[i][j] = 0
                        break
                    else:
                        print("Error: eventMove 2 (down) is wrong!")
                        break
    elif eventMove == 3:  # Left
        for i in range(5):
            for j in range(1, 5):
                while j > 0 and MatrixTable[i][j] != 0:
                    if MatrixTable[i][j-1] == 0:
                        MatrixTable[i][j-1], MatrixTable[i][j] = MatrixTable[i][j], MatrixTable[i][j-1]
                        j -= 1
                    elif MatrixTable[i][j-1] == MatrixTable[i][j]:
                        MatrixTable[i][j-1] *= 2
                        MatrixTable[i][j] = 0
                        break
                    else:
                        print("Error: eventMove 3 (left) is wrong!")
                        break
    elif eventMove == 4:  # Right
        for i in range(5):
            for j in reversed(range(4)):
                while j < 4 and MatrixTable[i][j] != 0:
                    if MatrixTable[i][j+1] == 0:
                        MatrixTable[i][j+1], MatrixTable[i][j] = MatrixTable[i][j], MatrixTable[i][j+1]
                        j += 1
                    elif MatrixTable[i][j+1] == MatrixTable[i][j]:
                        MatrixTable[i][j+1] *= 2
                        MatrixTable[i][j] = 0
                        break
                    else:
                        print("Error: eventMove 4 (right) is wrong!")
                        break
    return MatrixTable

#PrintMatrixTable(MatrixTable);
#MatrixTable = MoveCell(MatrixTable,1);
#MatrixTable = MoveCell(MatrixTable,1);
#PrintMatrixTable = (MatrixTable);


                

def PrintCell(MatrixTable):
    for i in range(5):
        for j in  range(5):
            if MatrixTable[i][j] == 2:
                pygame.draw.rect(screen, square_color2, (ScreenMargin + j * CellSize , ScreenMargin + i* CellSize, CellSize, CellSize ));
            if MatrixTable[i][j] == 4:
                pygame.draw.rect(screen, square_color1, (ScreenMargin + j * CellSize , ScreenMargin + i* CellSize, CellSize, CellSize )); 
            if MatrixTable[i][j] == 8:
                pygame.draw.rect(screen, square_color3, (ScreenMargin + j * CellSize , ScreenMargin + i* CellSize, CellSize, CellSize ));
            if MatrixTable[i][j] == 16:
                pygame.draw.rect(screen, square_color4, (ScreenMargin + j * CellSize , ScreenMargin + i* CellSize, CellSize, CellSize ));    
def PrintBoard():
    temp = 0;
    for i in range(NumberCell + 1 ):
        pygame.draw.line(screen, black, (ScreenMargin + temp, ScreenMargin), (ScreenMargin + temp , ScreenMargin + NumberCell * CellSize ), LineMatrix);
        pygame.draw.line(screen, black, (ScreenMargin, ScreenMargin + temp), (ScreenMargin + NumberCell * CellSize , ScreenMargin + temp), LineMatrix);
        temp += CellSize;



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Handle the "W" key press event
                MatrixTable = MoveCell(MatrixTable, 1)
            elif event.key == pygame.K_s:
                # Handle the "S" key press event
                MatrixTable = MoveCell(MatrixTable, 2)
            elif event.key == pygame.K_a:
                # Handle the "A" key press event
                MatrixTable = MoveCell(MatrixTable, 3)
            elif event.key == pygame.K_d:
                # Handle the "D" key press event
                MatrixTable = MoveCell(MatrixTable, 4)

            
    #MatrixTable = (1,0,0,0,MatrixTable);
    # Xoa Man hinh
    screen.fill(white);
    # Vẽ hình vuông
    #pygame.draw.rect(screen, square_color1, (10, 10, CellSize, CellSize ));
    # Vẽ đường thẳng 
    PrintCell(MatrixTable);
    PrintBoard();
    # Lấy vị trí chuột
    MousePosX, MousePosY = pygame.mouse.get_pos();
    #print("X: ", MousePosX, " Y: ", MousePosY)
    # Cập nhật màn hình
    pygame.display.flip();
    # Giữ cửa sổ mở trong 60 frame mỗi giây
    pygame.time.Clock().tick(60);
