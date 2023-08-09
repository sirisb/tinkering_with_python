def bin_search_recursive(nums_list, num, left, right, count=0):

    while left <= right:

        mid = (left+right)//2
        if nums_list[mid] == num:
            return mid+1, count+1
        if nums_list[mid] > num:
            return bin_search_recursive(nums_list, num, left, mid, count+1)
        if nums_list[mid] < num:
            return bin_search_recursive(nums_list, num, mid + 1, right, count + 1)
    return -1


def bin_search_iterative(nums_list, num):
    left, right = 0, len(nums_list)-1
    count = 0
    while left <= right:
        count = count + 1
        mid = (left+right)//2
        if nums_list[mid] == num:
            return mid+1, count
        if nums_list[mid] > num:
            right = mid
        else:
            left = mid+1
    return -1


# For every iteration, compare mid, left and right numbers with the target number to be found.
def bin_search_iterative_improved(nums_list, num):
    left, right = 0, len(nums_list)-1
    count = 0
    while left < right:
        count = count + 1
        mid = (left + right)//2
        if nums_list[mid] == num:
            return mid+1, count
        elif nums_list[left] == num:
            return left+1, count
        elif nums_list[right] == num:
            return right+1, count

        if nums_list[mid] > num:
            right = mid-1
            left = left+1
        else:
            left = mid+1
            right = right - 1
    return -1


def search(nums_list, num):
    if nums_list is None or len(nums_list) == 0:
        return -1
    return bin_search_recursive(nums_list, num, 0, len(nums_list) - 1)


def main():
    nums_list = [1, 2, 4, 5, 6, 7, 9, 12, 34, 45, 56, 67, 77, 78, 89, 90, 92, 95]

    pos, counts = search(nums_list, 1)
    print(f"Recursive Binary Search: position = {pos} and number of loops took to find = {counts} ")

    pos, counts = bin_search_iterative(nums_list, 1)
    print(f"Iterative Binary Search: position = {pos} and number of loops took to find = {counts} ")

    pos, counts = bin_search_iterative_improved(nums_list, 1)
    print(f"Improved Iterative Binary Search: position = {pos} and number of loops took to find = {counts} ")


if __name__ == "__main__":
    main()
