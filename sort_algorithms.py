def insert_sort(array):
    """Function for insert sorting algorithm"""
    # position of new element for comparison
    for i in range(len(array)):
        # j is the index of element for comparison
        j = i
        # check if the element is the first or if it less than the previous
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            # new index of element for comparison
            j -= 1


def selection_sort(array):
    """Function for selection sorting algorithm"""
    # the last element will automatically be correct
    for i in range(len(array)-1):
        # compare the first with all the next to find the least
        # then the second to find the least + 1 ...
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]


def buble_sort(array):
    """Function for buble sorting algorithm"""
    for i in range(1, len(array)):
        # the last element will always be correct
        # after the first cycle the last-1 also correct ...
        for j in range(len(array)-i):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]


def test_func(sort_algorithm):
    """ Tests for sorting algorithms"""
    print("Testing of ", sort_algorithm.__doc__)
    a = [4, 2, 3, 5, 1, 7, 6]
    a_sorted = [1, 2, 3, 4, 5, 6, 7]
    b = [3, -1, 0, 2, 1, -2, -3]
    b_sorted = [-3, -2, -1, 0, 1, 2, 3]
    c = [4, 3, 2, 2, 1]
    c_sorted = [1, 2, 2, 3, 4]
    sort_algorithm(a)
    sort_algorithm(b)
    sort_algorithm(c)
    print("Ok!" if a == a_sorted else "Fail!")
    print("Ok!" if b == b_sorted else "Fail!")
    print("Ok!" if c == c_sorted else "Fail!")


test_func(insert_sort)
test_func(selection_sort)
test_func(buble_sort)
