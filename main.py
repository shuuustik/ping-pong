import pygame
from random import randint

pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Racket(pygame.sprite.Sprite):
    # class Racket inherits from class "Sprite" w Pygame.


    def __init__(self, color, width, height):
        # call the base class (Sprite) construstor first
        # thanks to the super() method we inherit all the elements of the base class
        super().__init__()

        # passing Racket the color, width and height, the background color and setting it to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw Racket as a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # get a rectangle (size) from the image object
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # checking the boundary condition
        if self.rect.y < 0:
           self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # checking the boundary condition
        if self.rect.y > 400:
           self.rect.y = 400



class Ball(pygame.sprite.Sprite):
    # class Ball inherits from class "Sprite" w Pygame.


    def __init__(self, color, width, height):
        # call the base class construstor
        super().__init__()

        # passing the color, size and transparency
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # drawing a ball (as a tectange)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # randomize speed
        self.velocity = [randint(4, 8), randint(-8, 8)]

        # getting the rectangle from the image object
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)



# define sizes and open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

racketA = Racket(WHITE, 10, 100)
racketA.rect.x = 20
racketA.rect.y = 200

racketB = Racket(WHITE, 10, 100)
racketB.rect.x = 670
racketB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# list of all seen child objects of the Sprite class
all_sprites_list = pygame.sprite.Group()

# adding both rackets and the ball to the list
all_sprites_list.add(racketA)
all_sprites_list.add(racketB)
all_sprites_list.add(ball)

# start the right block of the program
continuee = True

# used to control the number of frames per second (fps)
clock = pygame.time.Clock()

# the initial results of the players
scoreA = 0
scoreB = 0

# -------- main program loop -----------
while continuee:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # closing the window
            continuee = False

    # Racket movements up down arrows keys or w and s keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rakietkaA.moveUp(5)
    if keys[pygame.K_s]:
        rakietkaA.moveDown(5)
    if keys[pygame.K_UP]:
        rakietkaB.moveUp(5)
    if keys[pygame.K_DOWN]:
        rakietkaB.moveDown(5)

    # sprite list update
    all_sprites_list.update()

    # checking if the ball does not hit any wall
    # and the appropriate scoring of A point if it passes the A or B racket and hits the wall behind it
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    # checking the collision of the ball with the racketA or racketB
    if pygame.sprite.collide_mask(ball, racketA) or pygame.sprite.collide_mask(ball, racketB):
      ball.bounce()

    # drawing
    # black screen
    screen.fill(BLACK)
    # a thin line through the center of the pitch
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # drawing objects
    all_sprites_list.draw(screen)

    # displaying the results
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    # refreshing the entire screen
    pygame.display.flip()

    # 60 frames per second
    clock.tick(60)

# end
pygame.quit()