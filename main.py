from typing import Union

def approximate_sqrt(number: int, precision: Union[int, float]):

    if type(number) == str or type(precision) == str:
        return "Podaj poprawnie dane"

    if number <= 0:
        return 0.0

    epsilon = 10**(-precision)
    b = float(number)
    a = number / b
    
    while abs(a - b) >= epsilon:
        b = (a + number / a) / 2
        a = number / b
    
    return round(b, precision)

def get_user_input():
    number = int(input("Podaj liczbę do spierwiastkowania: "))
    precision = int(input("Podaj ilość miejsc po przecinku: "))
    return number, precision

def main():
    number, precision = get_user_input()
    result = approximate_sqrt(number, precision)
    print(result)

if __name__ == "__main__":
    main()