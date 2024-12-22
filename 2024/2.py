from dataclasses import dataclass


@dataclass
class Report:
    levels: list[int]

    MIN_DIFFERENCE = 1
    MAX_DIFFERENCE = 3

    def is_safe(self) -> bool:
        assert len(self.levels) >= 2
        is_increasing: bool = self.levels[0] < self.levels[1]

        is_safe = True
        for i in range(len(self.levels) - 1):
            if is_increasing:
                level_diff = self.levels[i + 1] - self.levels[i]
            else:
                level_diff = self.levels[i] - self.levels[i + 1]
            is_safe &= (
                level_diff >= self.MIN_DIFFERENCE and level_diff <= self.MAX_DIFFERENCE
            )

        return is_safe

    def is_safe_with_dampener(self) -> bool:
        is_safe = self.is_safe()
        for i in range(len(self.levels)):
            new_levels = self.levels[:i] + self.levels[i + 1 :]
            is_safe |= Report(new_levels).is_safe()
        return is_safe


def parse_input(filename: str) -> list[str]:
    with open(filename, "r") as file:
        body = file.readlines()
        body = [i.split(" ") for i in body]
        new_body: list[list[int]] = []

        for report in body:
            new_report = [int(i) for i in report]
            new_body.append(new_report)
        return new_body

    raise AssertionError


def main() -> None:
    body = parse_input("2.in")

    safe_count = 0
    for report in body:
        safe_count += Report(report).is_safe_with_dampener()
    print(safe_count)


if __name__ == "__main__":
    main()
