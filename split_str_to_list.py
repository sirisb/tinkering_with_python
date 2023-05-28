import itertools


def str_to_list(s):
    print(s)
    print(*s)
    print([*s])  # Unpacking iterables like list, dict and tuples.
    lst = [*s]
    print(lst)

    # Using basic for loop to iterate over char in string
    lst = []
    for c in s:
        lst.append(c)
    print(lst)

    # List COMPREHENSION.
    letter = [x for x in s]
    print(letter)

    # list typecasting
    letters = list(s)
    print(letters)

    # using list.extend() function.
    lst = []
    lst.extend(s)
    print(lst)

    # using itertools.chain
    letters = list(itertools.chain.from_iterable(s))
    print(letters)

    # using list slicing
    lst[:] = s
    print(lst)


def main():
    str_to_list("Hello There")


if __name__ == "__main__":
    main()
