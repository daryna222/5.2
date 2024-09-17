#багатокутник
import pygame


pygame.init() # ініціалізація Pygame


window = pygame.display.set_mode((500, 500)) # створення вікна


red = (255, 0, 0) # Колір (RGB)


points = [(100, 100), (300, 100), (200, 300)] # точки багатокутника (трикутник)

# основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
 
    window.fill((255, 255, 255))  # заливка фону. Білий фон
    
  
    pygame.draw.polygon(window, red, points, 0) # малюємо багатокутник
    
    
    pygame.display.flip() # оновлення дисплея


pygame.quit() # закриття Pygame
