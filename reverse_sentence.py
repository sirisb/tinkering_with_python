def reverse(sentence):
    i = -1
    sent_arr = sentence.split(" ")
    while -1*i <= len(sent_arr):
        print(sent_arr[i], end=" ")
        i = i-1
    print(" ")


def reverse1(sentence):
    s_arr = sentence[::-1]
    res = []
    for word in s_arr:
        res.append(word)
    print("".join(res))


def reverse2(sentence):
    s_arr = sentence.split()[::-1]
    res = []
    for word in s_arr:
        res.append(word)
    print(" ".join(res))


def reverse3(sentence):
    s_arr = sentence.split(" ")
    print(" ".join(reversed(s_arr)))


# Using stack
def reverse4(sentence):
    stack = []
    for word in sentence.split(" "):
        stack.append(word)
    res_str = []
    while stack:
        res_str.append(stack.pop())
    print("Using Stack ", " ".join(res_str))


def reverse5(sentence):
    s_arr = sentence.split()
    s_reverse = []
    for i in range(len(s_arr)-1, -1, -1):
        s_reverse.append(s_arr[i])
    print("Iterate from last ",  " ".join(s_reverse))


def reverse6(sentence):
    s_arr = sentence.split()
    end = len(s_arr)-1
    start = 0
    while start < end:
        temp = s_arr[start]
        s_arr[start] = s_arr[end]
        s_arr[end] = temp
        start += 1
        end -= 1
    print("Two Pointer = ", " ".join(s_arr))


def main():
    reverse("Today is Monday")
    reverse1("Today is Tuesday")
    reverse2("Today is Wednesday")
    reverse3("Today is Thursday")
    reverse4("Today is Friday")
    reverse5("Today is Saturday")
    reverse6("Everyday is awsome!")


if __name__ == "__main__":
    main()
