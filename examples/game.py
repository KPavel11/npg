# Импортируем модуль
import npg
npg.start._init_()
# Создоём окно
dis = npg.start._world_(x = 800, y = 800, name = 'example')
# Ресуем квадрат в координатах x:0, y:0
npg.draw.figure.rect(x = 0, y = 0, h = 40, w = 40, dis = dis, collor = (200, 200, 200))
# Обновляем экран
npg.display.update()


# Импортируем модуль time в игру
npg.TIME.time()
# Создоём переменную отвечающую за скорость воспроизведения игры
fps_clock = npg.TIME.clock()
# Ждём 1 секунду
npg.TIME._stop_(1)
# Создоём переменные
y = 0
x = 0
y1 = 60
x1 = 60
x2 = 0
y2 = 420
x3 = 618
y3 = 600
_min_ = False
_min_2 = False
_min_3 = False
# Запускаем игру
while True:
    # Проверяем не нажал ли игрок на кнопку 'Закрыть'
    npg.keys._quit_()
    

    # Проверяем нажатие на клавиши 'ULDR'
    if npg.keys.ULDR('U'):
        y -= 2
    if npg.keys.ULDR('D'):
        y += 2
    if npg.keys.ULDR('L'):
        x -= 2
    if npg.keys.ULDR('R'):
        x += 2

    # Ресуем четыре фоновых изображения
    npg.draw.back_picture(file = 'platform.png', dis = dis, window_size = (400, 400), y = 400)
    npg.draw.back_picture(file = 'platform.png', dis = dis, window_size = (400, 400))
    npg.draw.back_picture(file = 'platform.png', dis = dis, window_size = (400, 400),x = 400, y = 0)
    npg.draw.back_picture(file = 'platform.png', dis = dis, window_size = (400, 400),x = 400, y = 400)

    # Создаём кводратную матрицу с помощь текстового файла 'example.ftnpg'
    matr = npg.matrix.create('example', [[-1, 'Empty'], [20, 'platform3.png'], [10, 'platform.png']], x1, y1)
    # Рисуем фигуры согласно матреце
    npg.draw.matrix(l = matr, px = 32, dis = dis)
    
    matr = npg.matrix.create('example2', [[-1, 'Empty'], [20, 'platform2.png'], [10, 'platform.png']], x2, y2)
    npg.draw.matrix(l = matr, px = 32, dis = dis)
    matr = npg.matrix.create('example2', [[-1, 'Empty'], [20, 'platform2.png'], [10, 'platform.png']], x3, y3)
    npg.draw.matrix(l = matr, px = 32, dis = dis)
    matr = npg.matrix.create('example3', [[-1, 'Empty'], [10, 'platform.png']], 416, 0)
    npg.draw.matrix(l = matr, px = 32, dis = dis)
    
    if npg.keys.ULDR('U'):
        # Создоём костюм
        sprite = npg.new.costume('sprite_u.png', 32)
        
    elif npg.keys.ULDR('D'):
        sprite = npg.new.costume('sprite_d.png', 32)
        
    elif npg.keys.ULDR('L'):
        sprite = npg.new.costume('sprite_r.png', 32)
        
    elif npg.keys.ULDR('R'):
        sprite = npg.new.costume('sprite_l.png', 32)
        
    else:
        sprite = npg.new.costume('sprite_d.png', 32)
    # Отрисовываем костюм
    npg.draw.costume(x, y, sprite, 32, dis)
    # Отрисовываем сообшение
    npg.display.message('Привет', (255,255,0), npg.font.fonts(1, 45), 10, 10, dis)
    # Обнавляем экран
    npg.display.update()
    # Создоём задержку во времени с помошью переменной fps_clock, см строку 15 
    npg.TIME.tick(60, fps_clock)
    # Проверяем не косается ли объект устоновленных границ
    a = npg.warning.border(0, 0, 800, 800, x, y)
    if a[0]:
        x = 0
    elif a[1]:
        x = 800
    if a[2]:
        y = 0
    elif a[3]:
        y = 800

    #  Проверяем не косается ли объект указаного загрождения
    a = npg.warning.wall(side = 'x', coord = 400, f = 0, t = 416, x = x, y = y)
    if a:
        x = 390
        
    a = npg.warning.border(0, 0, 160, 160, x1, y1)
    if a[0]:
        x1 = 0
        _min_ = False
    elif a[1]:
        x1 = 160
        _min_ = True
    if a[2]:
        y1 = 0
        _min_ = False
    elif a[3]:
        y1 = 160
        _min_ = True
    if _min_:
        y1 -= 1
        x1 -= 1
    if not _min_:
        y1 += 1
        x1 += 1
    a = npg.warning.border(0, 0, 640, 800, x2, y2)
    if a[0]:
        _min_2 = False
    elif a[1]:
        _min_2 = True
    if _min_2:
        x2 -= 3
    elif not _min_2:
        x2 += 3
    a = npg.warning.border(0, 0, 640, 800, x3, y3)
    if a[0]:
        _min_3 = False
    elif a[1]:
        _min_3 = True
    if _min_3:
        x3 -= 3
    elif not _min_3:
        x3 += 3
    
        

    


