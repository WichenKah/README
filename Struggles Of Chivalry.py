#Team Knight
#Struggles of Chivalry
#Chandon, Wichen, Yassel
#Objective:

from gamelib import*#import game library

#objects and initial settings
game = Game (1000,700,"Struggles Of Chivalry")
bk = Image("Castle.jpg",game)
bk.resizeTo(game.width, game.height)
red=Image("redhulk.png",game)
slash=Animation("slash.png",11,game,1848/3,1920/4)
hero=Image("SmallKnight.gif",game)
hero.resizeTo(310,310)
hero2=Image("Range.png",game)
hero2.resizeTo(270,270)
backslash=Animation("backslash.png",10,game,1314/2,1730/5)
shoot=Animation("Shoot.png",6,game,741,1200/6)
shine=Animation("shine.png",12,game,450/3,600/4)
dslash=Animation("demon-awakening-effect-slash-1.png",6,game,1098/2,789/3)
f1=Font(black,48,blue,"Impact")
gm=Image("Game Over.png",game)
red.moveTo(800,350)
hero.moveTo(200,600)
hero2.moveTo(200,500)
shine.moveTo(800,400)
shine.resizeBy(100)
#Level 1 - game loop
while not game.over:
    game.processInput()
    bk.draw()
    red.draw()
    hero.draw()
    hero2.draw()
    shoot.x=hero2.x + 20
    shoot.y=hero2.y
    shoot.draw(False)
    slash.x = hero.x
    slash.y = hero.y
    slash.draw(False)
    backslash.x = hero.x - 180
    backslash.y = hero.y 
    backslash.draw(False)
    dslash.x=red.x- 50
    dslash.y=red.y
    dslash.draw(False)
    game.drawText(("Player 1 Health: ")+str(hero.health),50,50)
    game.drawText(("Player 2 Health: ")+str(hero2.health),50,75)
    game.drawText(("Enemy Health: ")+str(red.health),600,50)
    offscreen = True
    if keys.Pressed[K_a]:
        hero2.x-=7
    if keys.Pressed[K_d]:
        hero2.x+=7
    if keys.Pressed[K_w]:
        hero2.y-=7
    if keys.Pressed[K_s]:
        hero2.y+=7
    if keys.Pressed[K_h]:
        hero.x-=6
    if keys.Pressed[K_k]:
        hero.x+=6
    if keys.Pressed[K_u]:
        hero.y-=6
    if keys.Pressed[K_j]:
        hero.y+=6
    if keys.Pressed[K_o] and slash.visible == False:
        slash.visible = True
        slash.draw(False)
    if keys.Pressed[K_p] and backslash.visible == False:
        backslash.visible = True
        backslash.draw(False)
    if keys.Pressed[K_f] and shoot.visible == False:
        shoot.visible=True
        shoot.draw(False)
    if red.collidedWith(slash):
        red.health-=1
        red.moveTo(red.x+5,red.y+6)
    if red.collidedWith(backslash):
        red.health-=1
        red.moveTo(red.x-5,red.y-4)
    if red.collidedWith(shoot):
        red.health-=0.1
        red.moveTo(red.x+1,red.y)
    if red.collidedWith(hero)and dslash.visible == False:
        dslash.visible=True
        dslash.draw(False)
    if red.collidedWith(hero2)and dslash.visible == False:
        dslash.visible=True
        dslash.draw(False)
    if hero.collidedWith(dslash):
        hero.health-=5
        hero.x-=200
    if hero2.collidedWith(dslash):
        hero2.health-=10
        hero2.x-=200
    if red.health<1:
        game.over=True
    if hero.health<1:
        gm.draw()
        game.drawText(("To quit walk into the enemy again"),350,500)
    if hero2.health<1:
        gm.draw()
        game.drawText(("To quit walk into the enemy again"),350,500)
    if hero.health<-2:
        game.quit()
    if hero2.health<-2:
        game.quit()
    game.update(30)
game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    bk.draw()
    hero.draw()
    hero2.draw()
    shoot.x=hero2.x + 20
    shoot.y=hero2.y
    shoot.draw(False)
    slash.x = hero.x
    slash.y = hero.y
    slash.draw(False)
    backslash.x = hero.x - 180
    backslash.y = hero.y 
    backslash.draw(False)
    shine.draw()
    if keys.Pressed[K_a]:
        hero2.x-=7
    if keys.Pressed[K_d]:
        hero2.x+=7
    if keys.Pressed[K_w]:
        hero2.y-=7
    if keys.Pressed[K_s]:
        hero2.y+=7
    if keys.Pressed[K_h]:
        hero.x-=6
    if keys.Pressed[K_k]:
        hero.x+=6
    if keys.Pressed[K_u]:
        hero.y-=6
    if keys.Pressed[K_j]:
        hero.y+=6
    if keys.Pressed[K_o] and slash.visible == False:
        slash.visible = True
        slash.draw(False)
    if keys.Pressed[K_p] and backslash.visible == False:
        backslash.visible = True
        backslash.draw(False)
    if keys.Pressed[K_f] and shoot.visible == False:
        shoot.visible=True
        shoot.draw(False)
   
    game.update(30)

game.over=False
