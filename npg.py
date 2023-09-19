import pygame
pygame.init()


class start:
    def _init_():
        import pygame
        pygame.init()
        return pygame.init()
    def _world_(x: int, y: int, name: str):
        
        dis = pygame.display.set_mode((x, y))
        pygame.display.set_caption(name)
        return dis
    def _start_(file: str):
        import os 
        a = 'start ' + file
        os.system(a)
        return os.system(a)
    def _game_():
        import subprocess
        module = "pygame"
        subprocess.run(["pip", "install", module, "--upgrade"])

class new:

    def _world_(x: int, y: int, name: str):
        dis = pygame.display.set_mode((x, y))
        pygame.display.set_caption(name)
        return dis
    def _list_(name: str):
        inf = open(name,'w')
        inf.close
    def costume(file: str, px: int):
        sprite = pygame.image.load(file)
        sprite = pygame.transform.scale(sprite, (px, px))
        return sprite
    def costumes(files: list, px: int):
        costumes = []
        for i in files:
            sprite = pygame.image.load(i)
            sprite = pygame.transform.scale(sprite, (px, px))
            costumes += [sprite]
        return costumes
class draw:
    def sprite(x: int, y: int, px: int, file: str, dis):
        
        sprite = pygame.image.load(file)
        sprite = pygame.transform.scale(sprite, (px, px))
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
    def animation(x: int, y: int, costumes: list, nymder: int, px: int, dis):
        sprite = costumes[nymder]
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
    def costume(x: int, y: int, costume, px: int, dis):
        sprite = costume
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
    def back_picture(file: str, dis, window_size, x = 0, y = 0):
        
        background_picture = pygame.image.load(file)
        background_picture = pygame.transform.scale(background_picture, window_size)
        dis.blit(background_picture, (x, y))
        return background_picture
    def back_collor(dis, collor):
        dis.fill(collor)
        return
    class figure:
        def rect(x: int, y: int, h: int, w: int, dis, collor):
            xx = x - (h / 2)
            yy = y - (w / 2)
            pygame.draw.rect(dis, collor, [xx, yy, h, w])
            return
    def matrix(l: list, px: int, dis):
        for i in l:
            x = i[0]
            y = i[1]
            pict = i[2]
            if pict != 'Empty':
                global sprite
                sprite = pygame.image.load(pict)
                sprite = pygame.transform.scale(sprite, (px, px))
                xx = x - (px / 2)
                yy = y - (px / 2)
                dis.blit(sprite, (xx, yy))
        return












class keys:
    def _quit_():
        for i in pygame.event.get():                            
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
        return 
    
    def ULDR(k: str):
        kk = '0'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            kk = 'L'
        elif keys[pygame.K_RIGHT]:
            kk = 'R'
        elif keys[pygame.K_DOWN]:
            kk = 'D'
        elif keys[pygame.K_UP]:
            kk = 'U'
        if k == kk:
            return True
        return False
    def WASD(k: str):
        kk = '0'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            kk = 'W'
        elif keys[pygame.K_a]:
            kk = 'A'
        elif keys[pygame.K_s]:
            kk = 'S'
        elif keys[pygame.K_d]:
            kk = 'D'
        if k == kk:
            return True
        return False
class TIME:
    def time():
        import time
        return 
    def clock():
        
        fps_clock = pygame.time.Clock()
        return fps_clock
    def tick(fps: int, fps_clock):
        fps_clock.tick(fps)
        return
    def _stop_(second: float):
        import time
        time.sleep(second)
        return
class warning:
    def border(x0: int, y0: int, x1: int, y1: int, x: int, y: int):
        if x < x0:
            a = True
        else:
            a = False
        if x > x1:
            b = True
        else:
            b = False
        if y < y0:
            c = True
        else:
            c = False
        if y > y1:
            d = True
        else:
            d = False
        card = [a, b, c, d]
        return card
    def wall(side: str, coord: int, f: int, t: int, x: int, y: int):
        if side == 'x':
            if x == coord:
                for i in range(f, t):
                    if y == i:
                        return True
            return False
        if side == 'y':
            if y == coord:
                for i in range(f, t):
                    if x == i:
                        return True
            return False
    def collision(file: str, x: int, y: int, x2: int, y2: int):
        
        inf = open(file + '.ftnpg')
        a_l = []

        for lines in inf:
            c = ''
            a_l1 = []
            line = lines.split()
            for i in str(line):
                
                c += str(i)
                c = c.replace(',','')
                c = c.replace('[','')
                c = c.replace(']','')
                c = c.replace("'",'')
                if len(c) > 1:
                    
                    a_l1 += [int(c)]
                    c = ''
            a_l += [a_l1]
        
        
        
        
        
        
        
        yy = y
        
        
        for i in range(len(a_l)):
            xx = x
            for j in range(len(a_l[i-1])):
                
                if int(a_l[i-1][j-1]) > 1:
                    
                    if (x2 < xx + 30 and x2 > xx - 30) and (y2 < yy + 30 and y2 > yy - 30):

                        return True
                xx += 32
            yy += 32
        return False




















class display:
    def message(msg: str, collor, font, a: int, b: int, dis):
        mesg = font.render(msg, True, collor)
        dis.blit(mesg, [a,b])
        return
    def update():
        pygame.display.update()
        return pygame.display.update()
class font:
    def fonts(num: int, a: int):
        font1 = pygame.font.SysFont('bahnschrift', a)
        font2 = pygame.font.SysFont('comicsansms', a)
        font3 = pygame.font.SysFont('arial', a)
        fonts = [font3, font2, font1]
        return fonts[num]
    def font(name: str, a: int):
        font = pygame.font.SysFont(name, a)
        return font
class matrix:
    
    def create(file: str, l: list, x: int, y: int):
        
        inf = open(file + '.ftnpg')
        a_l = []

        for lines in inf:
            c = ''
            a_l1 = []
            line = lines.split()
            for i in str(line):
                
                c += str(i)
                c = c.replace(',','')
                c = c.replace('[','')
                c = c.replace(']','')
                c = c.replace("'",'')
                if len(c) > 1:
                    
                    a_l1 += [int(c)]
                    c = ''
            a_l += [a_l1]
        
        
        coard = []
        
        '''[[-1,1,-1],[1,1,1],[1,-1,1]]'''      ###    Пример возможного списка ag_l    ###
        xx = x
        yy = y
        for i in a_l:
            xx = x
            for j in i:
                coard += [[xx, yy]]
                xx += 32
            yy += 32
        
        coard_draw = []
        coard_draw1 = []
        yy = y
        for i in range(len(a_l)):
            coard_draw = []
            xx = x
            for j in range(len(a_l[i-1])):
                coard_draw = []
                
                for u in l:
                    coard_draw = []
                    if u[0] == a_l[i][j]:
                        coard_draw1 += [[xx, yy, u[1]]]
                        
                    
                xx += 32
            yy += 32
            coard_draw += coard_draw1
        return coard_draw

        
        






































    
        

    


