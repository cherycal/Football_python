__author__ = 'chance'
from dictdiffer import diff
from deepdiff import DeepDiff


dictA = {
    'A1': {'name': 'Alan', 'age': 1},
    'A2': {'name': 'Aaron', 'age': 2},
    'A3': {'name': 'Angel', 'age': 3}
}

dictB = {
    'A4': {'name': 'Arthur', 'age': 4},
    'A2': {'name': 'Aaron', 'age': 5},
    'A3': {'name': 'Angel', 'age': 3}
}


def test_dict_diffs():

    key_diffs = (set(dictA.keys()) | set(dictB.keys())) - (set(dictA.keys()) & set(dictB.keys()))
    print(f"key diffs: {key_diffs}")
    print("Diff")
    print(list(diff(dictA, dictB)))
    print("DeepDiff")
    print(DeepDiff(dictA, dictB))


def main():
    test_dict_diffs()


if __name__ == "__main__":
    main()
