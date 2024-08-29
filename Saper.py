from random import randint as rnd  # random.randint imported and bound as rnd


class Cell:
    """Инициализирует объект клетки"""

    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True  # open/close the cell


class GamePole:
    """Инициализирует экземпляр игрового поля"""

    def __init__(self, N, M):
        self._n = N  # N - размер поля
        self._m = M  # M - общее число мин на поле
        self.pole = [[Cell() for n in range(self._n)] for i in range(self._n)]
        self.init()

    def init(self):
        """Расставляет мины в случайные клетки"""
        while self._m:
            i = rnd(0, self._n - 1)
            j = rnd(0, self._n - 1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True
                self._m -= 1

        index_around_cell = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        # координаты клеток вокруг поля
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    count_mines = sum((self.pole[x + i][y + j].mine for i, j in index_around_cell if
                                       0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = count_mines

    def show(self):
        """Показывает поле"""
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()
