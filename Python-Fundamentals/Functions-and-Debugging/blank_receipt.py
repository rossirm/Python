def create_header():
    return 'CASH RECEIPT\n------------------------------\n'


def create_body():
    return 'Charged to____________________\nReceived by___________________\n'


def create_footer():
    return '------------------------------\n\u00A9 SoftUni'


def create_receipt():
    return f'{create_header()}{create_body()}{create_footer()}'


print(create_receipt())
