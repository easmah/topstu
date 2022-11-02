
from Exercises.classesExercise.privileges import Privileges


class user:

    def __init__(self, first_name, last_name, age, country_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country_of_birth = country_of_birth
        self.login_attempt = 0

    def describe_user(self):
        print(f"User Details:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Country of Birth: {self.country_of_birth}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


'''
emmanuel = User('Emmanuel', 'Asmah', 27, 'Ghana')
emmanuel.describe_user()
emmanuel.greet_user()
emmanuel.increment_login_attempts()
emmanuel.increment_login_attempts()
emmanuel.increment_login_attempts()
print(f"Login attempt: {emmanuel.login_attempt}")
emmanuel.reset_login_attempts()
print(f"Reset Login: {emmanuel.login_attempt}")'''


class Admin(user):

    def __init__(self, first_name, last_name, age, country_of_birth, privileges):
        super().__init__(first_name, last_name, age, country_of_birth)
        self.privilege = Privileges(privileges)

    """def show_privileges(self):
        print("Admin Privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")"""


admin = Admin('Emmanuel', 'Asmah', 27, 'Ghana', ['can add post', 'can delete post', 'can ban user'])
admin.describe_user()
admin.privilege.show_privileges()
admin.privilege.print_style()
