def oxford_comma(items):
   if isinstance(items, list) and len(items) == 1:
    return items[0]

   return items

fruit_list =  oxford_comma(["kiwi"])
print(fruit_list) 
