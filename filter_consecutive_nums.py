# To filter a list consisting of, list of consecutive numbers.
def filter_consecutive_nums(num_array):
    if len(num_array) < 2:
        return [num_array]

    result = []

    for i, curr in enumerate(num_array, start=0):
        if i == 0:
            sub_array = [curr]
            prev = curr
            continue
        if prev + 1 == curr:  # if current num is consecutive num of previous
            sub_array.append(curr)
            prev = curr
        else:
            result.append(sub_array)
            prev = curr
            sub_array = [prev]
    result.append(sub_array)

    return result


def main():
    nums = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14]
    print(filter_consecutive_nums(nums))


if __name__ == "__main__":
    main()
