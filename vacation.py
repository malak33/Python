def hotel_cost(nights): 
    cost = 140 * nights
    return cost
    
def plane_ride_cost(location):
    if location.lower() == "charlotte":
        return 183
    elif location.lower() == "tampa":
        return 220
    elif location.lower() == "pittsburgh":
        return 222
    else:
        return 475
    
def rental_car_cost(days):
    if days <3:
        return 40 * days
    elif days < 7:
        return 40 * days - 20
    else:
        return 40 * days - 50
