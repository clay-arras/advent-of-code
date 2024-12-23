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


@dataclass
class WordFinder:
    word: str
    grid: list[str]

    def count_num_words(self) -> int:
        num_words = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for k in [
                    Dirs.N,
                    Dirs.E,
                    Dirs.S,
                    Dirs.W,
                    Dirs.NE,
                    Dirs.NW,
                    Dirs.SE,
                    Dirs.SW,
                ]:
                    num_words += self._is_word_at_pos(x=i, y=j, dir=k)

        return num_words

    def _is_word_at_pos(self, x: int, y: int, dir: Dirs) -> bool:
        is_match = True
        for c in self.word:
            if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[x]):
                return False
            is_match &= self.grid[x][y] == c
            x += dir.value.x
            y += dir.value.y
        return is_match


def parse_input(filename: str) -> list[str]:
    with open(filename, "r") as file:
        body = file.readlines()
        body = [i.strip() for i in body]
        return body
    raise AssertionError


def main() -> None:
    body = parse_input("4.in")
    print(WordFinder(word="XMAS", grid=body).count_num_words())


if __name__ == "__main__":
    main()
