# CSE3130-Project-BrickBreaker

#### What is the program?

This is a simple remake of the popular game Atari-Breakout / Brick - Breaker. This is fully made in python using pygame. Upon launching the program, you will be greeted by a starting screen in which you have to press SPACE to start. For each block broken, your score will increase. The goal is to not let the ball touch the ground, as it will deduct one life. As soon as your life count (starting at 3) reaches 0, the game ends. This game does not have a "win" scenario, instead it has endless levels in which you can try your best to survive in!

#### Insight on planning behind the game!

The main component of planning behind this game was the collisions. A collision is viewed as the change in direction, however, these change in directions can be either in the X-axis or the Y-axis. If the ball bounces on the side of the brick, the ball will change its horizontal direction. If the ball bounces on the top/bottom of a block, then the ball will respond by changing the vertical direction! 

Image to describe:

<img src="Images/explain.png" width="200" >

In order to combat this problem, it is crucial to understand on what edge did the ball bounce on. In this program, we compared certain X and Y coordinates of the ball with the bricks to figure out which side they got hit on!

Refer to this picture for the brief explaination:

<img src="Images/explain2.png" width="200">

For the side collisions (right side collision in the image), I would test to see if the ball was completely in the pink shaded area. How? Notice the top left and bottom left corners of the ball have specific colors. In order to confirm the ball was in the shaded area, I would check if the **green** point was _above_ **the green line** and if the **yellow point** was _below_ the **yellow line**. Furthermore, we would make sure both of these points were touching the blocks right edge. If these conditions were met, I could be sure that the ball has touched the right edge of the block.

