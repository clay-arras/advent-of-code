class RedNosedReports:
    def isSafe(report: list[int]) -> bool:
        assert len(report) >= 2
        isIncreasing: bool = report[0] < report[1]
        minD, maxD = 1, 3

        isSafe = True
        for i in range(len(report) - 1):
            levelDiff = report[i] - report[i + 1]
            if isIncreasing:
                levelDiff = report[i + 1] - report[i]
            isSafe &= levelDiff >= minD and levelDiff <= maxD

        return isSafe


def parse_input(filename: str) -> list[str]:
    file = open(filename, "r")
    body = file.readlines()
    file.close()
    return body


def main() -> None:
    body = parse_input("2.in")
    body = [i.split(" ") for i in body]

    safeCount = 0
    for report in body:
        levels = [int(i) for i in report]
        safeCount += RedNosedReports.isSafe(report=levels)
    print(safeCount)


if __name__ == "__main__":
    main()
