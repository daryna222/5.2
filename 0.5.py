import pygame
pygame.init()

# Завантаження зображення
image = pygame.image.load("image.png")

# Масштабування зображення до нового розміру
new_size = (200, 200)
resized_image = pygame.transform.scale(image, new_size)

# Повернення зображення на 90 градусів
rotated_image = pygame.transform.rotate(image, 90)

# Встановлення кольору, який буде прозорим на зображенні
transparent_color = (255, 255, 255)
image.set_colorkey(transparent_color)

# Отримання коліру пікселя на певній позиції
pixel_color = image.get_at((10, 10))

# Відображення зображення на екрані
screen = pygame.display.set_mode((800, 600))
screen.blit(image, (0, 0))
pygame.display.update()

# Головний цикл програми
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()