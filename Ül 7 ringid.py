import pygame
import random  # Juhuslike värvide jaoks

width, height = 640, 480  # Mängu akna suurus
base_radius = 10          # Väikseima ringi algraadius
MAX_CIRCLES = 10          # Maksimaalne ringide arv ekraanil

pygame.init()  # Käivitab pygame'i mooduli
screen = pygame.display.set_mode((width, height))  # Loob mänguakna
pygame.display.set_caption("Ringide mäng - Metsjärv")  # Akna nimi

clock = pygame.time.Clock()  # FPS-i kontrollimiseks

circles = []  # Siia salvestatakse kõik ringid (koordinaadid, värv, raadius)

running = True  # Mängutsükkel töötab seni kuni True
while running:
    for event in pygame.event.get():  # Loeb kõiki sündmusi
        if event.type == pygame.QUIT:  # Kui suletakse aken
            running = False  # Lõpetab tsükli

        if event.type == pygame.MOUSEBUTTONDOWN:  # Kui hiirt klikitakse
            x, y = pygame.mouse.get_pos()  # Võtab hiire asukoha

            color = (  # Genereeritakse juhuslik värv (RGB)
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

            # Arvutab ringi suuruse vastavalt mitu ringi juba olemas on
            radius = base_radius + len(circles) * 2

            # Lisab uue ringi listi (x, y, värv, raadius)
            circles.append((x, y, color, radius))

            # Kui ringe on rohkem kui lubatud maksimum
            if len(circles) > MAX_CIRCLES:
                circles.pop(0)  # Eemaldab kõige vanema ringi

    screen.fill((153, 232, 158))  # Täidab tausta rohelise värviga

    for circle in circles:  # Joonistab kõik ringid
        x, y, color, radius = circle
        pygame.draw.circle(screen, color, (x, y), radius, 2)

    pygame.display.flip()  # Uuendab ekraani
    clock.tick(60)  # Piirab mängu kiiruse 60 FPS peale

pygame.quit()  # Lõpetab pygame'i töö
