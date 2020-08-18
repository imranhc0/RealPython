decimalArea = 20 #how much rice gorw in 1 decimal area. For our understanding we think 20kg rice gorw in 1 decimal area
oneAcer = 1000 #one Acer = 1000 deciamal Area 
riceGrowInOneAcer = decimalArea*oneAcer # how much rice grow in 1 acer. For our Understanding we think decimalArea*oneAcer in 1 acer area.
riceStoreInOnePot = 80 #how much rice store in 1 pots . For our understanding we think 80kg rice store in 1 pot
riceStores = riceGrowInOneAcer / riceStoreInOnePot #how many pots need to store all rice 

print(riceStores) 
