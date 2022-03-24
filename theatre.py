# Theatre exercise

def ten_percent(total):
    if total > 100:
       disc = 0.10
    else:
        total < 100
        disc = 0
    total_discount = total*disc
    final_price = total-total_discount
    return final_price

def discount(free_ticket):
    number_children = 0
    number_adult = 0
    while True:
        if number_children >= 10 <= 19:
            number_adult = -1
        elif number_children >= 20 <= 29:
            number_adult = -2
        elif number_children >= 30 <= 39:
            number_adult = -3
        elif number_children >= 40 <= 49:
            number_adult = -4
        elif number_children >= 50 <= 59:
            number_adult = -5
        elif number_children >= 60 <= 69:
            number_adult = -6
        elif number_children >= 70 <= 79:
            number_adult = -7
        elif number_children >= 80 <= 89:
            number_adult = -8
        elif number_children >= 90 <= 99:
            number_adult = -9
        elif number_children >= 100 <= 109:
            number_adult = -10
        else:
            number_adult ==""
            break
def discount(price):
        age = int(input("Please enter your age: "))
        con = 8.40
        if age > 65:
            price = con
        elif age < 12:
            price = child
        else:
            price = adult

            return price




adult = 10.50
child = 7.30
con = 8.40
number_children = 0
number_adult = 0
con_number = 0
adult_sum = number_adult*adult
child_sum = number_children*child
con_sum = con_number*con
total = adult_sum+child_sum+con_sum


