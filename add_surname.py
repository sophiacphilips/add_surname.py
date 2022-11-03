# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 11/2/22
# This code is designed to pull first names starting with "K" from a list of names and add the surname "Kardashian" to them

def add_surname(first_names):
    '''defining to add surname of Kardashian to names in first_names list that start with K'''
    return [n + " Kardashian" for n in first_names if n[0].upper()=="K"]
#n is holding the place for first name to go
#n in first names pulls names in first_names list
#n[0] denotes first letter in name (place 0) and if it's equivalent to uppercase "K" then it is to be added to last name kardashian


#test
#first_names= ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
#result= add_surname(first_names)
#print(result)
