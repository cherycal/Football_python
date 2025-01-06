__author__ = 'chance'


def dicts_from_lists(items, headers, check: bool = True):
    if check:
        out_list: list = []
        rc = 1
        for row in items:
            if len(headers) != len(row):
                print(f"ERROR: Header length {len(headers)}: {headers} does not "
                      f"equal items length {len(row)} for row {rc}: {row}\n")
                raise Exception
            else:
                out_list.append({h: i for (h, i) in zip(headers, row)})
                rc += 1
    else:
        out_list = [{h: i for (h, i) in zip(headers, item)} for item in items]
    return out_list


def main():
    items = [["a", "1", "C"], ["b", "D"], ["c", "3", "F"], ["a", "4", "G"]]
    headers = ["lower", "number", "upper"]
    # print(dicts_from_lists(items, headers))
    # print()
    print(dicts_from_lists(items, headers, check=True))


if __name__ == "__main__":
    main()
