#user profile data


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

#concatenate first and last nane

full_name = first_name + " " + last_name

#full profile of user

user_profile = f"{full_name} is {age} years old,lives in {city} and works as a {occupation}."

#Add escape characters to include quotation mark and a new line

user_info = "\"Profile Information:\"\n" + user_profile

modified_name = full_name.upper()
modified_profile = user_profile.replace("a", "an") if occupation.startswith(('a','e','i','o','u')) else user_info

#display user profile

print("**** User Profile ****")
print(modified_name)
print(modified_profile)
print("*********")


