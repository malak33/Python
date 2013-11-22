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
    
def rental_car_cost(rental_days):
    if rental_days <3:
        return 40 * rental_days
    elif rental_days < 7:
        return 40 * rental_days - 20
    else:
        return 40 * rental_days - 50
        
def trip_cost(city,days,spending_money):
    trip_cost = plane_ride_cost(city) +  rental_car_cost(days) + hotel_cost(days) + spending_money
    return trip_cost
