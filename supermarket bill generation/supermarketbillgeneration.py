'''supermarket  bill generation project''' 
from datetime import datetime  
name= input('enter your name:')
#list of items
lists='''
Rice   Rs.50/kg
Dal    Rs.70/kg
Wheat  Rs.60/kg
Oil    Rs.100/kg
Sugar  Rs.50/kg
Salt   Rs.25/kg
Coffee Rs.90/kg
Tea    Rs.150/kg
Paneer Rs.300/kg
'''
#declaratipon
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
    
#rates for the items
items={'Rice':50,'Dal':70,'Wheat':60,'Oil':100,'Sugar':50,'Salt':25,'coffe':90,'Tea':150,'Paneer':300}       
option=int(input('for the list of items press1:'))    
if option==1:
    print(lists)   
for i in range(len(items)):
    inp1=int(input('if you want to buy plese press1 or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input('Enter quantity:'))
        if item in items.keys():
            price=quantity*items[item]
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print('sorry you entered item is not available')
    else:
        print('you have entered the wrong number')
    inp=input("can i bill the items yes or no:")
    if inp =='yes':
        pass
        if finalamount!=0:
            print(25*'=','chaitanya super market',25*'=')
            print(28*' ','vishkhapatnam')
            print(75*'-')
            print('Sno',8*' ',"items",8*' ','quantity',3*' ')
            for i in range(len(pricelist)):
                print(i,8*" ",5*" ",ilist[i],plist[i])
            print(75*" ")
            print(50*' ','Total amount','Rs',totalprice)
            print('gst amount',10*' ','Rs',gst)
            print(75*" ")
            print(50*' ','Final amount','Rs',finalamount)
            print(75*" ")
            print(20*' ','thanks for the visiting')
            print(75*" ")
        
    else:
        print('its okay, please visit u again')     