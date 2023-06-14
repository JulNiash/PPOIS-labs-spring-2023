import datetime
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

import Tournament
from Tournament import *
import sys
import json
import App
from DataControl import *


def main():
    '''l = []
    sp = ['Баскетбол', 'Бейсбол', 'Бокс', 'Карате', 'Футбол', 'Волейбол', 'Легкая атлетика']
    name = ['Роман', 'Дмитрий', 'Кирилл', 'Вячеслав', 'Иван', 'Алексей', 'Даниил', 'Илья', 'Михаил', 'Александр']
    surn = ['Заломов', 'Кулешов', 'Шершень', 'Шакин', 'Буланович', 'Заяц', 'Кимстач', 'Новик', 'Мороз', 'Летко',
            'Захаров', 'Соболь', 'Васильев', 'Карелин', 'Павлов',]
    for i in range(50):
        t = Tournament()
        a = random.randint(0, len(sp)-1)
        t.tournament_name = 'Турнир по ' + sp[a]
        t.sport_name = sp[a]
        t.prize_money = random.randint(10, 500)
        t.set_winner_money()
        t.date = '{}/{}/{}'.format(str(random.randint(0, 29)), str(random.randint(1, 12)),
                                   str(random.randint(1991, 2023)))
        t.winner_name = name[random.randint(0, len(name)-1)] + ' ' + surn[random.randint(0, len(surn)-1)]
        l.append(t)
    write(l)'''

    app = QApplication(sys.argv)

    window = App.MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()