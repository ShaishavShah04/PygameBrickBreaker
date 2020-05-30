# CSE3130-Project-BrickBreaker
-
#### What is the program?

This is a simple remake of the popular game Atari-Breakout / Brick - Breaker. This is fully made in python using pygame. Upon launching the program, you will be greeted by a starting screen in which you have to press SPACE to start. For each block broken, your score will increase. The goal is to not let the ball touch the ground, as it will deduct one life. As soon as your life count (starting at 3) reaches 0, the game ends. This game does not have a "win" scenario, instead it has endless levels in which you can try your best to survive in!

#### Insight on planning behind the game!

The main component of planning behind this game was the collisions. A collision is viewed as the change in direction, however, these change in directions can be either in the X-axis or the Y-axis. If the ball bounces on the side of the brick, the ball will change its horizontal direction. If the ball bounces on the top/bottom of a block, then the ball will respond by changing the vertical direction! 

Image to describe:

<img src="Images/explain.png" >

