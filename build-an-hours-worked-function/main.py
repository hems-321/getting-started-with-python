# Write function here

def calculate_pay(working_hours, rate):
    overtime_hours = 0
    overtime_pay = 0
    if working_hours > 40:
        overtime_hours = working_hours - 40

    if overtime_hours:
        overtime_pay = overtime_hours * rate * 2

    return (working_hours*rate) + overtime_pay


def calculate_monthly_pay(wk_1_hours, wk_2_hours, wk_3_hours, wk_4_hours, pay_per_hour):
    return (calculate_pay(wk_1_hours, pay_per_hour)+
                calculate_pay(wk_2_hours, pay_per_hour)+
                calculate_pay(wk_3_hours, pay_per_hour)+
                calculate_pay(wk_4_hours, pay_per_hour))


print(calculate_monthly_pay(40,50,35,40,50))

# Worked 40 hours at $20 an hour
# print(calculate_pay(40, 20))

# Worked 50 hours at $20 an hour
# print(calculate_pay(50, 20))

# Worked 40 hours at $12 an hour
# print(calculate_pay(40, 12))
