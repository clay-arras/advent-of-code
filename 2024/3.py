from dataclasses import dataclass


@dataclass
class MulFunc:
    mul_str: str

    FIRST_HALF = "mul("
    LAST_HALF = ")"
    MAX_DIGIT_LENGTH = 3
    MIN_DIGIT_LENGTH = 1

    def evaluate_expr(self) -> int:
        if not self._is_valid():
            return 0
        processed_mul = self._process_mul_str()
        [firstParam, secondParam] = [int(i) for i in processed_mul]
        return firstParam * secondParam

    def _is_valid(self) -> bool:
        # TODO: misses the case mul(43,$^32)
        first_half_len = len(self.FIRST_HALF)
        last_half_len = len(self.LAST_HALF)

        is_valid = True
        is_valid &= len(self.mul_str) >= (
            first_half_len + last_half_len + 2 * self.MIN_DIGIT_LENGTH + 1
        )
        is_valid &= self.mul_str[:first_half_len] == self.FIRST_HALF
        is_valid &= self.mul_str[-last_half_len:] == self.LAST_HALF

        function_params = self._process_mul_str()
        is_valid &= len(function_params) == 2
        is_valid &= all(
            len(i) >= self.MIN_DIGIT_LENGTH and len(i) <= self.MAX_DIGIT_LENGTH
            for i in function_params
        )
        is_valid &= all(i.isdigit() for i in function_params)

        return is_valid

    def _process_mul_str(self) -> list[str]:
        removed_identifier = self.mul_str[
            len(self.FIRST_HALF) : -len(self.LAST_HALF)
        ].split(",")
        return removed_identifier


def parse_input(filename: str) -> list[str]:
    with open(filename, "r") as file:
        body = file.readlines()
        return body
    raise AssertionError


def main() -> None:
    body = parse_input("3.in")
    body = "\0".join(body)

    sum_of_mul_evals = 0
    for i in range(len(body) - len(MulFunc.FIRST_HALF)):
        if body[i : i + len(MulFunc.FIRST_HALF)] == MulFunc.FIRST_HALF:
            continue
        last_half_index = body[i + len(MulFunc.FIRST_HALF) :].find(
            MulFunc.LAST_HALF
        )
        if last_half_index == -1:
            continue
        sum_of_mul_evals += MulFunc(
            body[i : i + len(MulFunc.FIRST_HALF) + last_half_index + 1]
        ).evaluate_expr()

    print(sum_of_mul_evals)


if __name__ == "__main__":
    main()