import argparse
import math


def number_of_payments(principal, payment, interest):
    if principal > 0 and payment > 0 and interest > 0:
        interest /= 12 * 100
        periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
        if periods < 12:
            print(f'It will take {periods} '
                  f'{"month" if periods > 1 else "months"} '
                  f'to repay the loan!')
        elif periods % 12 == 0:
            years = periods // 12
            print(f'It will take {years} '
                  f'{"year " if years == 1 else "years "} '
                  f'to repay the loan!')
        else:
            years = math.floor(periods / 12)
            print(
                f'It will take {years} years and '
                f'{periods - years * 12} {"month" if periods - years * 12 > 1 else "months"} '
                f'to repay the loan!')
        overpayment = periods * payment - principal
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')


def annuity_payment_amount(principal, periods, interest):
    if principal > 0 and periods > 0 and interest > 0:
        interest /= 12 * 100
        payment = math.ceil(principal * (interest * math.pow(1 + interest, periods)) / (
                math.pow(1 + interest, periods) - 1))
        print(f'Your annuity payment = {payment}!')
        overpayment = periods * payment - principal
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')


def diff_payment_amount(principal, periods, interest):
    interest /= 12 * 100
    payments_sum = 0
    for m in range(1, periods + 1):
        dm = math.ceil(principal / periods + interest * (principal - principal * (m - 1) / periods))
        print(f'Month {m}: payment is {dm}')
        payments_sum += dm
    overpayment = payments_sum - principal
    print(f'Overpayment = {overpayment}')


def loan_principal(payment, periods, interest):
    if payment > 0 and periods > 0 and interest > 0:
        interest /= 12 * 100
        principal = int(payment / ((interest * math.pow(1 + interest, periods)) / (
                math.pow(1 + interest, periods) - 1)))
        print(f'Your loan principal = {principal}!')
        overpayment = periods * payment - principal
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')


parser = argparse.ArgumentParser()

parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)

args = parser.parse_args()

if not args.interest:
    print('Incorrect parameters')
    exit()
if args.type == 'annuity':
    if args.principal and args.payment and args.interest:
        number_of_payments(args.principal, args.payment, args.interest)
    elif args.principal and args.periods and args.interest:
        annuity_payment_amount(args.principal, args.periods, args.interest)
    elif args.payment and args.periods and args.interest:
        loan_principal(args.payment, args.periods, args.interest)
    else:
        print('Incorrect parameters')
elif args.type == 'diff':
    if args.principal and args.periods and args.interest:
        diff_payment_amount(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
