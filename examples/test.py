def solution(S):
    # write your code in Python 3.6
    items = S.split("\n")
    sum = 0
    for item in items:
        num = int(item.split(",")[0])
        print(num)
        sum += num
    print(sum)
    return sum


# S = '+46,Maria R\n-121,Robert D,\n+12,Juan Felipe H.\n+213,Hannah G.\n-23,Maria R.'
# solution(S)


def solution(S, T, U):
    """
    Converts United States Dollar amount to Canadian Dollar amount

    Args:
        S: string. Amount in United States Dollar

    Returns:
        string. Amount in Canadian Dollar
    """

    USD_TO_CAD = 0.75
    USD_TO_AUD = 1.41
    USD_TO_CAD = 1.34
    USD_TO_CHF = 0.92
    USD_TO_EUR = 0.86
    USD_TO_GBP = 0.78
    USD_TO_JPY = 106.13

    AUD_TO_USD = 0.71
    CAD_TO_USD = 0.75
    CHF_TO_USD = 1.09
    EUR_TO_USD = 1.17
    GBP_TO_USD = 1.28
    JPY_TO_USD = 0.0094

    dict = {"USD_TO_AUD": 1.41, "USD_TO_CAD": 1.34, "USD_TO_CHF": 0.92, "USD_TO_EUR": 0.86, "USD_TO_GBP": 0.78,
            "USD_TO_JPY": 106.13,
            "AUD_TO_USD": 0.71, "CAD_TO_USD": 0.75, "CHF_TO_USD": 1.09, "EUR_TO_USD": 1.17, "GBP_TO_USD": 1.28,
            "JPY_TO_USD": 0.0094}

    if float(S) < 0:
        return "Error 1: Amount is a negative value."
    exchange_method = T + "_TO_" + U
    exchange_amount = S * exchange_method
    exchange_amount_rounded = "{:.2f}".format(exchange_amount)
    return str(exchange_amount_rounded)


def test(S, T, U):
    if float(S) < 0:
        return "Error 1: Amount is a negative value."

    if T != "USD" and U != "USD":
        return "Error 2: Exchange not supported."

    exchange_method = T + "_TO_" + U
    print(exchange_method)

    exchange_map = {
        "USD_TO_AUD": 1.41,
        "USD_TO_CAD": 1.34,
        "USD_TO_CHF": 0.92,
        "USD_TO_EUR": 0.86,
        "USD_TO_GBP": 0.78,
        "USD_TO_JPY": 106.13,
        "AUD_TO_USD": 0.71,
        "CAD_TO_USD": 0.75,
        "CHF_TO_USD": 1.09,
        "EUR_TO_USD": 1.17,
        "GBP_TO_USD": 1.28,
        "JPY_TO_USD": 0.0094
    }

    print(exchange_map[exchange_method])

    exchange_amount = float(S) * exchange_map[exchange_method]
    exchange_amount_rounded = "{:.2f}".format(exchange_amount)
    return exchange_amount_rounded
