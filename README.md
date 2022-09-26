## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Classes](#classes)

## General info
Classic ping-pong game.

## Technologies
Project is written using the well-known pygame library.

## Classes
In particular at the beginning there are definitions of the two classes: Racket and Ball, which are written as
inheriting from the pygame.sprite.Sprite class. The classes are quite
simple, their methods take care of changing and checking the limit positions and determining (e.g. drawing
within a certain range) values of the speed of the ball.
