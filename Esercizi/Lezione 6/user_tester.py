from user import *

privileges1=Privileges(['can add post', 'can delete post', 'can ban user'])
admin2=Admin('Mario', 'Mario', privileges1)
admin2.privileges.show_privileges()