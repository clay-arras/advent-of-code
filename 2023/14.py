class SimulateReflectorDish:
    def __init__(self, dish: list[str]) -> None:
        self.dish = dish

    def simulate_tilt(self) -> None:
        pass

    def calculate_total_load(self) -> int:
        pass        


def parse_input(filename: str) -> list[str]:
    file = open(filename, "r")
    body = file.readlines()
    file.close()
    return body


def main() -> None:
    dish = parse_input("14.in")
    simulator = SimulateReflectorDish(dish)
    simulator.simulate_tilt()
    total_load = simulator.calculate_total_load()
    print(total_load)


if __name__ == "__main__":
    main()
