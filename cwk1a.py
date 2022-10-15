def main():
    def is_number(number):
        result = False
        try:
            float(number)
            if (str(number).count(".") == 0 and str(number).count("-") == 0)or\
               (str(number).count(".") == 1 and str(number).count("-") == 0):
                result = True
        except:
            pass
        return result
    tax = input("Please input your tax: ")
    if is_number(tax):
        if float(tax) == 0.00:
            income = 12500.00
            print('%.2f' % income)
        elif float(tax) > 0 and float(tax) <= 7500.00:
            income = float(tax) / 0.2 + 12500.00
            print('%.2f' % income)
        elif float(tax) > 7500 and float(tax) <= 47500.00:
            income = (float(tax) - 7500) / 0.4 + 50000.00
            print('%.2f' % income)
        elif float(tax) >= 47500.00:
            income = (float(tax) - 47500) / 0.45 + 150000.00
            print('%.2f' % income)
    else:
        income = "Invalid amount!"
        print(income)
