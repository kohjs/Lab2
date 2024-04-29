def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    sorted_list = sort_temperature(num_list)
    average = calc_average(num_list)
    print("Average = ", average)
    find_min_max(sorted_list)
    calc_median_temperature(sorted_list)

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input("Input numbers: ")
    number_list = list(map(float, numbers.split(",")))

    return number_list

def calc_average(number_list):
    average = sum(number_list) / len(number_list)
    return average

def find_min_max(num_list):
    min = num_list[-1]
    max =  num_list[0]
    print("Largest value is", min)
    print("Smallest value is", max)

def sort_temperature(num_list):
    num_list.sort()
    return num_list
def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    
    n = len(sorted_list)
    
    if n == 0:
        return None
    
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        num1 = sorted_list[n // 2- 1]
        num2 = sorted_list[n // 2]
        return (num1+num2)/ 2



if __name__ == "__main__":
    main()