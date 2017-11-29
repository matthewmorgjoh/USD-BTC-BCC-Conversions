def BTCtoUSD(BTCvalue, BTCamount):


    BTCtoUSD = float(BTCamount) * float(BTCvalue)
    answer = str(round(BTCtoUSD, 2))
    print()
    print('{0} Bitcoins is equal to ${1} USD.'.format(BTCamount, answer))
    # print(BTCtoUSD)

BTCtoUSD(8258.52, 0.00092739)

def BCCtoUSD(BCCvalue, BCCamount):

    BCCtoUSD = float(BCCvalue) * float(BCCamount)
    answer = str(round(BCCtoUSD, 2))
    # print(BCCtoUSD)
    print()
    print('{0} BitConnect Coins is equal to ${1} USD.'.format(BCCamount, answer))

BCCtoUSD(297.31, 162.0)

