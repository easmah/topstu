class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

    def print_style(self):
        print(f"Just testing")