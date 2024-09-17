import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Будинок з героєм")

# Кольори
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
GREEN = (34, 139, 34)

# Завантаження зображення героя
hero_image = pygame.image.load('hero.png')  # Потрібен файл з вашим героєм
hero_image = pygame.transform.scale(hero_image, (100, 150))  # Масштабування зображення героя

# Функція для малювання будинку
def draw_house():
    # Фон неба
    screen.fill(BLUE)
    
    # Трава
    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))
    
    # Основа будинку
    pygame.draw.rect(screen, BROWN, (300, 300, 200, 200))
    
    # Дах будинку
    pygame.draw.polygon(screen, RED, [(275, 300), (400, 200), (525, 300)])
    
    # Вікно
    pygame.draw.rect(screen, WHITE, (350, 350, 50, 50))
    
    # Двері
    pygame.draw.rect(screen, WHITE, (420, 400, 50, 100))

# Головний цикл програми
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Малюємо будинок
    draw_house()
    
    # Додаємо зображення героя на екран
    screen.blit(hero_image, (600, 350))  # Розміщення героя
    
    # Оновлюємо екран
    pygame.display.flip()

# Закриваємо Pygame
pygame.quit()
sys.exit()
