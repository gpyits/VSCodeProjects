from users import *

print('###TEST 1###')
privileges1=Privileges(['can add post', 'can delete post', 'can ban user'])
admin2=Admin('Mario', 'Mario', privileges1)
admin2.privileges.show_privileges()

from user import User
from admin_user import Privileges, Admin

print('###TEST 2###')
privileges1=Privileges(['can add post', 'can delete post', 'can ban user'])
admin2=Admin('Mario', 'Mario', privileges1)
admin2.privileges.show_privileges()