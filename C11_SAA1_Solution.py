# Import "pygame" module 
import pygame
# Import "time" module
import time
# Initialize "pygame"
pygame.init() 

# Create a screen of size (400, 300)
screen = pygame.display.set_mode((400,300))
# Set the "screen" title as "Counter" 
pygame.display.set_caption("Counter")

# RGB color combinations
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
YELLOW = (255,255,0)

carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False      
            pygame.quit()
    
        for i in range(1,21):
            screen.fill(DARKBLUE)
            
            font1 = pygame.font.Font(None, 50)
            text1 = font1.render("Counter:", 1, YELLOW)
            screen.blit(text1, (145,100))
            
            font2 = pygame.font.Font(None,100)
            text2 = font2.render(str(i), 1, WHITE)
            screen.blit(text2, (180,130))
            
            pygame.display.flip()
            time.sleep(2)
        
pygame.quit()