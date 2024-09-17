import pygame

# Ініціалізація Pygame
pygame.init()

# Створення вікна
window = pygame.display.set_mode((500, 500))

# Кольори (RGB)
green = (0, 255, 0)
purple = (128, 0, 128)

# Точки багатокутника
polygon_points = [(150, 150), (350, 150), (400, 300), (100, 300)]

# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Заливка фону
    window.fill((255, 255, 255))  # Білий фон
    
    # Малюємо багатокутник
    pygame.draw.polygon(window, green, polygon_points, 0)
    
    # Малюємо лінію через багатокутник
    pygame.draw.line(window, purple, (150, 150), (400, 300), 5)
    
    # Оновлення дисплея
    pygame.display.flip()

# Закриття Pygame
pygame.quit()