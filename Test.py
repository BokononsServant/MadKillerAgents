import pygame

pygame.init() 

#create the screen
window = pygame.display.set_mode((640, 480)) 
pygame.draw.line(window, (255, 255, 255), (0, 0), (30, 50))
#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print (event)

##width   = screen.getmaxyx()[1]
##height  = screen.getmaxyx()[0]
##size    = width*height
##char    = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
##b       = []
## 
##curses.curs_set(0)
##curses.start_color()
##curses.init_pair(1,0,0)
##curses.init_pair(2,1,0)
##curses.init_pair(3,3,0)
##curses.init_pair(4,4,0)
##screen.clear
##for i in range(size+width+1): b.append(0)
## 
##while 1:
##        for i in range(int(width/9)): b[int((random.random()*width)+width*(height-1))]=65
##        for i in range(size):
##                b[i]=int((b[i]+b[i+1]+b[i+width]+b[i+width+1])/4)
##                color=(4 if b[i]>15 else (3 if b[i]>9 else (2 if b[i]>4 else 1)))
##                if(i<size-1):   screen.addstr(  int(i/width),
##                                                i%width,
##                                                char[(9 if b[i]>9 else b[i])],
##                                                curses.color_pair(color) | curses.A_BOLD )
## 
##        screen.refresh()
##        screen.timeout(30)
##        if (screen.getch()!=-1): break
## 
##curses.endwin()
