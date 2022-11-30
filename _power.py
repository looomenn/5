""" Finding the power of a number that, in the congruent equation, equals 1 or -1 with modulus M """
def main() -> list:
    given_int, power, modulus = map(int, input().split())

    cases = []
    seq = modulus / 2
    number = 1

    for _ in range(1, power+1):
        number *= given_int

        while abs(number) > seq:
            if __DEBUG == 1:
                debug = number

            if number < 0:

                number += modulus

                if __DEBUG == 1:
                    print(f'[DEBUG] operation: +\t power: {_:<5} old: {debug:<5} new: {number:<5}')
            else:
                number -= modulus

                if __DEBUG == 1:
                    print(f'[DEBUG] operation: -\t power: {_:<5} old: {debug:<5} new: {number:<5}')

        case = {f'{given_int}^{_} ≅ {number} (mod {modulus})'}
        cases.append(case)

        if __LIMIT == 1:
            if number == -1 or number == 1:
                break

            if _ == power:
                print(f'[DEBUG] Power {power} of given number is not enough to get 1 or -1!')
                break

    return cases


if __name__ == "__main__":
    print('0 - Limit On | 1 - Limit off | 2 - Debug + Limit on | 3 - Debug only')
    state = int(input('State (0 | 1 | 2 | 3)'))

    # 0 - Limit On | 1 - Limit off | 2 - Debug + Limit | 3 - Debug only

    match state:
        case 0:
            __LIMIT = 1
            __DEBUG = 0
        case 1:
            __LIMIT = 0
            __DEBUG = 0
        case 2:
            __LIMIT = 1
            __DEBUG = 1
        case 3:
            __LIMIT = 0
            __DEBUG = 1
        case other:
            __LIMIT = 1
            __DEBUG = 0

    for case in range(int(input())):
        print(f'Case #{case+1}: {main()}')

# 1 - debug?
# 0 - stop on 1 | -1  ?
# 1 - test-cases
# 7 10 100 - test case
