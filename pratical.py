 # define the menu of restaurtant

 # menu= {
 #     "coffe" : 30,
 #     "tea" : 10,
# # # # # # # # # # # # # # # # # #     "pasta": 40,
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     "burger": 50,
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     "sandwich" : 60,
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("welcome to python restaurtant")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("coffe:RS30,\n tea:RS10,\n pasta:RS40,\n burger:RS50,\n sandwich:RS60,\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # order_total = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # item_1 = input("Enter the iteam which you want to order =")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if item_1 in menu:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     order_total += menu[item_1]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(f"your item {item_1} has been add to your order")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(f"order item {item_1} is not available yet")    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # another_order = input("do you want to add another item? (yes/no)")    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # if another_order == "yes":
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     item_2 = input("Enter the name of second item=")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if item_2 in menu:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         order_total += menu[item_2]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(f"your item {item_2} has been add to your order")
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(f"order item {item_1} is not available yet") 
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(f"total amount to items to pay is {order_total}")   




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # email silcer:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("welcome to the email silcer")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # email=input("Enter your email address:").strip()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # username = email[0:email.index('@')]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # domain = email[email.index('@')+1:]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('username-',username)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('domain-',domain)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Name seprater

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("welcome to the person name seprater ")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # person = input("enter the person name:")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # firstname = person[0:person.index('#')]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # lastname = person[person.index('#')+1:]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('firstname-',firstname)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('lastname-',lastname)








# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("welcome to the email silcer")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # email = input("enter your address email:").strip()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # username = email[0:email.index('@')]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # domain = email[email.index("@")+1:-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("username-",username )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print("domain-",domain)

    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # hpcl = {"Petrol": 110, "Diesel": 95}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # iocl = {"Petrol": 109, "Diesel": 96}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # bpcl = {"Petrol": 111, "Diesel": 94}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def compare_fuel(prices):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     for fuel in prices["HPCL"]:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(f"\n--- {fuel} Price Comparison ---")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         p = {
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             "HPCL": prices["HPCL"][fuel],
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             "IOCL": prices["IOCL"][fuel],
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             "BPCL": prices["BPCL"][fuel]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         cheapest = min(p, key=p.get)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print(p)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Cheapest:", cheapest)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # compare_fuel({"HPCL": hpcl, "IOCL": iocl, "BPCL": bpcl})

    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import random
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def check_tank_level():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     level = random.randint(0, 100)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Tank Level:", level, "%")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     if level < 20:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("⚠ Low Level Warning!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     elif level > 90:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("⚠ High Level Warning!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         print("Level Normal.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     check_tank_level()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     time.sleep(2)
    
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([[1,2],[3,4]])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(type(arr))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(np.__version__)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import  numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array((1,2,34,))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = np.array(23)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = np .array([1,2,3])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = np.array([[1,2,3],[3,4,5]])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = np.array([[[1,2,3],[2,4,4]]])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(c.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d.ndim)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3,4,], ndmin=5)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('number of dimensions:' ,arr.ndim

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # a = np.array(22)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # b = np.array([[1,3,5,6]])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # c = np.array([1,2,3,4])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # d = np.array([[[1,2,3],[1,4,4]]])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(a.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(b.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(c.ndim)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(d.ndim)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,3,2,3])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr[1:3])



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array(['apple', 'mango'])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr.dtype)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3,4,4],dtype='S')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(arr.dtype)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1.3,2.2,4.2])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # newarr = arr.astype(int)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(newarr)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(newarr.dtype)




# # # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,3,4])
# # # # # # # # # # # # # # # # # # # # # # # # # # # newarr = np.astype(bool)

# # # # # # # # # # # # # # # # # # # # # # # # # # # print(newarr)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(newarr.dtype)


# # # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,3,4,4])
# # # # # # # # # # # # # # # # # # # # # # # # # # x = arr.copy()
# # # # # # # # # # # # # # # # # # # # # # # # # # arr[1]= 343

# # # # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(x)


# # # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3,3])
# # # # # # # # # # # # # # # # # # # # # # # # # x = arr.view()
# # # # # # # # # # # # # # # # # # # # # # # # # arr[2]=22

# # # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # # print(x)



# # # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # # arr = np.array([2,1,1,1])
# # # # # # # # # # # # # # # # # # # # # # # # x = arr.copy()
# # # # # # # # # # # # # # # # # # # # # # # # x[0]=111

# # # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # # print(x)


# # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,3,4,5])

# # # # # # # # # # # # # # # # # # # # # # # x = arr.copy()
# # # # # # # # # # # # # # # # # # # # # # # y = arr.view()

# # # # # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # # # # print(y)


# # # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3,3])
# # # # # # # # # # # # # # # # # # # # # # # x = arr.copy()
# # # # # # # # # # # # # # # # # # # # # # # arr[2]=9

# # # # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # # # print(x)


# # # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # # arr = np.array([[1,1,2,2],[1,3,4,5,]])
# # # # # # # # # # # # # # # # # # # # # # print(arr.shape)

# # # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3])

# # # # # # # # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # # # # # # # # # print("shape of array;",arr.shape)


# # # # # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # # # # arr = np.array([1,2,3,4,5,6,6,7,8,7,9,0,])
# # # # # # # # # # # # # # # # # # # # newarr = arr.reshape(4,3)

# # # # # # # # # # # # # # # # # # # # print(newarr)


# # # # # # # # # # # # # # # # # # # import numpy as np 
# # # # # # # # # # # # # # # # # # # arr = np.array([1,2,4])

# # # # # # # # # # # # # # # # # # # for x in arr:
# # # # # # # # # # # # # # # # # # #     print(x)


# # # # # # # # # # # # # # # # # # import numpy as np 
# # # # # # # # # # # # # # # # # # arr = np .array([[1,1,2],[6,6,7]])

# # # # # # # # # # # # # # # # # # for x in arr:
# # # # # # # # # # # # # # # # # #     print(x)


# # # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # # arr = np.array([[1,3,5],[1,2,4]])

# # # # # # # # # # # # # # # # # for x in arr:
# # # # # # # # # # # # # # # # #   for y in x:
# # # # # # # # # # # # # # # # #     print(y)


# # # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # # arr = np.array([[[1,2,3],[4,5,6]],[[2,5,6],[6,7,8]]])
     
# # # # # # # # # # # # # # # # for x in arr:
# # # # # # # # # # # # # # # #     print(x)



# # # # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # # # arr1= np.array([1,2,3])
# # # # # # # # # # # # # # # arr2= np.array([4,5,5])

# # # # # # # # # # # # # # # arr= np.concatenate((arr1,arr2))
# # # # # # # # # # # # # # # print(arr)


# # # # # # # # # # # # # # import  numpy as np 

# # # # # # # # # # # # # # arr1 = np.array([1,2,4])
# # # # # # # # # # # # # # arr2 = np.array([4,6,3])

# # # # # # # # # # # # # # arr = np.array((arr1,arr2))
# # # # # # # # # # # # # # print(arr)

# # # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # # arr1 = np.array([1,2,3])
# # # # # # # # # # # # # arr2 = np.array([5,4,3])

# # # # # # # # # # # # # arr= np.stack((arr1,arr2),axis= 1)

# # # # # # # # # # # # # print(arr)


# # # # # # # # # # # # import numpy as np 

# # # # # # # # # # # # arr1 = np.array([1,2,3])
# # # # # # # # # # # # arr2 = np.array([4,5,6])

# # # # # # # # # # # # arr = np.hstack([arr1,arr2])

# # # # # # # # # # # # print(arr)

# # # # # # # # # # # import numpy as np 

# # # # # # # # # # # arr1= np.array([1,2,3])
# # # # # # # # # # # arr2= np.array([4,6,5])

# # # # # # # # # # # arr = np.vstack((arr1,arr2))
# # # # # # # # # # # print(arr)

# # # # # # # # # # import numpy as np 

# # # # # # # # # # arr1= np.array([1,3,4])
# # # # # # # # # # arr2= np.array([5,6,7])

# # # # # # # # # # arr= np.dstack((arr1,arr2))
# # # # # # # # # # print(arr)

# # # # # # # # # import numpy as np 

# # # # # # # # # arr= np.array([1,2,3,4,5,6])

# # # # # # # # # newarr =np.array_split(arr,12)
# # # # # # # # # print(newarr)

# # # # # # # # import numpy as np 

# arr= np.array(([1,2],[3,5]),[5,6])
# newarr= np.array_split(arr,3)

 # print(arr)


 # import numpy as np 

 # arr = np.array([1,2,3,4,5,6])
 # newarr= np.array_split(arr,4)

 # print(newarr)


 # import numpy as np 

 # arr = np.array([1,2,3,4,5,6])
 # newarr= np.array_split(arr,3)

 # print(newarr[0])
 # print(newarr[1])
 # print(newarr[2])


# import numpy as np 

 # arr = np.array([[1,2,4],[3,4,5],[5,6,7],[7,8,9]])
 # newarr= np.dsplit(arr,2,axis=1)

 # print(newarr)


 # import numpy as np 

 # arr = np.array([1,2,3,4,5,3,3,4])

 # x = np.where(arr==4)
 # print(x)

 # import numpy as np

 # arr = np.array([1,2,3,4,5,5,5,7])

 # x =np.searchsorted(arr,3)
 # print(x)

# import numpy as np 
# arr = np.array([2,3,4,1])
# print(np.sort(arr))



# import numpy as np 

# arr = np.array([23,45,33,44])

# x = [ True,True,False,True]
# newarr = arr[x]

# print(newarr)

# import pandas as pd 

# df = pd.read_csv("bats_information.csv")
# print(df )


# import pandas as pd 

# df = pd.read_csv("globalAirQuality.csv")
# print(df)


# import pandas as pd 

# mydatasets = {
#     'cars':['bmw','volvo','ford'],
#     'passings': [2,4,6] 
# }
# mydata = pd.DataFrame(mydatasets)
# print(mydata)


# import pandas as pd 

# mydatasets = {
#     "office":['Manager','employee','peon'],
#     'count':[2,68,5]
#     }
# mydata = pd.DataFrame(mydatasets)
# print(mydata)



# import pandas as pd 

# mydatasets = {
#    ' student':['shubham','anuj','ompraskash'],
#    'roll no ':[ 22, 27, 29],
#    'age':[22,25,23]
   
# }

# mystudent= pd.DataFrame(mydatasets)
# print(mystudent)

# import pandas as pd 

# print(pd.__version__)

# import pandas as pd 

# a = [1,7,3]
# mydata= pd.Series(a)
# print(mydata)

# import pandas as pd 

# a = ['shubham','ashish','omprakash']
# mydata = pd.Series(a)
# print(mydata)

# import pandas as pd 

# a = [1,3,5,5,]
# mydata = pd.Series(a)
# print(mydata[0])


# import pandas as pd 

# a= [1,32,44]
# myver = pd.Series(a, index= ['x','y', 'z'])

# print(myver)

# import pandas as pd 

# a = [1,5,6,8]
# myver = pd.Series(a,index=['1','2','3','4'])

# print(myver)


# import pandas as pd 

# a =  [ 11,44,66,33]
# myver =pd.Series(a, index= ['x','y','z','w'])

# print(myver["y"])

# import pandas as pd 

# calories = {"day1":420, "day2":220,"day3":320}

# myver = pd.Series(calories)
# print(myver)


# import pandas as pd 

# calories = {"day1":420,"day2":220,"day3":200}

# myver = pd.Series(calories, index=["day1", "day3"])
# print(myver)


# import pandas as pd 

# data = {
#     "calories": [230,300,111,233],
#     "duration":[10,20,80,24]    
# }
 
# myvar = pd.DataFrame(data, index = ['a','b','c','d'])

# print(myvar)



# import pandas as pd 

# student = {
#     "name":["shubham ","anuj","shasvat"],
#     "roll no ":[11,33,44,]
    
# } 

# mydata = pd.DataFrame(student)
# print(mydata)


# import pandas as pd 

# data = {
#     "calories" : [ 220,230,450],
#     "duration": [20,30,60]
    
# }

# df = pd.DataFrame(data)
# print(df.loc[2])


# import pandas as pd 

# data = {
#     "calories": [290,220,555],
#     "duration": [10,20,30]
    
# }

# df = pd.DataFrame(data, index= ["day1","day2", "day3"])
# print(df)

# import pandas as pd 

# df = pd.read_csv("bats_information.csv")
# print(df)

# import pandas as pd 

# student = {
#     "name":{
#         "1":"shubham",
#         "2":"aman",
#         "3":"smarth",
#         "4":"anuj"
#     },
    
#     "rollno":{
#         "1":10,
#         "2":12,
#         "3":20,
#         "4":15
   
#     },
#     "percentage":{
#         "1": 50,
#         "2": 60,
#         "3": 90,
#         "4": 89
#     }
    
# }

# df = pd.DataFrame(student)
# print(df)


# import pandas as pd 

# df = pd.read_csv('globalAirQuality.csv')
# newdf = df.dropna()
# print(newdf)

# import pandas as pd

# a = [1,2,4]
# data = pd.Series(a)
# print(data)



# import pandas as pd 

# df = pd.read_csv("Message Group - Product.csv")
# print(df)
# print("_____original data_____")
# print(df.isnull().sum())



# import pandas as pd 

# df = pd.read_csv("bats_information.csv")
# print(df)

# print(df.isnull())
# print(df.sum())


# import pandas as pd 
# a = ["shubham", "anuj", "himanshu"]
# df =pd.Series(a, index= ['a', 'b', 'c'])

# print(df)

# import pandas as pd 

# data = {
#     "name":["shubham", "kunal","harshit","anuj"],
#     "marks":[67,78,58,89]
# }

# df = pd.DataFrame(data , index=[1,2,3,4])
# df.rename(columns={'name': "ne"})
# print(df)

# import pandas as pd 

# student= {
    
#     "name":["shubham", "anuj","abhishek","punit","aryan"],
#     "marks":[88,97,"None",78,75],
#     "age":[22,23,"None",22,24],
#     "percentage" :[ 80, 91,"None",76,74]
# }

# df = pd.DataFrame(student)
# newdf= df.()
# print(newdf)



# import pandas as pd 
# import matplotlib.pyplot as plt

# df = pd.read_csv("globalAirQuality.csv")

# df.plot(kind ='hist')
# plt.show()


# import pandas as pd 
# import matplotlib.pyplot as plt

# data = {
#     "name":["shubham", "arav","rehan","harsh"],
#     "age":[22,34,55,55],
#     "marks":[89,54,88,78]
# }

# df = pd.DataFrame(data)
# print(df)

# df.plot()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel("report.xlsx")

# df.plot(kind="line", color=['blue', 'red', 'yellow'])

# plt.title('meta report')
# plt.xlabel('days')
# plt.ylabel('sales in week')
# plt.show()


# import pandas as pd 
# import matplotlib.pyplot as plt 


# df = pd.read_excel("report.xlsx")
# df.plot(kind= 'bar')

# plt.title("sales data reprt")
# plt.xlabel("days")
# plt.ylabel("sales in week")
# plt.show()

# import numpy as np 

# arr = np.array([1,1,2,30])
# print(arr)


# import pandas as pd 

# data = {
#     "name":["shubham","ronit"],
#     "age":[22,24]
# }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd

# a = [1,2,3,3]
# b = [ 1,2,33]
# myver = pd.Series(a:b)
# print(myver) 

# import pandas as pd 
# data = {
#      "petrol":[22,44,66,11],
#      "Diseal":[99,80,33,44]
#  }

# myver = pd.DataFrame(data, index=[1,2,3,4])
# print(myver)
# print(pd.__version__)

# import pandas as pd 

# a = [0,2,3,4,5,7]

# myver =pd.Series(a, index=[1,2,3,4,5,6,])
# print(myver)
# import pandas as pd 

# A= [122,44,55,666,33]

# data= pd.Series(A)
# print(data)
# print(data[1])

# import pandas as pd 

# calories = {"day1":220, "day2":120, "day3":330} 

# myver = pd.Series(calories)
# print(myver)

# import pandas as pd 

# data= {
#     'calories':[112,444,333],
#     'duration':[1,2,3] 
#        }
# mydata = pd.DataFrame(data, index=[1,2,3])
# print(mydata)

# import numpy as np 

# a = [1,2,3,3]

# myarr= np.array(a)
# print(myarr)

# import numpy as np

# arr = np.array([1,2,3,4,4])

# print(arr)
# print(np.__version__)
# print(type(arr))

# import numpy as np 

# arr = np.array([[67,99]])

# print(arr.ndim)


# import numpy as np

# arr = np.array([1,3,4,5], ndimn=5)
# print(arr)
# print("number of dimensions:",arr.ndim) 

# import numpy as np 

# arr = np.array([1,2,3,4])
# print(arr[1])

# import numpy as np

# arr = np.array([1,2,3,4,5,4,])
# print(arr[1]+arr[4])

# import numpy as np 

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print("2 element on 1 row:" ,arr[1,3])


# import numpy as np 

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print("last element on 1 row:" , arr[1 ,-1])


# import numpy as np 

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:])

# import  numpy as np 
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[0,1:3])

# import numpy as np 
# arr = np.array([1,3,4,5])

# print(arr)
# print(arr.dtype)


# import numpy as np 

# arr = np.array([1,2,3,4,5], dtype= 'S')

# print(arr)
# print(arr.dtype)


# import numpy as np 

# arr = np.array([1,2,3,4], dtype="i4")
# print(arr)
# print(arr.dtype)

# import numpy as np 

# arr  = np.array([1.1 ,2.3,2.1])
# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)


# import numpy as np 

# arr = np.array([1.2, 1.3,4.3])
# newarr = arr.astype(int)

# print(newarr)
# print(newarr.dtype)

# import numpy as np 

# arr  = np.array([1.1 ,2.3,2.1])
# newarr = np.astype('i')

# print(newarr)
# # print(newarr.dtype)

# import numpy as np 

# arr = np.array(["shubham", "anuj" , "harsh"])
# x = arr.copy()
# arr[1]= "govind"

# print(arr)
# print(x)

# import numpy as np 

# arr = np.array([1,2,3,54,5])
# x = arr.view()
# arr[3]= 77

# print(arr)
# print(x)

# import numpy as np 

# arr = np.array(["shubham", "anuj" , "harsh"])
# x = arr.view()
# arr[1]= "govind"

# print(arr)
# print(x)

# import numpy as np 

# arr = np.array([1,2,3,4,5])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# import numpy as np 
# arr = np.array([["shubham" , "anuj"]])

# print(arr.shape)


# import numpy as np 

# arr = np.array([1,2,3,4,5] , ndmin= 0)

# print(arr)
# print("shape of array:", arr.shape)


# import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8,9])

# newarr = arr.reshape(3,3)
# print(newarr)


# import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# newarr = arr.reshape(2,3,2)
# print(newarr)
 
 
# import numpy as np 

# arr = np.array([1,2,3,4,])

# for x in arr:
#     print(x)


# import numpy as np 

# arr = np.array([[1,2,3,4],[4,5,5,2]])
# for x in arr:
#     print(x)

# import numpy as np 

# arr = np.array([[1,2,3,4,4,]])

# for x in arr :
#     for y in x :
#         print(y)


# import numpy as np 

# arr = np.array([[[1,3,3],[4,5,5,],[3,5,6]]])

# for x in arr:
#     for y in x :
#         for z in y :
#             print(z)
            

# import numpy as np

# arr = np.array([[1,2],[1,2],[4,4],[7,8]]) 

# for x in np.nditer(arr):
#     print(x)

# import numpy as np 

# arr1 = np .array([1,2,3,4])
# arr2 = np.array([3,4,5,1])

# newarr = np.concatenate((arr1,arr2))
# print(newarr)

# import numpy as np 

# arr1  = np.array([[1,2],[2,3],[4,5],[7,8]])
# arr2 = np.array([[9,0],[8,8],[8,5],[1,1]])

# arr= np.concatenate((arr1 ,arr2))
# print(arr)


# import numpy as np 

# arr1 = np.array([1,2,2,2])
# arr2 = np.array([8,8,9,0])

# arr = np.stack((arr1,arr2))
# print(arr)


# import numpy as np 

# arr= np.array([1,2,3,3])
# newarr = np.array_split(arr,1)

# print(newarr)

# import numpy as np 

# arr = np.array([1,2,3,3,4,5,6,6])
# newarr = np.where(arr ==3)
# print(newarr)
# import numpy as np 

# arr = np.array([21,33,5,68])
# x = [True , True ,True , False]
# newarr = arr[x]
# print(newarr)




# import numpy as np 

# arr = np.array([22,44,55,66,88])
# x = [True,False,True,True,True]
# newarr = arr[x]
# print(newarr)


# import numpy as np 

# arr = np.array([44,54,23,40,56,88,67,42,23])
# filter_arr = []

# for elment in arr:
#     if elment > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
        
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)        



# import numpy as np 

# arr = np.array([1,2,3,3,4,5,6,7,8,9,10,11,12,33,445])
# filter_arr = []

# for element in arr:
#     if element< 10:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False) 
        
# newarr = arr[filter_arr] 

# print(filter_arr)
# print(newarr)        


# import numpy as np 

# arr = np .array([1,22,3,33,4,5,66,77,88])

# filter_arr = []


# for element in arr:
#     if element == 22:
#         filter_arr.append(True) 
#     else:
#         filter_arr.append(False)
        
# newarr = arr[filter_arr]


# print(filter_arr)
# print(newarr) 




# import numpy as np 
# arr = np.array([2,4,56,77,88,12])


# filter_arr = []

# for element in arr :
#     if element % 2 == 0 :
#         filter_arr.append(True)
#     else :
#         filter_arr.append(False)
        
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)    


# import pandas as pd 

# df = pd.read_csv('VehicleMPG.csv')
# print(df) 

# import pandas as pd 

# data = {
#     'name':['shubham', 'anuj'],
#     'age':[22,33]    
#     }     
# df = pd.DataFrame(data , index= (1,2)) 
# print(df)
# print(pd.__version__) 

# import pandas as pd 

# a = [1,2,3,]
# newver = pd.Series(a)
# print(a)


# import pandas as pd 

# data = ["shubham", "geed"]
# newver = pd.Series(data)
# print(newver)


# import pandas as pd 

# calories = {'day1':220 , 'day2': 210 , "day3":110}

# myver = pd.Series(calories)
# print(myver)

import pandas as pd
import matplotlib.pyplot as plt

data  = {
    "Name": ['shubham', 'anuj','amit','omprakash'],
    "age" : [22,55,66,33]   
    
}
df = pd.DataFrame(data)
df.plot(kind = 'hist',x = 'Name' , y = "age")
plt.show()