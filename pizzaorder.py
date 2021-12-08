print('HI! WELCOME TO OUR PIZZA WORLD :-)')
print('AVAILABLE ITEMS :')
pizza={
    'small pizza':{'name':'RS', 'price' : 150},
    'medium pizza':{'name':'RS','price':200},
    'large pizza':{'name':'RS','price':250},
    'pepperoni for small pizza':{'name':'RS','price':20},
    'pepperoni for medium or large pizza':{'name':'RS','price':30},
    'extra cheese for any size pizza':{'name':'RS','price':10}
      }

for i in pizza.keys():
    print(i+' : ',pizza[i]['name']+' : '+str(pizza[i]['price']))
order = {}
print(' ')
while True:
    select = input('Please Select your Item :')
    condition = input('Do you want add toppings? [y or n] :')
    order[select] = pizza[select]
    if condition == 'n':
        break

sub_total=[]
for i in order.keys():
    sub_total.append(order[i]['price'])


bill=0
for i in sub_total:
    bill=bill+i
print(' ')
print('Total Amount = RS.',bill)






