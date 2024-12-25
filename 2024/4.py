from dataclasses import dataclass
from enum import Enum


@dataclass
class Coord:
    x: int
    y: int


class Dirs(Enum):
    N = Coord(0, 1)
    E = Coord(1, 0)
    S = Coord(0, -1)
    W = Coord(-1, 0)
    NE = Coord(1, 1)
    NW = Coord(-1, 1)
    SE = Coord(1, -1)
    SW = Coord(-1, -1)


class WordFinder:
    def __init__(self, grid: list[str], word: str):
        self.grid = grid
        self.word = word
        self.width = len(grid)
        self.height = len(grid[0])

    def count_num_words(self) -> int:
        num_words = 0
        for i in range(self.width):
            for j in range(self.height):
                for k in Dirs:
                    num_words += self._is_word_at_pos(x=i, y=j, dir=k)
        return num_words

    def count_num_x_words(self) -> int:
        num_words = 0
        for i in range(self.width):
            for j in range(self.height):
                num_words += self._is_word_x_at_pos(x=i, y=j)
        return num_words

    def _is_word_at_pos(self, x: int, y: int, dir: Dirs) -> bool:
        is_match = True
        for c in self.word:
            if not self._check_in_bounds(x=x, y=y):
                return False
            is_match &= self.grid[x][y] == c
            x += dir.value.x
            y += dir.value.y
        return is_match

    def _is_word_x_at_pos(self, x: int, y: int) -> bool:
        word_radius = len(self.word) // 2
        nw_se: bool = self._is_word_at_pos(
            x - word_radius, y + word_radius, dir=Dirs.SE
        ) or self._is_word_at_pos(x + word_radius, y - word_radius, dir=Dirs.NW)

        ne_sw: bool = self._is_word_at_pos(
            x + word_radius, y + word_radius, dir=Dirs.SW
        ) or self._is_word_at_pos(x - word_radius, y - word_radius, dir=Dirs.NE)

        return nw_se and ne_sw

    def _check_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height


def parse_input(filename: str) -> list[str]:
    with open(filename, "r") as file:
        body = file.readlines()
        body = [i.strip() for i in body]
        return body
    raise AssertionError


def main() -> None:
    body = parse_input("4.in")
    print(WordFinder(word="MAS", grid=body).count_num_x_words())


if __name__ == "__main__":
    main()
