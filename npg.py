import pygame
pygame.init()


# создаём класс start
class start:
    
    # Создаём функцию _init_
    def _init_():
        import pygame
        pygame.init()
        return pygame.init()
        
    # Создаём функцию _world_
    # Которая создаёт игровое окно, с высотой e, ширеной x, и названием name
    def _world_(x: int, y: int, name: str):
        dis = pygame.display.set_mode((x, y))
        pygame.display.set_caption(name)
        return dis
        
    # Создаём функцию _start_ которая запускает файл file
    def _start_(file: str):
        import os 
        a = 'start ' + file
        os.system(a)
        return os.system(a)
        
    # Создаём функцию _game_  которая скачивает модуль pygame
    def _game_():
        import subprocess
        module = "pygame"
        subprocess.run(["pip", "install", module, "--upgrade"])


# создаём класс new
class new:
    
    # Создаём функцию _world_
    # Которая создаёт игровое окно, с высотой e, ширеной x, и названием name
    def _world_(x: int, y: int, name: str):
        dis = pygame.display.set_mode((x, y))
        pygame.display.set_caption(name)
        return dis
        
    # Создаём функцию _list_ которая создоёт файл name
    def _list_(name: str):
        inf = open(name,'w')
        inf.close
        
    # Создаём функцию costume
    # Которая создоёт новый костюм с помощю файла file c расширением .png и размером px (в пиксилях)
    def costume(file: str, px: int):
        sprite = pygame.image.load(file)
        sprite = pygame.transform.scale(sprite, (px, px))
        return sprite
        
    # Создаём функцию costumes
    # Которая создоёт новый костюмы с помощю списка файлов files c расширением .png и размером px (в пиксилях)
    def costumes(files: list, px: int):
        costumes = []
        for i in files:
            sprite = pygame.image.load(i)
            sprite = pygame.transform.scale(sprite, (px, px))
            costumes += [sprite]
        return costumes


# создаём класс draw
class draw:
    
    # Создаём функцию sprite
    # Которая отрисовывает квадратную картинку на экране(его надо указать в dis) с помощю файла file c расширением .png, с размером px (в пиксилях), на координатах x,y
    def sprite(x: int, y: int, px: int, file: str, dis):
        sprite = pygame.image.load(file)
        sprite = pygame.transform.scale(sprite, (px, px))
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
        
    # Создаём функцию animation
    ''' 
    Которая отрисовывает квадратную картинку на экране(его надо указать в dis) с помощю списка файлов costumes c расширением .png, 
    номер нужной картинки из списка costumes надо указать в nymder, 
    с размером px (в пиксилях), на координатах x,y
    '''
    def animation(x: int, y: int, costumes: list, nymder: int, px: int, dis):
        sprite = costumes[nymder]
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
        
    # Создаём функцию costume
    # Которая отрисовывает квадратную картинку на экране(его надо указать в dis) с помощю переменной costume(которая создаётся в функции new.costume), с размером px (в пиксилях), на координатах x,y
    def costume(x: int, y: int, costume, px: int, dis):
        sprite = costume
        xx = x - (px / 2)
        yy = y - (px / 2)
        dis.blit(sprite, (xx, yy))
        return sprite
        
    # Создаём функцию back_picture
    # Которая отрисовывает квадратную картинку на экране(его надо указать в dis) с помощю файла file c расширением .png, с размером window_size пример((400, 400)), на координатах x,y (по умолчанию 0)
    def back_picture(file: str, dis, window_size, x = 0, y = 0):
        background_picture = pygame.image.load(file)
        background_picture = pygame.transform.scale(background_picture, window_size)
        dis.blit(background_picture, (x, y))
        return background_picture

    # Создаём функцию back_collor
    # Которая заполняет весь экран (dis) цветом (collor)
    def back_collor(dis, collor):
        dis.fill(collor)
        return

    # Создаём функцию matrix
    # Которая отрисовывает множество картинок с размером px который по умолчянию 32 пиксиля с помощю списка l который можно создать с помошью функции matrix.create и отображает на фоне dis
    def matrix(l: list, px = 32, dis):
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

    
    # создаём класс figure
    class figure:
        
        # Создаём функцию rect
        # Которая отрисовывает прямоугольный участок на экране(его надо указать в dis) с высотой w и ширеной h на координатах x,y и цветом collor
        def rect(x: int, y: int, h: int, w: int, dis, collor):
            xx = x - (h / 2)
            yy = y - (w / 2)
            pygame.draw.rect(dis, collor, [xx, yy, h, w])
            return


# создаём класс keys
class keys:
    
    # Создаём функцию _quit_ которая при нажатие на поле закрыть закрывает игру
    def _quit_():
        for i in pygame.event.get():                            
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
        return 
        
    # Создаём функцию ULDR 
    # Которая отслеживает нажатие стрелочек, в параметр k введите клавишу которую  надо отследить например 'U', обратите внимание надо ввести заглавную букву 'U', 'L', 'D' или 'R'
    # Если ввести любую другую букву то результат всегда будет False
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
        
    # Создаём функцию WASD 
    # Которая отслеживает нажатие стрелочек, в параметр k введите клавишу которую  надо отследить например 'W', обратите внимание надо ввести заглавную букву 'W', 'A', 'S' или 'D'
    # Если ввести любую другую букву то результат всегда будет False
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


# создаём класс TIME
class TIME:
    
    # Создаём функцию time которая импортирует модуль time в игру
    def time():
        import time
        return 
        
    # Создаём функцию clock которая создоёт переменную отвечающую за скорость воспроизведения игры
    def clock():
        fps_clock = pygame.time.Clock()
        return fps_clock
        
    # Создаём функцию tick которая создоёт задержку во времени с помошью переменной fps_clock и fps
    # Фактически эта функция регулирует количество кадров в секунду каличество кадров указано в переменной fps
    def tick(fps: int, fps_clock):
        fps_clock.tick(fps)
        return
        
    # Создаём функцию _stop_ которая останавливает игру на количество секунд указанное в пораметре second
    def _stop_(second: float):
        import time
        time.sleep(second)
        return


# создаём класс warning
class warning:
    
    # Создаём функцию border
    # Эта функция проверяет не болше иле меньше x или y устоновленных границ x0, y0, x1, y1 и вазврощяет картридж из 4 значений 
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
        
    '''
    Создаём функцию wall
    Эта функция создаёт 'стену' и проверяет не зажодят ли координаты за неё
    параметр side принемает 'x' или 'y' в зависимости от того вертикальная стена или горезонтальная пишите 'x' если вертикальная а 'y' если горизонтальная
    coord принемает координаты стены если вертикальная то x стены а если горизонтальная то y стены 
    f координату начала стены, t конца
    x - x предмета, y - y предмета
    '''
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
            
    # Эта функция к сожалению покашто не работает
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


# создаём класс display
class display:
    
    # создаём функцию message
    # которая выводит на окно dis, сообшение msg, цвета collor, шрифта font, в координатах a,b
    def message(msg: str, collor, font, a: int, b: int, dis):
        mesg = font.render(msg, True, collor)
        dis.blit(mesg, [a,b])
        return
        
    # создаём функцию update которая обновляет экран 
    def update():
        pygame.display.update()
        return pygame.display.update()


# создаём класс font
class font:
    
    # создаём функцию fonts которая выдаёт шрифт под номером num 0:bahnschrift, 1:comicsansms, 2:arial размера a
    def fonts(num: int, a: int):
        font1 = pygame.font.SysFont('bahnschrift', a)
        font2 = pygame.font.SysFont('comicsansms', a)
        font3 = pygame.font.SysFont('arial', a)
        fonts = [font3, font2, font1]
        return fonts[num]
        
    # создаём функцию font которая выдаёт шрифт name с размером a
    def font(name: str, a: int):
        font = pygame.font.SysFont(name, a)
        return font


# создаём класс matrix
class matrix:
    
    # создаём функцию create
    '''
    которая создаёт матрецу с помощю файла file со специальным расширением .ftnpg 
    с помощью условных числовых обозначений где -1 всегда 'Entry' а остальные обозначения должны быть больше 1 
    в списке l указываются условные обозначения например [[-1, 'Entry'], [10, 'platform.png']]
    начало отрисовки идёт с x,y
    '''
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

