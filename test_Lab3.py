import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_more_than_ten():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 65, 67, 87, 78, 99]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 1

def test_bubble_sort_no_numbers():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 0)

def test_bubble_sort_not_int():
    result = []
    input_arr = ["99", "88", "77", "66", "55", "44"]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 2)