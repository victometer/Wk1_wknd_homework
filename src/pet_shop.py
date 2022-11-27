# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name (shop_name):
    return shop_name['name'] 

def get_total_cash (pet_shop):
    # total_cash = pet_shop["admin"]["total_cash"]
    # return total_cash
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash (pet_shop, added_cash):
    # total_cash['admin']['total_cash'] + added_cash
    pet_shop["admin"]["total_cash"] += added_cash

def add_or_remove_cash (pet_shop, removed_cash):
    # total_cash['admin']['total_cash'] + added_cash
    pet_shop["admin"]["total_cash"] += removed_cash

def get_pets_sold (pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold (pet_shop, num):
    pet_shop['admin']['pets_sold'] += num
    # do i need to return the new value?

def get_stock_count (pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed (pet_shop, breed):
    all_pets = [] 
    for pet in pet_shop['pets']:
        if pet['breed'] == None:
            return None
        if pet['breed'] == breed: 
            all_pets.append(pet['breed'])
    return all_pets

# still wondering why just a count=0 if petshop[pets][breed] == breed, 
# count+=1 doesnt work? Needs a for loop to go through them all, right?
# and pets is a list, so cant represent it as above, so instead we need to
# make a new list where the counted pets would go, but we don't need a count
# as whenever new items get added to our empty list, the computer will count
# them itself, right?


def find_pet_by_name (pet_shop, name):
    pets = []
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pets.append(pet['name'])
            return pet
    return None


def remove_pet_by_name (pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].remove(pet)


def add_pet_to_stock (pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return len(pet_shop['pets'])

def get_customer_cash (customers):
    return customers['cash']

def remove_customer_cash(customers, num):
    remaining_cash = customers['cash'] - num # += is a sleeker version of this
    customers['cash'] = remaining_cash # because it subtracyts the cash as 
    return customers['cash'] # well as overwrites the old value with the new
    # inside the dictionary.

def get_customer_pet_count (customers):
    return len(customers['pets'])


def add_pet_to_customer (customers, new_pet):
    customers['pets'].append(new_pet)


def customer_can_afford_pet(customers, new_pet):
    if customers['cash'] >= new_pet['price']:
        return True
    else:
        return False

def sell_pet_to_customer (pet_shop, pet, customers):
    if pet == None:
        return None
    if customers['cash'] >= pet['price']:
        pet_shop['pets'].remove(pet)
        pet_shop['admin']['pets_sold'] += 1 
        pet_shop['admin']['total_cash'] += pet['price']
        customers['cash'] += (-pet['price'])
        customers['pets'].append(pet)
    
    # pet_list = []
    # for any_pet in pet_shop:
    #     if any_pet['name'] == pet['name']:
    #         pet_list.append(pet)
    #     else:
    #         return None
    #     if customers['cash'] >= pet['price']:
    #         pet_shop['pets'].remove(pet)
    #         pet_shop['admin']['pets_sold'] += 1 
    #         pet_shop['admin']['total_cash'] += pet['price']
    #         customers['cash'] += (-pet['price'])
    #         customers['pets'].append(pet)
    #
    # for pet in pet_shop['pets']: #might need a pets[]
    #     if pet == pet['name'] and customers['cash'] >= pet['price']:
    #         pet_shop['pets'].remove(pet)
    #         pet_shop['admin']['pets_sold'] += 1 #how to make this more usable?
    #         pet_shop['admin']['total_cash'] += pet['price']
    #         customers['cash'] += (-pet['price'])
    #         customers['pets'].append(pet)
    #         # return len(customers['pets'])  

# find pet by Name
# check if customer can afford pet
# if true change:
#     pet count in Store
#     cash in Store
#     cash in customer
#     pet in customer




