import pygame
import sys
import random
import time

class Game:
    def __init__(self):
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong")
        pygame.init()

        self.clock = pygame.time.Clock()

        

        # Ball
        

        self.ball = pygame.Rect((self.width/2 - 20, self.height/2 - 20, 20, 20))
        self.dirx = random.choice([-2, 2])
        self.diry = random.choice([-2, 2])

        # Players

        self.player1 = pygame.Rect((100, self.height/2 - 50, 20, 100))
        self.player2 = pygame.Rect((980, self.height/2 - 50, 20, 100))

        # Score
        self.player1points = 0
        self.player2points = 0

        self.textfor2 = f"Player 2: {self.player2points}"
        self.textfor1 = f"Player 1: {self.player1points}"
        self.font = pygame.font.SysFont("Arial", 50)

    def loop(self):
        while True:
            
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            self.text2 = self.font.render(self.textfor2, True, (255, 0, 0))
            self.text1 = self.font.render(self.textfor1, True, (255, 0, 0))
            self.screen.blit(self.text1, (170, 100))
            self.screen.blit(self.text2, (690, 100))


            pygame.draw.rect(self.screen, (255, 255, 255), self.player1)
            pygame.draw.rect(self.screen, (255, 255, 255), self.player2)

            pygame.draw.rect(self.screen, (255, 255, 255), self.ball)
            
            self.ball.move_ip(self.dirx, self.diry)

            if self.ball.y == self.height - 20 or self.ball.y == 0:
                self.diry *= -1

            if self.ball.x == self.width - 20 or self.ball.x == 0:
                self.points()

            if self.ball.colliderect(self.player1) or self.ball.colliderect(self.player2):
                self.dirx *= -1
                
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            
            # Player 1
            if keys[pygame.K_w]:
                self.player1.move_ip(0, -2)
                if self.player1.y < 0:
                    self.player1.y = 0
            if keys[pygame.K_s]:
                self.player1.move_ip(0, 2)
                if self.player1.y > self.height - 100:
                    self.player1.y = self.height - 100

            # Player 2
            if keys[pygame.K_UP]:
                self.player2.move_ip(0, -2)
                if self.player2.y < 0:
                    self.player2.y = 0
            if keys[pygame.K_DOWN]:
                self.player2.move_ip(0, 2)
                if self.player2.y > self.height - 100:
                    self.player2.y = self.height - 100 
                        

            pygame.display.update()

    def points(self):
        print(self.ball.x)
        if self.ball.x <= 0:
            self.player2points += 1
            self.textfor2 = f"Player 2: {self.player2points}"
            self.textfor1 = f"Player 1: {self.player1points}"
            self.ball.x = self.width/2 - 20 
            self.ball.y = self.height/2
            self.player1.y = self.height/2 - 50
            self.player2.y = self.height/2 -50
            time.sleep(1)
        if self.ball.x >= 1060:
            self.player1points += 1
            self.textfor2 = f"Player 2: {self.player2points}"
            self.textfor1 = f"Player 1: {self.player1points}"
            self.ball.x = self.width/2 - 20 
            self.ball.y = self.height/2
            self.player1.y = self.height/2 - 50
            self.player2.y = self.height/2 -50
            time.sleep(1)
        
    

        


Game().loop()