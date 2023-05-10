# calculadora usando pygame
import pygame
width = 800  #Largura Janela
height = 650 #Altura Janela
WHITE = [255, 255, 255]
global result
result = ""

def load():
    global sys_font
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 50)

def check_click(x1,y1,w1,h1,x2,y2):
     return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1
    
def draw_screen(screen):
    screen.fill(WHITE)

    pygame.draw.rect(screen, (157, 157, 157), (50, 100, 700, 100))
    t = sys_font.render(result, False, WHITE)
    screen.blit(t, (85,125))
    
    pygame.draw.rect(screen, (157, 0, 0), (50, 200, 100, 100))
    t = sys_font.render("1", False, WHITE)
    screen.blit(t, (85,225))
    
    pygame.draw.rect(screen, (157, 0, 0), (150, 200, 100, 100))
    t = sys_font.render("2", False, WHITE)
    screen.blit(t, (185,225))
    
    pygame.draw.rect(screen, (157, 0, 0), (250, 200, 100, 100))
    t = sys_font.render("3", False, WHITE)
    screen.blit(t, (285,225))
    
    pygame.draw.rect(screen, (157, 0, 0), (50, 300, 100, 100))
    t = sys_font.render("4", False, WHITE)
    screen.blit(t, (85,325))
    
    pygame.draw.rect(screen, (157, 0, 0), (150, 300, 100, 100))
    t = sys_font.render("5", False, WHITE)
    screen.blit(t, (185,325))
    
    pygame.draw.rect(screen, (157, 0, 0), (250, 300, 100, 100))
    t = sys_font.render("6", False, WHITE)
    screen.blit(t, (285,325))
    
    pygame.draw.rect(screen, (157, 0, 0), (50, 400, 100, 100))
    t = sys_font.render("7", False, WHITE)
    screen.blit(t, (85,425))
    
    pygame.draw.rect(screen, (157, 0, 0), (150, 400, 100, 100))
    t = sys_font.render("8", False, WHITE)
    screen.blit(t, (185,425))
    
    pygame.draw.rect(screen, (157, 0, 0), (250, 400, 100, 100))
    t = sys_font.render("9", False, WHITE)
    screen.blit(t, (285,425))

    pygame.draw.rect(screen, (157, 0, 0), (150, 500, 100, 100))
    t = sys_font.render("0", False, WHITE)
    screen.blit(t, (185,525))

    pygame.draw.rect(screen, (157, 0, 0), (450, 400, 100, 100))
    t = sys_font.render("*", False, WHITE)
    screen.blit(t, (489,435))

    pygame.draw.rect(screen, (157, 0, 0), (550, 400, 100, 100))
    t = sys_font.render("/", False, WHITE)
    screen.blit(t, (585,432))

    pygame.draw.rect(screen, (157, 0, 0), (450, 300, 100, 100))
    t = sys_font.render("+", False, WHITE)
    screen.blit(t, (485,325))

    pygame.draw.rect(screen, (157, 0, 0), (550, 300, 100, 100))
    t = sys_font.render("-", False, WHITE)
    screen.blit(t, (585,325))

    pygame.draw.rect(screen, (0, 157, 0), (650, 400, 100, 100))
    t = sys_font.render("=", False, WHITE)
    screen.blit(t, (685,420))
    pass

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global result
    if mouse_buttons[0]:
        if check_click(50, 200, 100, 100, px_mouse, py_mouse):
            result = result + "1"
        if check_click(150, 200, 100, 100, px_mouse, py_mouse):
            result = result + "2"
        if check_click(250, 200, 100, 100, px_mouse, py_mouse):
            result = result + "3"
        if check_click(50, 300, 100, 100, px_mouse, py_mouse):
            result = result + "4"
        if check_click(150, 300, 100, 100, px_mouse, py_mouse):
            result = result + "5"
        if check_click(250, 300, 100, 100, px_mouse, py_mouse):
            result = result + "6"
        if check_click(50, 400, 100, 100, px_mouse, py_mouse):
            result = result + "7"
        if check_click(150, 400, 100, 100, px_mouse, py_mouse):
            result = result + "8"
        if check_click(250, 400, 100, 100, px_mouse, py_mouse):
            result = result + "9"
        if check_click(150, 500, 100, 100, px_mouse, py_mouse):
            result = result + "0"
        if check_click(450, 400, 100, 100, px_mouse, py_mouse):
            result = result + "*"
        if check_click(450, 300, 100, 100, px_mouse, py_mouse):
            result = result + "+"
        if check_click(550, 300, 100, 100, px_mouse, py_mouse):
            result = result + "-"
        if check_click(550, 400, 100, 100, px_mouse, py_mouse):
            result = result + "/"
        if check_click(650, 400, 100, 100, px_mouse, py_mouse):
            i = 0
            
            while result[i] != "*" or result[i] != "+":
                i += 1
            op1 = result[0:i]
            op2 = result[i+1::]
            if result[i] == "*":
                result = str(int(op1)*int(op2))
            if result[i] == "+":
                result = str(int(op1)+int(op2))
                           
def main_loop(screen):
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                    mouse_buttons = pygame.mouse.get_pressed()
                    px_mouse, py_mouse = pygame.mouse.get_pos()
                    mouse_click_down(px_mouse, py_mouse, mouse_buttons)
                    
        # Desenha objetos na tela 
        draw_screen(screen)
        # Pygame atualiza o seu estado
        pygame.display.update() 

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
