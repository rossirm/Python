def create_header():
    print('CASH RECEIPT\n------------------------------')


def create_body():
    print('Charged to____________________\nReceived by___________________')


def create_footer():
    print('------------------------------\n\u00A9 SoftUni')


def create_receipt():
    create_header()
    create_body()
    create_footer()


create_receipt()
