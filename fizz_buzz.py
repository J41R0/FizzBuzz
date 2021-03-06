def is_divisible(number, divisor):
    """
    Validate if number is divisible by divisor
    Args:
        number: int number
        divisor: int number

    Returns: True if number is divisible by divisor; False otherwise

    """
    return True if (number % divisor) == 0 else False


def fizz_buzz_game(number):
    """
    If number is divisible by 3 return 'Fizz', if divisible by 5 return 'Buzz' and if divisible by 3 and 5 return
     'FizzBuzz'. In any other situation return number
    Args:
        number: int number

    Returns: A word if number is divisible by 3, 5 or both; number otherwise

    """
    if type(number) != int:
        return "Invalid data type"
    if is_divisible(number, 3) and is_divisible(number, 5):
        return 'FizzBuzz'
    if is_divisible(number, 3):
        return 'Fizz'
    if is_divisible(number, 5):
        return 'Buzz'

    return number
