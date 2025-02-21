input_number = int(input('adj meg egy öszeget:'))
''' 
output
20,000FT --> 1 db 
'''

monye_type = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10,5]

for actual_type in monye_type:
    number_of_nots = int(input_number / actual_type)
    input_number = input_number % actual_type
    if number_of_nots > 0 :
        print(f'{actual_type}Ft -->{number_of_nots}db')

