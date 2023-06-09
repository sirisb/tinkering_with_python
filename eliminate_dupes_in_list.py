# Given list of fruits,
# "Apple", "Orange", "Apple", "Grape", "Pear", "Mango".
# print unique set/ list
# print a unique sorted set/ list

# using set.  order not preserved.
def remove_dupes(fruits):
    return set(fruits)


# using dict to record num. of occurrences of a fruit in the collection, sort and remove dupes.
def remove_dupes1(fruits):
    res = {}
    for fruit in sorted(fruits):
        if fruit in res:
            res[fruit] = res[fruit] + 1
        else:
            res[fruit] = 1
    return res


def main():
    fruits = ("Apple", "Orange", "Apple", "Grape", "Pear", "Mango")
    print(remove_dupes(fruits))
    print(remove_dupes1(fruits))


if __name__ == "__main__":
    main()