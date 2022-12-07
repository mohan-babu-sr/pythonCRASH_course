hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = False

if hasHighIncome and hasGoodCredit and not hasCriminalRecord:
    print('Eligible for loan!')
elif hasHighIncome or hasGoodCredit and not hasCriminalRecord:
    print('Need to has some property for loan!')
else:
    print('U r not eligible for a loan!!!')
