user_input = input("Which birthday are you looking for? ")
family_member_birthday = {"Hems": "25th December", "Harain": "22nd Nov", "Noya": "24th March", "Vasud": "4th April"}
if user_input in family_member_birthday:
    print(family_member_birthday[user_input])
else:
    print(f"{user_input} not found in your app")
