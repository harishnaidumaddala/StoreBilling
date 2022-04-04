import json
def load_bill ( item , itemCategory , quantityPrice , tax , finalPrice ) :
    billing_details = {
    "item": None,
    "itemCategory": None,
    "tax" : None,
    "finalPrice" : None  
    }
    billing_details['item'] = item
    billing_details['itemCategory'] = itemCategory
    billing_details['tax'] = tax
    billing_details['quantityPrice'] = quantityPrice
    billing_details['finalPrice'] = finalPrice
    billing_list.append(billing_details)
    return(billing_list)
 

input_file = open ('jsonIn.txt')
json_array = json.load(input_file)
store_list = []
billing_list=[]
total = 0
cloth = 0
totalTax = 0


    
for item in json_array:
    store_details = {
    "item": None,
    "itemCategory": None,
    "quantity": None,
    "price": None
    }
 
    store_details['item'] = item['item']
    store_details['itemCategory'] = item['itemCategory']
    store_details['quantity'] = item['quantity']
    store_details['price'] = item['price'] 
    store_list.append(store_details)
    
    
for items in store_list:
    if ( items['itemCategory'] == 'Food' or items['itemCategory'] == 'Medicine' ) :  
        quantityPrice = ( items['quantity'] * items['price'] )
        tax =  quantityPrice * (0.05) 
        finalPrice = quantityPrice + tax
        total = total + finalPrice 
        totalTax = totalTax + tax
        billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
        
    if ( items['itemCategory'] == 'Clothes') :
        cloth = cloth + (items['quantity'] * items['price'] )
        if ( cloth <= 1000) :  
            quantityPrice = ( items['quantity'] * items['price'] )
            tax =  quantityPrice * (0.05) 
            finalPrice = quantityPrice + tax
            total = total + finalPrice 
            totalTax = totalTax + tax
            billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
           
        if ( cloth > 1000) :  
            quantityPrice = ( items['quantity'] * items['price'] )
            tax =  quantityPrice * (0.12) 
            finalPrice = quantityPrice + tax
            total = total + finalPrice 
            totalTax = totalTax + tax
            billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
           
    if ( items['itemCategory'] == 'Music' ) : 
        quantityPrice = ( items['quantity'] * items['price'] )
        tax =  quantityPrice * (0.03) 
        finalPrice = quantityPrice + tax
        total = total + finalPrice 
        totalTax = totalTax + tax
        billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
    if ( items['itemCategory'] == 'Imported' ) :
        quantityPrice = ( items['quantity'] * items['price'] )
        tax =  quantityPrice * (0.18) 
        finalPrice = quantityPrice + tax
        total = total + finalPrice 
        totalTax = totalTax + tax
        billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
    if ( items['itemCategory'] == 'Books' ) : 
        quantityPrice = ( items['quantity'] * items['price'] )
        tax =  quantityPrice * (0.00) 
        finalPrice = quantityPrice + tax
        total = total + finalPrice 
        totalTax = totalTax + tax
        billing_list = load_bill( items['item'] , items['itemCategory'] , quantityPrice , tax ,finalPrice )
for items in billing_list :
    print(items)
print("Total amount : ", total) 
if total >= 2000  :
    total = total - ( total * 0.05 )
 
bill_details = {
            "totalAmount": total,
            "totalTax": totalTax,
        }
print ("total tax :", tax)       
print("Total amount payable : ", total) 
           
    
        

    
        
