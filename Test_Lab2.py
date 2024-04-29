from Lab2 import find_min_max, calc_average, sort_temperature

def test_find_min_max():   
    lst = [1,2,3]
    result = find_min_max(lst)
    assert (1, 3)

def test_calc_average():
    lst = [2,3,4,5,6]
    average = calc_average(lst)
    assert average == 4

def calc_median_temperature():
    lst = [1,2,3]
    median = calc_median_temperature(lst)
    assert median == 2