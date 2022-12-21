import numpy as np
import pandas as pd

x=np.array([0,1,2,3,4,5])
p=np.array([0.3,0.2,0.15,0.1,0.13,0.12])   #probability values
cp= np.cumsum(p)   # cumulitive values
cp

#random numbers
rnd= np.array([0.33,0.98,0.38,0.22,0.52,0.49,0.51])

#prob = 0.33
#i_sim = np.sum(cp<prob)
#x[i_sim]
                       
simulates=[]
for prob in rnd:
    i_sim = np.sum(cp<prob)
    simulates.append(x[i_sim])   
print(simulates)
    

## Supply

x=np.array([10,20,30,40,50])
c=np.array([40,50,190,150,70])
p=c/500
cp=np.cumsum(p)
cp
rnd_supply = np.array([0.34,0.9,0.22,0.45,0.68])

simu_supply = []
for pro in rnd_supply:
    i_sim = np.sum(cp<pro)
    simu_supply.append(x[i_sim])
print(simu_supply)




#Demand 
x=np.array([10,20,30,40,50])
c=np.array([50,110,200,100,40])
p=c/500
cp=np.cumsum(p)
cp
rnd_dem = np.array([0.98,0.35,0.89,0.3,0.48])

simu_dem = []
for pro in rnd_dem:
    i_sim = np.sum(cp<pro)
    simu_dem.append(x[i_sim])
print(simu_dem)   




df = pd.DataFrame({'Supply Rnd':rnd_supply,
                   'Sim Supply':simu_supply,
                   'Demand Rnd':rnd_dem,
                   'Sim Demand':simu_dem})

df['Sold Quantity'] = np.minimum(df['Sim Supply'],
                                 df['Sim Demand'])

df['Waste Quantity']=(df['Sim Supply']-df['Sold Quantity'])
df['Profit']=(df['Sold Quantity']*10)
df['Loss']=(df['Waste Quantity']*8)
df['Net']=(df['Profit']-df['Loss'])
df
















