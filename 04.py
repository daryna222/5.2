import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
image = pygame.image.load("image.png")  # Завантажуємо зображення
screen.blit(image, (100, 100))  # Малюємо зображення на екрані
pygame.display.flip()



# rotated_image = pygame.transform.rotate(image, 45)  # Повертаємо зображення на 45 градусів
# screen.blit(rotated_image, (100, 100))  # Виводимо повернуте зображення
# pygame.display.flip()



# scaled_image = pygame.transform.scale(image, (200, 150))  # Змінюємо розмір зображення
# screen.blit(scaled_image, (100, 100))
# pygame.display.flip()



# background = pygame.Surface((800, 600))
# background.fill((255, 255, 255))  # Білий фон
# background.blit(image, (50, 50))  # Малюємо зображення на фоні
# screen.blit(background, (0, 0))
# pygame.display.flip()


# optimized_image = image.convert()  # Оптимізуємо зображення для швидшого рендерингу
# screen.blit(optimized_image, (100, 100))
# pygame.display.flip()


# sub_image = image.subsurface(pygame.Rect(0, 0, 50, 50))  # Обрізаємо частину зображення
# screen.blit(sub_image, (100, 100))
# pygame.display.flip()


# image.set_colorkey((255, 255, 255))  # Робимо білий колір прозорим
# screen.blit(image, (100, 100))
# pygame.display.flip()


# color = image.get_at((10, 10))  # Отримуємо колір пікселя на координаті (10, 10)
# print(color)  # Виводимо колір у консоль
