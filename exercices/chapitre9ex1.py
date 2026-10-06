from helpers.validation import valider_email, valider_password
print(f"imad@test.com -> {valider_email("imad@test.com")}")
print(f"saratest.ca -> {valider_email("saratest.ca")}") 

print(valider_password("12345678"))
print(valider_password("123"))
