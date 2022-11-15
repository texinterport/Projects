#!/usr/bin/env python
# coding: utf-8

# In[3]:


MENU_PROMPT = "\nEnter 'a' to add a rum, 'l' to see your rums, 'f' to find a rum by title, or 'q' to quit: "
rums = []


def add_rum():
    brand = input("Enter the rum brand: ")
    region = input("Enter the rum region: ")
    variety = input("Enter the rum variety: ")

    rums.append({
        'brand': brand,
        'region': region,
        'variety': variety
    })


def show_rums():
    for rum in rums:
        print_rum(rum)


def print_rum(rum):
    print(f"Brand: {rum['brand']}")
    print(f"Region: {rum['region']}")
    print(f"Variety: {rum['variety']}")


def find_rum():
    search_brand = input("Enter rum brand you're looking for: ")

    for rum in rums:
        if rum["brand"] == search_brand:
            print_rum(rum)


user_options = {
    "a": add_rum,
    "l": show_rums,
    "f": find_rum
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        #if selection == "a":
            #add_rum()
        #elif selection == "l":
            show_rums()
        #elif selection == "f":
            #find_rum()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()


# In[1]:


MENU_PROMPT = "\nEnter 'a' to add a rum, 'l' to see your rums, 'f' to find a rum by title, or 'q' to quit: "
rums = []


def add_rum():
    brand = input("Enter the rum brand: ")
    region = input("Enter the rum region: ")
    variety = input("Enter the rum variety: ")

    rums.append({
        'brand': brand,
        'region': region,
        'variety': variety
    })


def show_rums():
    for rum in rums:
        print_rum(rum)


def print_rum(rum):
    print(f"Brand: {rum['brand']}")
    print(f"Region: {rum['region']}")
    print(f"Variety: {rum['variety']}")


def find_rum():
    search_brand = input("Enter rum brand you're looking for: ")

    for rum in rums:
        if rum["brand"] == search_brand:
            print_rum(rum)


user_options = {
    "a": add_rum,
    "l": show_rums,
    "f": find_rum
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()


# In[ ]:




