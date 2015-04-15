__author__ = 'Боян'


def loss_or_profit(income, outcome):
    income_sum = sum(income)
    loss_sum = sum(outcome)

    total = income_sum - loss_sum

    return total


print(loss_or_profit([1, 2, 3], [3]))
# '+3'
print(loss_or_profit([10], [20, 30]))
# '-40'
print(loss_or_profit([10], [10]))
# '=0'