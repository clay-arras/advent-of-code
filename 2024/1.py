from collections import defaultdict
from dataclasses import dataclass


@dataclass
class ListSimilarityMetrics:
    left_list: list[int]
    right_list: list[int]

    def pair_distance_sum(self) -> int:
        self.left_list.sort()
        self.right_list.sort()

        list_length: int = len(self.left_list)
        list_sum: int = 0
        for i in range(list_length):
            list_sum += abs(self.left_list[i] - self.right_list[i])

        return list_sum

    def similarity_score_sum(self) -> int:
        right_freq_dict = defaultdict(lambda: 0)
        for i in self.right_list:
            right_freq_dict[i] += 1

        similarity_sum = 0
        for i in self.left_list:
            similarity_sum += i * right_freq_dict[i]

        return similarity_sum


def parse_input(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, "r") as file:
        body = file.readlines()
        left_list: list[int] = []
        right_list: list[int] = []

        for i in body:
            line = [x for x in i.split(" ") if x != ""]
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))
        return left_list, right_list

    raise AssertionError


def main() -> None:
    left_list, right_list = parse_input("1.in")
    ret = ListSimilarityMetrics(left_list=left_list, right_list=right_list)
    print(ret.similarity_score_sum())


if __name__ == "__main__":
    main()
