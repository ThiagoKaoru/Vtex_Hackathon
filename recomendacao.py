
shop_list = ['banana','uva']
cashier_list = [(2,0),(3,0),(4,0),(5,0),(6,0)]
#Shop_list e a lista de compras do consumidor
market_map = {
    'banana' : (1,0),
    'chocolate' : (2,0),
    'uva' : (3,0)}
#market_map e a localizacao de cada produto no mercado
list_location = []
for product in shop_list:
    if product in market_map:
        list_location.append(market_map[product])

print(list_location) 


