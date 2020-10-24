## Challenge: Gamer W
## Category: Web

### Prompt:
> Can you figure out how to cheat the system? Grab his hat to prove your victory!

### Solution:
Using Cetus (similar to cheat engine), I was able to find and modify/freeze values associated with the player's health, gold, and damage. I was also able to find the value corresponding to the boss's health. Once I set it to 0, my character was trapped behind some obstacles:

![boxes](/GamerW1.png)

At first I tried to find a way to disable collisions so I could walk through the boxes, but I realized I had already found the value corresponding to the player's speed. By setting the speed super high, the player clipped through the wall and I was able to collect the boss's hat. The victory screen showed the flag:

![flag](/GamerW2.png)

### Flag:
tjctf{c3tus_del3tus_ur_m3ms_g0ne}