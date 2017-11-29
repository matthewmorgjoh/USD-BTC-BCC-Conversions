
def BTCtoUSD():

    print('How much is Bitcoin worth?')

    BTCvalue = input()
    print()
    # print(BTCvalue)

    print('Converting BTC to USD')
    print('Enter BTC amount: ')
    BTCamount = input()

    BTCtoUSD = float(BTCamount) * float(BTCvalue)
    answer = str(round(BTCtoUSD, 2))
    print()
    print('{0} Bitcoins is equal to ${1} USD.'.format(BTCamount, answer))
    # print(BTCtoUSD)

def BCCtoUSD():

    print('How much is BitConnect worth?')
    BCCvalue = input()
    print()

    print('Converting BCC to USD')
    print('Enter BCC amount: ')
    BCCamount = input()



    BCCtoUSD = float(BCCvalue) * float(BCCamount)
    answer = str(round(BCCtoUSD, 2))
    # print(BCCtoUSD)
    print()
    print('{0} BitConnect Coins is equal to ${1} USD.'.format(BCCamount, answer))


# BTCtoUSD()

# BCCtoUSD()

'''
print('Would you like to convert BTC or BCC?')
answer = input()
print()


if answer == 'BTC':
    BTCtoUSD()

if answer == 'BCC':
    BCCtoUSD()
'''



def USDtoBTC():

    print('How much is Bitcoin worth?')
    BTCvalue = input()
    print()


    print('Converting USD to BTC')
    print('Enter USD amount: ')
    USDamount = input()

    USDtoBTC = float(USDamount) / float(BTCvalue)

    answer = str(round(USDtoBTC, 7))
    print()

    print('${0} USD is equal to {1} Bitcoins.'.format(USDamount, answer))

def USDtoBCC():

    print('How much is BitConnect worth?')
    BCCvalue = input()
    print()

    print('Converting USD to BCC')
    print('Enter USD amount: ')
    USDamount = input()

    USDtoBCC = float(USDamount) / float(BCCvalue)

    answer = str(round(USDtoBCC, 7))
    print()

    print('${0} USD is equal to {1} BitConnect Coins.'.format(USDamount, answer))

print('Would you like to convert BTC or BCC?')
answer = input()

if answer == 'BTC':
    USDtoBTC()

if answer == 'BCC':
    USDtoBCC()

