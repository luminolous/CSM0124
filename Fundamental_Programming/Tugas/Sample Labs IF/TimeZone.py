#HH:MM:SS untuk GMT+2
#CH:CM:CS untuk GMT+7

HH, MM, SS = map(int,input().split(':'))
CH, CM, CS = map(int,input().split(':'))

# HH = int(HH)
# MM = int(MM)
# SS = int(SS)
# CH = int(CH)
# CM = int(CM)
# CS = int(CS)

gmt2 = ( HH * 3600 ) + ( MM * 60 ) + ( SS * 1 )
gmt7 = (( CH * 3600 ) + ( CM * 60 ) + ( CS * 1 )) - ( 5 * 3600 )

time = gmt2 - gmt7

TH = time // 3600
TM = (time - (TH * 3600)) // 60
TS = ((time - (TH * 3600)) - (TM * 60))

TH = "%02d" %TH
TM = "%02d" %TM
TS = "%02d" %TS

if time > 0:
    print(TH + ":" + TM + ":" + TS)
elif time < 0:
    print("See you on the next pear event!")
