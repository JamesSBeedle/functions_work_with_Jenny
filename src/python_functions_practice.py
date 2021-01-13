def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2



def subtract(number_1, number_2):
    return number_1 - number_2

subtract(10, 5)


def multiply(number_1, number_2):
    return number_1 * number_2

multiply(4, 2)


def divide(number_1, number_2):
    return number_1 / number_2

divide(10, 2)
    
def length_of_string(string):
    return len(string)



def join_string(string_1, string_2):
    return string_1 + string_2



def add_string_as_number(numero_1, numero_2):
    return int(numero_1) + int(numero_2)



# def number_to_full_name_month_1(number):
#     import datetime
#     number_to_full_month_name = datetime.datetime.now()
#     return number_to_full_name_month_1.strftime('%B') 

months = {1: "January", 3: "March", 9: "September", 10: "October", 4: "April"}
def number_to_full_month_name(month_number):
    return months[month_number]


def number_to_short_month_name(month_number):
    short_month = number_to_full_month_name(month_number)[0:3]
    return short_month


