def max_in_row(table):
    max_element = 0
    for row in table:
        if table[row]>=table[row+1]:
            max_element += table[row]
    return max_element
    """
    Дан двумерный массив(список списков, таблица) размером n x m.
    Каждая строка состоит из m элементов, всего n строк.
    Верните список, где будут максимумы для каждой строки таблицы:
    1-ый элемент это максимум в первой строке таблицы, 2-ой максимум во второй и тд
    """
    pass


def test_max_in_row():
    assert max_in_row([
        [1, 2, 3, 4],
        [1, -1, 1, 2],
        [-4, -3, -2, -1]
    ]) == [4, 2, -1]
    assert max_in_row([
        [1],
        [2],
        [3],
    ]) == [1, 2, 3]
    assert max_in_row([
        [-1, -2, -3, -4],
        [-1, -1, -1, -2],
        [-4, -3, -2, -1]
    ]) == [-1, -1, -1]
print("Tests passed")
