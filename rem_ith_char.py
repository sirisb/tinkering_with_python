def remove_char(word, pos):
    print(word)
    lst = []
    for i in range(0, len(word)):
        if i != pos:
            lst.append(word[i])
    print("".join(lst))
    

# Preferred way.
def remove_char1(word, pos):
    print(word[:pos]+word[pos+1:])


def remove_char2(word, pos):
    lst = "".join([word[i] for i in range(0, len(word)) if i != pos])
    print(lst)


def main():
    remove_char("Hello", 1)
    remove_char1("Hello", 1)
    remove_char2("Hello", 1)


if __name__ == "__main__":
    main()