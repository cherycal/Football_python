__author__ = 'chance'


def try_syntax(n: int) -> str:
    if n > 1:
        return f"{n} tries"
    else:
        return f"{n} try"


def test_lambda():
    print(f"test_lambda")
    n1 = 1
    n2 = 2
    nums = [0, 1, 2, 3, 4]
    print(f"{(lambda tt: f'{tt} try' if abs(tt) == 1 else f'{tt} tries')(n1)}")
    print(f"{(lambda tt: f'{tt} try' if abs(tt) == 1 else f'{tt} tries')(n2)}")
    print([f"{(lambda tt: f'{tt} try' if abs(tt) == 1 else f'{tt} tries')(num)}" for num in nums])


def test_map():
    print(f"test_map")
    nums = [0, 1, 2, 3, 4]
    print(list(map(try_syntax, nums)))


def test_sorted():
    num_list = [1, 3, 4, 2, 6, 3, 7, 2, 5]
    print(sorted(num_list))


def main():
    test_sorted()


if __name__ == "__main__":
    main()
