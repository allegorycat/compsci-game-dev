import pygame as pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

text_surface_title = test_font.render("TITLE OF THE GAME", True, 'Blue')
text_surface_by = test_font.render("By Yan", True, 'Blue')
text_surface_by = pygame.transform.scale(text_surface_by, (60, 20))


def title_screen():
    screen.blit(text_surface_title, (20, 50))
    screen.blit(text_surface_by, (20, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            exit()
    title_screen()
    # .blit puts one surface onto another

    # draw all elements, update everything
    pygame.display.update()
    clock.tick(60)
