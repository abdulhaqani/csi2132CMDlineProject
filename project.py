import psycopg2
import random

hostname = 'ec2-54-147-209-121.compute-1.amazonaws.com'
username = 'gtvyqkynqletdx'
password = 'b0659bbd8435b4ca5d59c84b5e7c2fa25efcb63a728ae7d4621457dd7da91dab'
database = 'd2kmmk80gp3q7j'

myConn = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
loop = True

cur = myConn.cursor()
while (loop):
  selection = input('What would you like to do? \nTo do each whichever you intend, print the letter associated with your command \nAdd listing: a\nView Available Listings: v \nDelete: d\nExit: e\n')
  if (selection == 'a' or selection == 'A'):
    print("For each element in the entry, provide it's corresponding value \n")
    propertyId = input("Input a number password for your property Id: ")
    hostId = input("\nHost id: ")
    price = input("\nPrice: ")
    priceId = random.randint(1, 1000000)

    uniqueSpace = input("\nis it a unique space? (y/n): ")
    while (uniqueSpace != 'y' and uniqueSpace != 'Y' and uniqueSpace !='n' and uniqueSpace !='N'):
      uniqueSpace = input("please input y or n for yes or no")
    if (uniqueSpace == 'y' or uniqueSpace == 'Y'): 
      uniqueSpace = True
    else: 
      uniqueSpace = False

    sharedRoom = input("\nis it a shared Room? (y/n): ")
    while (sharedRoom != 'y' and sharedRoom != 'Y' and sharedRoom !='n' and sharedRoom !='N'):
      sharedRoom = input("please input y or n for yes or no")
    if (sharedRoom == 'y' or sharedRoom == 'Y'): 
      sharedRoom = True
    else: 
      sharedRoom = False

    privateRoom = input("\nis it a private Room? (y/n): ")
    while (privateRoom != 'y' and privateRoom != 'Y' and privateRoom !='n' and privateRoom !='N'):
      privateRoom = input("please input y or n for yes or no")
    if (privateRoom == 'y' or privateRoom == 'Y'): 
      privateRoom = True
    else: 
      privateRoom = False
    
    availableDates = "Null"

    query = "INSERT INTO property(property_id, guest_id, host_id, unique_space, shared_room, private_room, available_dates) VALUES ({}, null, {}, {}, {}, {}, {});".format(propertyId, hostId, uniqueSpace, sharedRoom, privateRoom, availableDates)
    print(query)
    cur.execute(query)

    query = "INSERT INTO price(price_id ,host_id, property_id, price) VALUES ({}, {}, {}, {});".format(priceId, hostId, propertyId, price)

    cur.execute(query)

  elif (selection == 'v' or selection == 'V'):
    cur.execute("SELECT price, property_id, host_id FROM Price")
    for price, property_id, host_id in cur.fetchall():
      print ('Property ID: '+ str(property_id) + ', Host_id: ' + str(host_id) + ', Price: ' + str(price))
  elif (selection == 'd' or selection == 'D'):
    propertyId = input("Input a the password for the propertyId you want do delete: ")
    query = "DELETE FROM property WHERE property_id = " + str(propertyId) + ";"
    query2 = "DELETE FROM price WHERE property_id = " + str(propertyId) + ";"
    cur.execute(query)
    cur.execute(query2)
  elif (selection == 'e' or selection == 'e'):
    loop = False
  
print('Goodbye')