import json
from budget import income


def list_bills():
    with open("bills.json", 'r') as json_file:
        json_decoded = json.load(json_file)
    return json_decoded

def remaining(hours):
    data = income.net_income(hours) - sum(list_bills().values())
    return data
                


def add_bill():
    # Input option if they want to add a new bil
    print('''
    ######################################
    # Would you like to add a new bill?: #
    # Y = YES                            #
    # N = NO                             #
    ######################################
    ''')

    add_bill = input('')
    
    another = True
    while another == True:
        if add_bill == 'Y':
            bill_name = input('What is the bame of the bill?')
            bill_amount = input('How much is the bill?: ')

            with open("bills.json", 'r') as json_file:
                json_decoded = json.load(json_file)

            json_decoded[bill_name] = float(bill_amount)

            with open("bills.json", 'w') as json_out_file:
                json.dump(json_decoded, json_out_file)

            print('You added ' + bill_name.upper() + ' for the amount of $' + str(bill_amount) + ' to your budget')

            print('''
            ########################################
            # Would you like to add another bill?: #
            # Y = YES                              #
            # N = NO                               #
            ########################################
            ''')
            new_bill = input('')
            
            new = True
            
            while new == True:
                
                if new_bill == 'Y':
                    new == False
                    another == True
                    break
                    

                elif new_bill == 'N':
                    new == False
                    return another == False
                    
                
                else:
                    print('Invalid response, please enter a valid response')
                    new_bill = input()
                    


        elif add_bill == 'N':
            return print('No bills have been added')

        else:
            print('INVALID RESPONSE, please enter a valid response:')
            add_bill = input()


# def another_bill():
