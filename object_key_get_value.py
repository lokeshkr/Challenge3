# nested object - using Python Dictionary to resolve the vaule of a key
obj = {"x1":{"y1":{"z1":"a1"}}}
# the function reads the object and using the dictionary to gather the value of the object of nested x,y,z
def val(obj):
 for x in obj.values():
  #print(x)
  for y in x.values():
   print("vaule is :" , *y.values())
  
if __name__ == '__main__':
 val(obj)
