from pygame import*

back = (2,250, 172)
win_widht = 700
win_height = 600
window = display.set_mode((win_widht, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)