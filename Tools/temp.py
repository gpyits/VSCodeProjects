#snippet tester

a='ciaocomestai'
l=['ciao', 'come', 'c', 'stai']
result=''
for word in l:
    result+=word if result+word in a else ''
print(result)













#actually useful, keep for ltr
# def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
#     contact = {"name": name, "email": email, "telefono": telefono}
#     return contact

# def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
#     if name!=None:
#         dictionary["name"] = name
#     elif email!=None:
#         dictionary["email"] = email
#     elif telefono!=None:
#         dictionary["telefono"] = telefono

# contact=create_contact('name', 'a@email.com', 123455)
# update_contact(contact, 'name2', 'email', 0)
# print(contact)