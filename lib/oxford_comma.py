def oxford_comma(items):
   if isinstance(items, list) and len(items) == 1:
    return items[0]
   elif isinstance(items, list) and len(items) == 2:
    new_list = " and ".join(items)
    return new_list
       
   return items

fruit_list =  oxford_comma(["kiwi"])
updated_fruit_list = oxford_comma(["kiwi", "durian"])
print(updated_fruit_list)
print(fruit_list) 
