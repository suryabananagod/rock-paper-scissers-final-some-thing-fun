import random
import pygame

class Button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False


class RpsGame():
    def __init__(self):
            pygame.init()
    
            self.screen = pygame.display.set_mode((960, 640))
            pygame.display.set_caption("RPS Smasher")
                
            self.bg = pygame.image.load("https://img.freepik.com/premium-vector/hands-playing-rock-paper-scissors-game-flat-design-style-vector-illustration_540284-598.jpg?w=2000")
            self.r_btn = pygame.text.pygame.text.load("rock").convert_alpha()
            self.p_btn = pygame.text.pygame.text.load("paper").convert_alpha()
            self.s_btn = pygame.text.pygame.text.load("scissors").convert_alpha()

            self.chose_rock = pygame.image.pygame.image.load("https://clipart-library.com/new_gallery/131-1313931_rock-paper-scissors.png").convert_alpha()
            self.chose_paper = pygame.image.pygame.image.load("https://static.vecteezy.com/system/resources/previews/012/604/090/non_2x/scissors-gesture-on-left-hand-for-concept-of-rock-paper-scissors-game-isolated-on-white-background-free-photo.jpeg").convert_alpha()
            self.chose_scissors = pygame.image.pygame.image.load("https://www.shutterstock.com/shutterstock/photos/160446689/display_1500/stock-vector-hand-sign-of-rock-paper-scissors-game-isolated-vector-on-white-background-160446689.jpg").convert_alpha()

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.r_btn, (20, 500))
            self.screen.blit(self.p_btn, (330, 500))
            self.screen.blit(self.s_btn, (640, 500))

            self.rock_btn = Button(30, 520, (30, 520), 300, 140)
            self.paper_btn = Button(340, 520, (340, 520), 300, 140)
            self.paper_btn = Button(640, 520, (640, 520), 300, 140)

            self.font = pygame.font.Font(('Splatch.ttf'), 90)
            self.text = self.font.render(f" "), True, (255, 255, 25)

            self.pl_score = 0
            self.pc_score = 0

    def player(self):
            if self.rock_btn.clicked(30):
                self.p_option = "rock"
                self.screen.blit(self.choose_rock, (120, 200))
            elif self.paper_btn.clicked(340):
                self.p_option = "paper"
                self.screen.blit(self.choose_paper, (120, 200))
            else:
                self.scissors_btn.clicked(640)
                self.p_option = "scissors"
                self.screen.blit(self.choose_scissors, (120, 200))

            return self.p_option

    def computer(self):
            self.pc_random_choice =" "
            option = ["rock", "paper", "scissors"]
            pc_choice = random.choice(list(option))
            if pc_choice == "rock":
                self.pc_random_choice = "rock"
                pc_choice = self.choose_rock
            elif pc_choice == "paper":
                self.pc_random_choice = "paper"
                pc_choice = self.choose_paper
            else:
                self.pc_random_choice = "scissors"
                pc_choice = self.choose_scissors
                pc_option = self.screen.blit(pc_choice, (600, 200))
            return pc_option