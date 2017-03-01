# Emerging-Coders
def airbnb_cost(nights):
    return 140*nights
def plane_cost(city):
    if city=="Maldives":
        return 583
    if city=="Bora Bora":
        return 220
    if city=="Rome":
        return 22
    if city=="Aspen":
        return 475
def rental_cost(days):
    return 100*days
    if days >= 7:
        return (100*days)-50
    elif days >= 3:
        return (100*days)-20
def spending_money(cost):
    return cost
def trip_cost (city,days,cost):
    return rental_cost(days)+airbnb_cost(days)+plane_cost(city) + spending_money(cost)

print trip_cost("Maldives",5,600)
