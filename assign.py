"""
Module:      Basic of Big Data,
Module code; DSUO7315,
Task:        Individual Assignment,
Lecturer:    Mr.Kelvin Rweshobora,
@author:     Asha Melius Kisonga

"""
product_list=[('Product_A', 150), ('Product_B', 200), ('Product_A', 120), ('Product_C', 180), ('Product_B', 250), ('Product_A', 200), ('Product_C', 119), ('Product_A', 94), ('Product_B', 190), ('Product_D', 71), ('Product_D', 129), ('Product_C', 150), ('Product_C', 251), ('Product_D', 106), ('Product_E', 113), ('Product_E', 228), ('Product_B', 156), ('Product_B', 267), ('Product_E', 175), ('Product_B', 265), ('Product_C', 286), ('Product_C', 151), ('Product_C', 258), ('Product_D', 220), ('Product_D', 96), ('Product_C', 164), ('Product_E', 252), ('Product_A', 156), ('Product_C', 79), ('Product_A', 218), ('Product_D', 287), ('Product_C', 50), ('Product_C', 113), ('Product_C', 250), ('Product_B', 248), ('Product_A', 57), ('Product_D', 56), ('Product_C', 117), ('Product_B', 277), ('Product_B', 73), ('Product_E', 214), ('Product_E', 99), ('Product_A', 244), ('Product_D', 256), ('Product_C', 72), ('Product_C', 95), ('Product_C', 55), ('Product_C', 172), ('Product_E', 187), ('Product_D', 205), ('Product_C', 225), ('Product_A', 206), ('Product_D', 141), ('Product_A', 69), ('Product_E', 273), ('Product_E', 80), ('Product_B', 80), ('Product_E', 256), ('Product_D', 98), ('Product_A', 224), ('Product_D', 128), ('Product_E', 295), ('Product_C', 108), ('Product_B', 268), ('Product_B', 154), ('Product_B', 112), ('Product_D', 55), ('Product_D', 156), ('Product_D', 290), ('Product_D', 289), ('Product_D', 197), ('Product_D', 98), ('Product_E', 108), ('Product_D', 73), ('Product_B', 254), ('Product_B', 156), ('Product_A', 146), ('Product_B', 182), ('Product_A', 287), ('Product_B', 183), ('Product_B', 111), ('Product_A', 280), ('Product_B', 173), ('Product_E', 104), ('Product_A', 265), ('Product_A', 198), ('Product_B', 92), ('Product_C', 170), ('Product_E', 53), ('Product_D', 262), ('Product_E', 197), ('Product_D', 138), ('Product_E', 269), ('Product_A', 123), ('Product_E', 187), ('Product_C', 290), ('Product_E', 182), ('Product_C', 161), ('Product_C', 280), ('Product_E', 93), ('Product_A', 158), ('Product_A', 120), ('Product_A', 147), ('Product_A', 95), ('Product_C', 187), ('Product_A', 225)]

## for printing all datasets provided. 
print(*product_list)

#import default dictionary
from collections import defaultdict
product_count=defaultdict(int)
product_total=defaultdict(int)

# for perfoming occurences of each unique product
for product,amount in product_list:
    product_total[product] +=amount
    product_count[product] +=1
    
print("the occurance of each unique product are as follows:")
for product, count in product_count.items():
    print(f"{product}:{count}")
    
    
#average sale amount
print("\naverage sale amount for each product ;")
for  product,total in product_total.items():
    average =total/product_count[product]
    print(f"{product}:{average:.2f}")
    
#top N product by sale amount 
N=5
top_product=sorted(product_total.items(),key=lambda x:x[1],
reverse=True)[:N]
print(f"\ntop {N} product by sale amount:")
for product,total_sales in top_product:
    print(f"{product}:{total_sales}")
    
""" End """



