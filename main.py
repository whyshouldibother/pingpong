import pygame 
pygame.init()
class color:
    def __init__(self,fall):
        self.val=0
        self.fall=fall
    def flip(self):
        self.fall=-self.fall
    def increase(self):
        self.val+=self.fall
class pos:
    def __init__(self,val,acc):
        self.val=val
        self.acc=acc
    def flip(self):
        self.acc=-self.acc
    def increase(self):
        self.val+=self.acc
win=pygame.display.set_mode((1280,600))
pygame.display.set_caption("First Game")
run=True
width=250
height=4
y1=pos(0,5)
y2=pos(1,10)
x1=pos(0,5)
x2=pos(1,10)
r=color(15)
g=color(5)
b=color(1)
while run:
    win.fill((0,0,0))
    pygame.time.delay(25)
    x1.increase()
    x2.increase()
    y1.increase()
    y2.increase()
    if (x1.val>=1280-width or x1.val<=0): x1.flip()
    if (y1.val>=600-height or y1.val<=0): y1.flip()
    if (x2.val>=1280-width or x2.val<=0): x2.flip()
    if (y2.val>=600-height or y2.val<=0): y2.flip()
    r.increase()
    if(r.val==255 or r.val==0): r.flip()
    if(r.val%15==0):g.increase()
    if(g.val==255 or g.val==0): g.flip()
    if(r.val%5==0):b.increase()
    if(b.val==255 or b.val==0):b.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(win,(r.val,g.val,b.val),(x1.val,y1.val,width,height))
    pygame.draw.rect(win,(r.val,g.val,b.val),(x2.val,y2.val,width,height))
    pygame.display.update()