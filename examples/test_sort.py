""" This is an example
"""


class SortHelper(object):
    """
    This is helper class for sort algorithm
    """

    def bubble_sort(self, arr):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

    def selection_sort(self, arr):
        for i in range(len(arr) - 1):

            # find min
            minimum = i

            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j

            # swap min & i
            arr[i], arr[minimum] = arr[minimum], arr[i]

    def insertion_sort(self, arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i

            # consider arr with two parts: Sorted |  unSorted
            # start from begining and put number in right place
            # we do backward here
            while pos > 0 and arr[pos - 1] > cursor:
                arr[pos] = arr[pos - 1]
                pos -= 1

            arr[pos] = cursor

    def merge_method(self, left, right, merged):
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged[left_index + right_index] = left[left_index]
                left_index += 1
            else:
                merged[left_index + right_index] = right[right_index]
                right_index += 1

        for left_index in range(left_index, len(left)):
            merged[left_index + right_index] = left[left_index]

        for right_index in range(right_index, len(right)):
            merged[left_index + right_index] = right[right_index]

        return merged

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left, right = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])

        return self.merge_method(left, right, arr)

    def partition_method(self, arr, begin, end):
        pivot_index = begin

        # select first element as pivot
        pivot = arr[begin]

        for i in range(begin + 1, end + 1):
            if arr[i] < pivot:
                tmp = arr[i]
                # if array takes maximum allowed memory here,
                # we first delete to prevent out of memory exception
                del arr[i]

                # insert tmp to the left side of pivot_index
                arr.insert(pivot_index, tmp)
                pivot_index += 1

        return pivot_index

    def quick_sort(self, arr, begin=0, end=None):
        if len(arr) == 0:
            return

        if end is None:
            end = len(arr) - 1

        if begin >= end:
            return

        pivot_index = self.partition_method(arr, begin, end)
        self.quick_sort(arr, begin, pivot_index - 1)
        self.quick_sort(arr, pivot_index + 1, end)


def test_bubble():
    shelper = SortHelper()
    run_test(shelper.bubble_sort)


def test_selection():
    shelper = SortHelper()
    run_test(shelper.selection_sort)


def test_insertion():
    shelper = SortHelper()
    run_test(shelper.insertion_sort)


def test_merge():
    shelper = SortHelper()
    run_test(shelper.merge_sort)


def test_quick():
    shelper = SortHelper()
    run_test(shelper.quick_sort)


def run_test(sortfx):
    arr = []
    sortfx(arr)
    assert arr == []

    arr = [2, 1, 4, 5, 3]
    sortfx(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    sortfx(arr)
    assert arr == [1, 2, 3, 4, 5]
