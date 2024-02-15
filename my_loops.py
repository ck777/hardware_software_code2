def get_menu(): #used  for display or menu
    menu_dict = {
    '1':'apples' ,
    '2':'bananas',
    '3':'cheeries',
    '4':'pears',
    'x':'done_ordering'
  }
  return menu_dict

def display_menu(menu_dict):
    for items, values in menu_dict.items():
        print (items+"."+values.replce('_',' ').capitalize())
    menu_selection = input("what woukd you lke to buy?").upper()

    print ("you selected {}".format(menu_dict[menu_selection]))

    return menu_selection

def display_purchases (items_list):
    del items_list[-1]
    print ("you purchased {} items".format(len(items_list)), end= " ")
    print(*items_list, sep = ", ",end= ".\n")

def main ():
    menu _selection = ''
    items_list = []
    while menu_selection !='X':
        menu_dict = get_menu()
        menu_selection =display_menu (menu_dict)
        items_list.append(menu_dict[menu_selection])
        input ("hit enter to continue!!")

    display_purchases(items_list)

if __name__ == "__main__":
    main()
