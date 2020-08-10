# Rainfall
# Demonstrates object animation
# Churchill - 9/24/2016

import pygame, random
from colour import Color as colour

pygame.init()
SIZE = [640, 480]

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

done = False

guy = pygame.image.load("rainfallguy.png").convert()

raindrops = []
for i in range(200):
    x = random.randrange(0, 641)
    y = random.randrange(0, 481)
    x_vel = random.randrange(8, 10)
    y_vel = x_vel * 3
    dropped = False
    point = [[x, y], [x+2, y+6], x_vel, y_vel, dropped]
    raindrops.append(point)

xdrop1 = 0
ydrop1 = 0
xdrop2 = 0
ydrop2 = 0
xdrop3 = 0
ydrop3 = 0
xdrop4 = 0
ydrop4 = 0


# velocities
xdrop1vel = 4
ydrop1vel = -2
xdrop2vel = 2
ydrop2vel = -4
xdrop3vel = -4
ydrop3vel = -2 
xdrop4vel = -2
ydrop4vel = -4


# Signallers
drop_land = False
splash_time = 0
pi = 22/7.0

def OnArc(x, y, h, k, r):
    if ((x-h)*(x-h) + (y-k)*(y-k)) <= r*r:
        return True
    else:
        return False
raindrops1 = raindrops[:int(len(raindrops)/2 - 50)]
raindrops2 = raindrops[int(len(raindrops)/2 - 50):]

while done == False:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill([int(i*255) for i in colour("White").rgb])
    arc = pygame.draw.arc(screen, [int(i*255) for i in colour("Darkred").rgb], [640/2-50, 480/2, 100, 100], 0, pi, 4)
    screen.blit(guy, [318, 253])
    for i in raindrops:
        if not i[4]:
            pygame.draw.line(screen, [int(i*255) for i in colour("Purple").rgb], i[0], i[1], 2)
            x_vel = i[2]
            y_vel = i[3]
            i[0][0] += x_vel
            i[0][1] += y_vel
            i[1][0] += x_vel
            i[1][1] += y_vel

            if i[0][0] > 640 or i[0][1] > 480:
                if i in raindrops1:
                    i[0][1] = random.randrange(-10, 480)
                    i[0][0] = random.randrange(-50, -10)
                else:
                    i[0][1] = random.randrange(-50, -10)
                    i[0][0] = random.randrange(-5, 641)
                i[1][0] = i[0][0] + 2
                i[1][1] = i[0][1] + 6
        if OnArc(i[1][0], i[1][1], 320, 290, 50):
            i[4] = True

        if i[4]:
            pygame.draw.circle(screen, [int(i*255) for i in colour("Purple").rgb], [i[1][0]+xdrop1, (i[1][1] -2)+ydrop1], 2)
            pygame.draw.circle(screen, [int(i*255) for i in colour("Purple").rgb], [i[1][0]+xdrop2, (i[1][1] -2)+ydrop2], 2)
            pygame.draw.circle(screen, [int(i*255) for i in colour("Purple").rgb], [i[1][0]+xdrop3, (i[1][1] -2)+ydrop3], 2)
            pygame.draw.circle(screen, [int(i*255) for i in colour("Purple").rgb], [i[1][0]+xdrop4, (i[1][1] -2)+ydrop4], 2)
            xdrop1 += xdrop1vel
            ydrop1 += ydrop1vel
            xdrop2 += xdrop2vel
            ydrop2 += ydrop2vel
            xdrop3 += xdrop3vel
            ydrop3 += ydrop3vel
            xdrop4 += xdrop4vel
            ydrop4 += ydrop4vel
            splash_time += 1
    
            if splash_time == 6:
                splash_time = 0
                i[4] = False
                if i in raindrops1:
                    i[0][1] = random.randrange(-10, 480)
                    i[0][0] = random.randrange(-50, -10)
                else:
                    i[0][1] = random.randrange(-50, -10)
                    i[0][0] = random.randrange(-5, 641)
                i[1][0] = i[0][0] + 2
                i[1][1] = i[0][1] + 6
                xdrop1 = 0
                ydrop1 = 0
                xdrop2 = 0
                ydrop2 = 0
                xdrop3 = 0
                ydrop3 = 0
                xdrop4 = 0
                ydrop4 = 0
            
        
        
    pygame.display.flip()

pygame.quit()
