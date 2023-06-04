from ursina import *
import time
import random

# Inisialisasi aplikasi Ursina
app = Ursina()

# Membuat objek pemain 1
player1 = Entity(model='quad', texture='PngItem_4964749.png',
                 scale=(2, 1, 2), position=(-6, 0, 0))
player1.speed = 2

# Membuat objek pemain 2
player2 = Entity(model='quad', texture='Red-Convertible-Car-PNG-HD-Quality.png',
                 scale=(2, 1, 2), position=(-6, -2, 0))
player2.speed = 2

# Membuat map jalur
map_line1 = Entity(model='quad', color=color.gray,
                   scale=(15, 0.1, 1), position=(0, 1, 0))
map_line2 = Entity(model='quad', color=color.gray,
                   scale=(15, 0.1, 1), position=(0, -1, 0))
map_line3 = Entity(model='quad', color=color.gray,
                   scale=(15, 0.1, 1), position=(0, -3, 0))
map_line4 = Entity(model='quad', color=color.gray,
                   scale=(0.1, 4, 1), position=(-5, -1, 0))
map_line5 = Entity(model='quad', color=color.gray,
                   scale=(0.1, 4, 1), position=(6.5, -1, 0))

# Mendefinisikan fungsi untuk input tap-tap


def input_handler(key):
    if key == 'left arrow':
        player1.x -= player1.speed * time.dt

    if key == 'right arrow':
        player1.x += player1.speed * time.dt

    if key == 'a':
        player2.x -= player2.speed * time.dt

    if key == 'd':
        player2.x += player2.speed * time.dt

    check_finish()

# Mengatur input handler


def update():
    for key in ('left arrow', 'right arrow', 'a', 'd'):
        if held_keys[key]:
            input_handler(key)

# Fungsi untuk memeriksa pemain yang mencapai garis finish


def check_finish():
    if player1.x >= 5.5 or player2.x >= 5.5:
        end_game()

# Fungsi untuk mengakhiri permainan


def end_game():
    player1.speed = 0
    player2.speed = 0

    # Menampilkan pesan pemenang
    if player1.x >= 5.5 and player2.x >= 5.5:
        winner_text = Text(text='Draw!', origin=(0, 0),
                           scale=2, background=True)
    elif player1.x >= 5.5:
        winner_text = Text(text='Player 1 Wins!', origin=(
            0, 0), scale=2, background=True)
    else:
        winner_text = Text(text='Player 2 Wins!', origin=(
            0, 0), scale=2, background=True)


# Memulai aplikasi Ursina
app.run()
