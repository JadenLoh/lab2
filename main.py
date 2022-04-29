def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    list1 = get_user_input()
    print("Average: ",calc_average_temperature(list1))
    calc_min_max_temperature(list1)
    print("Median: ",calc_median_temperature(list1))

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    listoflists = input()
    x = listoflists.split(",")
    print(type(x))
    listoffloats1 = [float(a) for a in x]
    print(listoffloats1)
    return listoffloats1

def calc_average_temperature(x):
    avg = sum(x) / len(x)
    return avg

def calc_min_max_temperature(y):
    minlist = min(y)
    print("Min: " , minlist)
    maxlist = max(y)
    print("Max: " , maxlist)

def calc_median_temperature(z):
    z_sorted = z.sort()
    if len(z) % 2 != 0:
        m = int((len(z) + 1) / 2 - 1)
        return z[m]
    else:
        m1 = int(len(z)/2 - 1)
        m2 = int(len(z)/2)
        return (z[m1]+z[m2])/2

main()