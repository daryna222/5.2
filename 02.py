import pygame

# Ініціалізація Pygame
pygame.init()

# Створення вікна
window = pygame.display.set_mode((500, 500))

# Колір лінії (RGB)
blue = (0, 0, 255)

# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Заливка фону
    window.fill((255, 255, 255))  # Білий фон
    
    # Малюємо лінію
    pygame.draw.line(window, blue, (100, 100), (400, 300), 5)
    
    # Оновлення дисплея
    pygame.display.flip()

# Закриття Pygame
pygame.quit()