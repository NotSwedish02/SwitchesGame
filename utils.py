import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()

font = pg.font.SysFont("TimesNewRoman",24)

FPS = 100.0
DELTA = 1/FPS

def spritesheet_to_frames(img,n):
    size = img.get_width()/n

    frames = []

    for i in range(n):
        surf = pg.Surface((size,size))
        surf.blit(img, (-i * size, 0))
        surf.set_colorkey((0,0,0))
        frames.append(surf)

    return frames

def load_img(img,scale,colorkey=(0,0,0)):
    img = pg.image.load("images/" + img + ".png")
    img = pg.transform.scale(img, (img.get_width()*scale,img.get_height()*scale))
    img.set_colorkey(colorkey)

    return img.convert_alpha()

def draw_arrow(start, end_, display):
    pg.draw.aaline(display, (255,255,255), start, end_, 3)    
    pg.draw.aaline(display, (255,255,255), end_, end_ + (end_ - start).rotate(140) * .25, 3)
    pg.draw.aaline(display, (255,255,255), end_, end_ + (end_ - start).rotate(-140) * .25, 3)

def hp_color(value):
    r = 40 + 70-value*.7
    b = 10 + value*1.5
    g = 10

    r*=2.55
    b*=2.55
    g*=2.55

    b = min(255,b)
    r = max(0,r)

    return r,g,b

debug_color_by_id = {
    0: (255,0,0),
    1: (255,155,0),
    2: (255,255,0),
    3: (255,155,155),
    4: (0,0,255),
    5: (0,155,255),
    6: (0,255,255),
    7: (0,255,155),

}

