import pygame as pygame

# game basics

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
smallfont = pygame.font.SysFont('None', 48)
tinyfont = pygame.font.SysFont('Helvetica', 26)
bigfont = pygame.font.SysFont('None', 55)


# def

class Label:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.set(text)

    def set(self, text):
        self.text = smallfont.render(text, 1, pygame.Color("Blue"))
        size = w, h = self.text.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.surface = pygame.Surface(size)
        self.surface.blit(self.text, (0, 0))

# variables

text_surface_title = bigfont.render("TITLE OF THE GAME", True, 'Blue')
text_surface_by = tinyfont.render('By Yan', True, 'Blue')
# text_surface_by = pygame.transform.scale(text_surface_by, (60, 20))
# start_game_text = smallfont.render('Start', True, 'Blue')

#button class

lab1 = Label("Start", 20, 200)

def title_screen():
    screen.blit(text_surface_title, (20, 50))
    screen.blit(text_surface_by, (20, 100))

def loading_screen():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                if lab1.rect.collidepoint(mx, my):
                    lab1.set("You clicked me")

        screen.blit(lab1.surface, (20, 200))
        #if event.type == pygame.MOUSEBUTTONDOWN:

    title_screen()

    # .blit puts one surface onto another

    # draw all elements, update everything
    pygame.display.update()
    clock.tick(60)
