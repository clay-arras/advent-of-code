class PageOrderChecker: 
    pass



def parse_input(filename: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    with open(filename, "r") as file:
        body = file.readlines()
        delim = body.index("\n")
        rules, updates = body[:delim], body[delim+1:]
        rules = [i.strip() for i in rules]
        updates = [i.strip() for i in updates]
        # updates = [ for j in updates]
        new_rules = []
        for i in rules:
            line = [int(x) for x in i.split(",")]
            new_rules.append(line)

        new_updates = []
        for i in updates:
            pass

        return rules, updates
    raise AssertionError


def main() -> None:
    rules, updates = parse_input("5.in")
    # print(updates)
    print(rules)


if __name__ == "__main__":
    main()