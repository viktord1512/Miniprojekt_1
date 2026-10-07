import pygame
import time
import math


pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white
clock = pygame.time.Clock()

# Define the center of the clock
center=(320, 240)
'''I denne kode defineres en tuple som center, der indeholder x- og y-koordinaterne for centrum af uret.
Parameteren (320, 240) angiver at centrum af uret er placeret ved x=320 og y=240 pixels i vinduet.'''

def get_hand_endpoint(center, length, angle_degrees):
    rad = math.radians(angle_degrees - 90)
    x = center[0] + length * math.cos(rad)
    y = center[1] + length * math.sin(rad)
    return (x,y)
'''I denne kode defineres funktionen "get_hand_endpoint", som beregner slutpunktet for urets viser baseret på 
centrum, længde og vinkel i grader.
I koden hvor variablen rad defineres konverteres vinklen fra grader til radianer, da trigonometriske funktioner i Python bruger radianer.
x og y-koordinaterne for slutpunktet beregnes ved at tage "center's" koordinater og lægge længden og gange med cosinus og sinus af vinklen.
Hvor return funktionen returnerer slutpunktet som en tuple med x- og y-koordinater.'''

run_flag = True
while run_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
            '''I denne kode håndteres Pygame events, såsom lukningen af vinduet/fanen.
            Hvis brugeren lukker vinduet, sættes run_flag til False, som afslutter løkken.'''

    # Fetch the actual time from the computer
    current_time = time.time()
    hours = current_time // 3600 % 12 # Ved at dividere med 3600 får vi antallet af timer, og ved at tage modulo af 12 får vi timerne i 12-timers format.
    minutes = (current_time // 60) % 60 # Ved at dividere med 60 får vi antallet af minutter, og ved at tage modulo af 60 får vi minutterne i en time.
    seconds = current_time % 60 # Ved at tage modulo af 60 får vi antallet af sekunder i et minut.
    '''I denne kode hentes den aktuelle tid fra computeren, og timer, minutter samt sekunder overføres til deres variabler.'''

    # Calculate the angles
    second_angle = seconds * 6 # 360 /60 = 6
    minute_angle = minutes * 6 # 360 / 60 = 6
    hour_angle = (hours * 30) + (minutes * 0.5) # 360 / 12 = 30, 60/30 = 0.5
    '''I denne kode beregnes vinklerne for sekund-, minut- og timeviseren baseret på de aktuelle tidspunkter.'''

    # Draw a black circle
    pygame.draw.circle(screen, (0,0,0), center, (200), 0) 
    '''I denne kode tegnes der en sort cirkel i vinduet pygame med funktionen pygame.draw.circle.
    Det første parameter siger hvilken skærm/display der skal tegnes på,
    Det andet parameter siger hvilken farve cirklen skal have (RGB).
    Det tredje parameter er en tuple som angiver x- og y-koordinaterne for centrum af cirklen.
    Det fjerde parameter er radiusen af cirklen, som er 200 pixels her.
    Det femte parameter er tykkelsen af cirklen, som er 0 pixels her, som betyder at
    cirklen bliver fyldt helt ud.'''

    # Draw the second hand
    pygame.draw.aaline(screen, (255,0,0), center,
    get_hand_endpoint(center, 160, second_angle), 1)
    '''I denne kode tegnes der en rød linje i vinduet pygame med funktionen pygame.draw.line.
    Det første parameter siger hvilken skærm/display der skal tegnes på,
    Det andet parameter siger hvilken farve linjen skal have (RGB).
    Det tredje parameter er en tuple som angiver startpunktet for linjen (x,y).
    Det fjerde parameter er en tuple som angiver slutpunktet for linjen (x,y).
    Det femte parameter er tykkelsen af linjen, som er 1 pixel her.'''

    # Draw the minute hand
    pygame.draw.aaline(screen, (0,0,255), center,
    get_hand_endpoint(center, 150, minute_angle), 3)
    '''I denne kode tegnes der en grøn linje i vinduet pygame med funktionen pygame.draw.line.
    Det første parameter siger hvilken skærm/display der skal tegnes på,
    Det andet parameter siger hvilken farve linjen skal have (RGB).
    Det tredje parameter er en tuple som angiver startpunktet for linjen (x,y).
    Det fjerde parameter er en tuple som angiver slutpunktet for linjen (x,y).
    Det femte parameter er tykkelsen af linjen, som er 3 pixels her.'''

    # Draw the hour hand
    pygame.draw.aaline(screen, (0,0,255), center,
    get_hand_endpoint(center, 110, hour_angle), 3)
    '''I denne kode tegnes der en blå linje i vinduet pygame med funktionen pygame.draw.line.
    Det første parameter siger hvilken skærm/display der skal tegnes på,
    Det andet parameter siger hvilken farve linjen skal have (RGB).
    Det tredje parameter er en tuple som angiver startpunktet for linjen (x,y).
    Det fjerde parameter er en tuple som angiver slutpunktet for linjen (x,y).
    Det femte parameter er tykkelsen af linjen, som er 3 pixels her.'''

# Draw the hour marks
    for i in range(12):
        '''I denne kode tegnes der 12 time markeringer på uret ved hjælp af en for-løkke.
        Løkken kører 12 gange, en gang for hver time markering (0-11).'''

    # Calculate the angle for each hour mark
        angle_hour = math.radians(i * 30) 
        '''I denne kode beregnes vinklen for hver time markering på uret.
        Parameteren i * 30 beregner vinklen i grader for hver time markering, 
        hvor i er indekset for time markeringen (0-11). 
        Funktionen math.radians() konverterer vinklen fra grader til radianer, som er den enhed, 
        der bruges i trigonometriske funktioner i python.'''

    # Calculate the start positions
        start_x = center[0] + 180 * math.cos(angle_hour)
        start_y = center[1] + 180 * math.sin(angle_hour)
        '''I denne kode beregnes startpositionen for hver time markering på uret.
        Parameteren center[0] og center[1] henter x- og y-koordinaterne for centrum af uret.
        Parameteren 180 er afstanden fra centrum til startpunktet for time markeringen.
        Funktionen math.cos() og math.sin() beregner henholdsvis cosinus og sinus af vinklen,
        som bruges til at beregne x- og y-koordinaterne for startpunktet.'''

    # Calculate the end positions
        end_x = center[0] + 200 * math.cos(angle_hour)
        end_y = center[1] + 200 * math.sin(angle_hour)
        '''I denne kode beregnes slutpositionen for hver time markering på uret.
        Parameteren center[0] og center[1] henter x- og y-koordinaterne for centrum af uret.
        Parameteren 200 er afstanden fra centrum til slutpunktet for time markeringen.
        Funktionen math.cos() og math.sin() beregner henholdsvis cosinus og sinus af vinklen, 
        som bruges til at beregne x- og y-koordinaterne for slutpunktet.'''

        pygame.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 4)
        '''I denne kode tegnes der en lille hvid linje for hver time markering på uret ved hjælp af funmtionen pygame.draw.line.
        Det første parameter siger hvilken skærm/display der skal tegnes på,
        Det andet parameter siger hvilken farve linjen skal have (RGB).
        Det tredje parameter er en tuple som angiver startpunktet for linjen (x,y).
        Det fjerde parameter er en tuple som angiver slutpunktet for linjen (x,y).
        Det femte parameter er tykkelsen af linjen, som er 4 pixels her.'''

# Draw the minute marks
    for i in range(60):
        angle_min = math.radians(i * 6)
        '''I denne kode beregnes vinklen for hvert minut på uret.
        Funktionen math.radians() konverterer vinklen fra grader til radianer.
        Hvert minut svarer til 6 grader (360 grader / 60 minutter).'''

        start_x = center[0] + 190 * math.cos(angle_min)
        start_y = center[1] + 190 * math.sin(angle_min)
        '''I denne kode beregnes startpositionen for hver minut markering på uret.
        Parameteren center[0] og center[1] henter x- og y-koordinaterne for centrum af uret.
        Parameteren 190 er afstanden fra centrum til start punktet for minut markeringen.
        Funktionen math.cos() og math.sin() bruges til at beregne x- og y-koordinaterne for 
        minut markeringens startpunkt.'''

        end_x = center[0] + 200 * math.cos(angle_min)
        end_y = center[1] + 200 * math.sin(angle_min)
        '''I denne kode beregnes slutpunktet for hver minut markering på uret.
        Det er stort set denne samme kode med undtagelse af afstanden fra centrum til slutpunktet,
        som her er 200 pixels i stedet for 190 pixels for startpunktet som betyder at markeringen
        bliver 10 pixels lang.'''

        pygame.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 2)
        '''I denne kode tegnes linjen for minut markeringen på uret ved hjælp af pygame.draw.line() funktionen.
        Funktionen tager skærmen, farven (hvid), startpunktet, slutpunktet og tykkelsen af linjen som parametre.'''

# Draw the numbers on the clock
    font = pygame.font.SysFont("Georgia", 34)
    for i in range(1, 13):
        '''I denne kode beregnes vinklen for hvert tal på uret.
        Hvert tal svarer til en vinkel på 30 grader (360 grader / 12 tal) på uret.'''
        angle = math.radians(i * 30 - 90)
        x = center[0] + 155 * math.cos(angle)
        y = center[1] + 155 * math.sin(angle)
        '''I denne kode beregnes positionen for hvert tal på uret.
        Funktionen math.radians() konverterer vinklen fra grader til radianer, 
        hvilket er nødvendigt for at kunne bruge math.cos() og math.sin() funktionerne.
        Bestemmelsen af x- og y-koordinaterne er næsten en gentagelse af den tidligere kode for
        "minute markings" men hvor x og y-koordinaterne ikke har en start og slutpunkt, da tallene 
        blot placeres direkte på disse koordinater.'''
        text = font.render(str(i), True, (0, 0, 255))
        text_rect = text.get_rect(center=(x,y))
        screen.blit(text, text_rect)
        '''I denne kode tegnes tallene på uret.
        Funktionen font.render() bruges til at oprette en tekstoverflade med det givne tal "str(i)", skrifttype "True" og farve.
        Funktionen text.get_rect() bruges til at få rektanglet for tekstoverfladen, så tallene kan 
        placeres korrekt på uret.'''
    
# Draw the circle in the middle of the clock
    pygame.draw.circle(screen, (255,255,255), center, 10, 0)

# Draw a outline around the clock
    pygame.draw.circle(screen, (0,0,255), center, 200, 4)

    # Refresh the screen and limit the loop speed
    pygame.display.flip()
    clock.tick(60)
    '''I denne kode opdateres skærmen med pygame.display.flip() og loophastigheden begrænses til 60 FPS med clock.tick(60).'''

pygame.quit()
'''I denne kode afsluttes pygame korrekt ved at kalde på pygame.quit() funktionen.'''
