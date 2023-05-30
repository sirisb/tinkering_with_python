def length(s):
    # by calling len() function.
    print(len(s))

    # with for loop.
    counter = 0
    for c in s:
        counter += 1
    print(counter)

    # with sum() and list comprehension.
    print(sum(1 for c in s))

    # a for loop is usually written as a loop over an iterable object.This means you don’t need a counting variable to
    # access items in the iterable.Sometimes, though, you do want to have a variable that changes on each loop
    # iteration. Rather than creating and incrementing a variable yourself, you can use Python’s enumerate() to get a
    # counter and the value from the iterable at the same time!
    
    for count, value in enumerate(s):
        pass
    print("enumerate", count+1)


def main():
    length("Hello there")


if __name__ == "__main__":
    main()