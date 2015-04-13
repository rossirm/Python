__author__ = 'Боян'


def loss_or_profit(income, outcome):
    income_sum = sum(income)
    loss_sum = sum(outcome)

    total = income_sum - loss_sum

    if total > 0:
        print("+{0}".format(total))
    elif total == 0:
        print("={0}".format(total))
    else:
        print("{0}".format(total))


loss_or_profit([1, 2, 3], [3])
# '+3'
loss_or_profit([10], [20, 30])
# '-40'
loss_or_profit([10], [10])
# '=0'