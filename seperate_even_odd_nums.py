def sep_even_odd_nums(nums):
    even_list = []
    odd_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list


#  Using list comprehension.
def sep_even_odd_nums1(nums):
    even_list = [num for num in nums if num % 2 == 0]
    odd_list = [num for num in nums if num % 2 != 0]
    return even_list, odd_list


def main():
    print(sep_even_odd_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(sep_even_odd_nums1([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == "__main__":
    main()

