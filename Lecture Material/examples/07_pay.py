print('this is the start of the file')

GROSS_PAY = 0
NET_PAY = -1
RANDOM_VARIABLE = 1234

def calculate_weeks_pay(hours, hourly_pay):
    '''calculates the weeks pay

    Assumes that a 10% of the gross pay will be taken for payment of
    taxes.

    Parameters
    ----------
    hours : float
        the number of hours worked for the week
    hourly_pay : float
        the hourly payment

    Returns
    -------
    float
        the net pay expected'''
    print('this is the start of our function')
    print(RANDOM_VARIABLE)
    gross_pay = hours * hourly_pay
    net_pay = gross_pay * 0.90
    return net_pay, gross_pay

print('calling the function')
net, gross = calculate_weeks_pay(34.5, 16.25)

print(f'Your net pay is ${net:.2f}')
print(f'Your gross pay is ${gross:.2f}')
print('End')

#inputs = [2, 2.5, '6', 8]

#sum_val = add(inputs)