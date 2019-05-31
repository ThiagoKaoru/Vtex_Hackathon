
shop_list = ['banana','uva']
cashier_list = [(2,0),(3,0),(4,0),(5,0),(6,0)]
travel_list = [(0,0)]
traveled = (0,0)
shelf_list = [(2,2),(3,2),(2,3),(3,3),(2,4),(3,4),(2,5),(3,5),(6,2),(5,2),(6,3),(5,3),(6,4),(5,4),(6,5),(5,5),(8,2),(9,2),(8,3),(9,3),(8,4),(9,4),(8,5),(9,5), (11,2),(12,2),(11,3),(12,3),(11,4),(12,4),(11,5),(12,5),(14,2),(15,2),(14,3),(15,3),(14,4),(15,4),(14,5),(15,5)]
#movimentacao pelo mercado
dic_trav={
    "up" = (travel_list[0],travel_list[1]+1)
    "down" = (travel_list[0],travel_list[1]-1,)
    "left" = (travel_list[0]-1,travel_list[1])
    "down" = (travel_list[0]+1,travel_list[1])
}
#Shop_list e a lista de compras do consumidor
market_map = {
    'banana' : (2,5),
    'chocolate' : (5,3),
    'uva' : (6,2)}
#market_map e a localizacao de cada produto no mercado
list_location = []
for product in shop_list:
    if product in market_map:
        list_location.append(market_map[product])


if travel_list==(0,0):
    for product in list_location:
        if product[0][0] > travel_list[0][0]:
            traveled= dic_trav["up"]
            travel_list.append(traveled)
        elif product[0][0] == travel_list[0][0] &     
        elif product[0][1]> travel_list[0][1]:
            traveled= dic_trav["right"]



