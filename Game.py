# Selena scj4ve and Joya jb7ft

import pygame
import gamebox
import random

"""
 We will be making a Space Invaders-type game for our final project. The user will press the up key to launch a
 bullet that will travel from the user's character at the bottom of the screen towards the top of the screen. There
 will be an enemy character that the user must try to hit with the bullets. If the bullet hits an enemy, the
 enemy will disappear and the user will receive 20 points. If the bullet does not hit an enemy, it will continue
 off of the top of the screen. The enemy will travel across the screen sideways and move towards the user after
 hitting a wall. We will have a start screen and end screen if the user gets 150 points or if the user's health
 reaches zero. The first optional feature we will incorporate is a moving enemy. We will include collectibles in the
 form of a coin that will generate every 10 seconds. We have three lives that represent health and will
 decrease by 1 if the enemy reaches the user bullet. Lastly, we will create three levels. If the user completes one
 level, they will move on to the second, etc. until completion of the game.
 """

camera = gamebox.Camera(800, 600)

score = 0
lives = 3
level_number = 1
ticker = 0
game_on = False
character = gamebox.from_color(400, 500, "green", 20, 20)

screen = pygame.display.set_mode((800, 600))
camera.display()

invader = gamebox.from_color(50, 50, "red", 20, 20)

bullet = gamebox.from_color(character.x, character.y, "yellow", 10, 10)
coin = gamebox.from_color(random.randrange(50, 750), character.y, "blue", 10, 10)


def tick(keys):
    """This function handles most of the game operations. It creates the black background and holds the start and end
screens. It also creates movement for the space bar, left, right, and up keys that control the character and bullet. It
prevents the character from moving off the screen and makes the invader move across the screen until it hits a wall, in
which case it resets to the opposite side and moves one row closer to the user. We also have it set so that when a
bullet touches the enemy, the enemy resets and the score increases. There is another touch action for when the character
gets a coin, it adds 10 points and waits a few seconds before regenerating. The levels are set by the user's score. For
each milestone, the enemy speed increases.
"""
    camera.clear('black')
    global game_on
    global score
    global lives
    global ticker
    global coin
    global level_number

    if not game_on:
        camera.draw(gamebox.from_text(400, 50, "Space Invader!", 40, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 100, "(There's only one)", 20, "Red", bold=True))
        camera.draw(gamebox.from_text(700, 50, "Selena Johnson (scj4ve)", 20, "Red", bold=True))
        camera.draw(gamebox.from_text(700, 75, "Joya Bhattacharyya (jb7ft)", 20, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 200, "Press up to shoot the enemies", 65, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 300, "Press space to begin", 65, "Red", bold=True))
        camera.draw(gamebox.from_text(400, 400, "Collect coins for more points", 65, "Red", bold=True))

    if pygame.K_SPACE in keys:
        game_on = True

    if game_on:
        if pygame.K_LEFT in keys:
            character.x -= 20
            if bullet.speedy == 0:
                bullet.x -= 20

        if pygame.K_RIGHT in keys:
            character.x += 20
            if bullet.speedy == 0:
                bullet.x += 20

        if pygame.K_UP in keys:
            bullet.speedy = -15

        bullet.move_speed()

        if bullet.y < 0:
            bullet.speedy = 0
            bullet.y = character.y
            bullet.x = character.x

        if character.x < 10:
            character.x = 10

        if character.x > 790:
            character.x = 790

        invader.x += 8
        if invader.x > 790:
            invader.x = 50
            invader.y += 50

        if bullet.touches(invader):
            invader.x = 50
            invader.y = 50
            score += 20

        if character.touches(coin):
            score += 10
            coin.x = 850

        if game_on:
            ticker += 1

        if ticker % 300 == 0 and coin.x == 850:
            coin = gamebox.from_color(random.randrange(50, 750), character.y, "blue", 10, 10)
            camera.draw(coin)

        if invader.y >= character.y:
            lives -= 1
            invader.x = 50
            invader.y = 50

        if lives <= 0:
            gamebox.pause()
            camera.draw(gamebox.from_text(400, 300, "You lose!", 50, "Red", bold=True))

        if score >= 50:
            invader.x += 16
            level_number = 2
        if score >= 100:
            invader.x += 32
            level_number = 3
        if score >= 150:
            gamebox.pause()
            camera.draw(gamebox.from_text(400, 300, "You win!", 50, "Red", bold=True))

    camera.draw(invader)
    camera.draw(bullet)
    camera.draw(character)
    camera.draw(gamebox.from_text(700, 550, "Score: " + str(score), 40, "Red", bold=True))
    camera.draw(gamebox.from_text(400, 550, "Lives: " + str(lives), 40, "Red", bold=True))
    camera.draw(gamebox.from_text(100, 550, "Level " + str(level_number), 40, "Red", bold=True))
    camera.draw(coin)
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
