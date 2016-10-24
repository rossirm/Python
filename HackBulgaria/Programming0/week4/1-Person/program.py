__author__ = 'Боян'
import datetime

person = {}
current_year = datetime.datetime.now().year

person["fist_name"] = input("Enter first name: ")
person["second_name"] = input("Enter second name: ")
person["third_name"] = input("Enter third name: ")
person["birth_year"] = input("Enter birth year: ")
person["current_age"] = current_year - int(person["birth_year"])

print(person)