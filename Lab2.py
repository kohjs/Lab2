def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    sorted_list = sort_temperature(num_list)
    average = calc_average(num_list)
    print("Average = ", average)
    find_min_max(sorted_list)

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input("Input numbers: ")
    number_list = list(map(float, numbers.split(",")))

    return number_list

def calc_average(number_list):
    return sum(number_list) / len(number_list)

def find_min_max(num_list):
    print("Largest value is", num_list[-1])
    print("Smallest value is", num_list[0])

def sort_temperature(num_list):
    num_list.sort()
    return num_list

if __name__ == "__main__":
    main()