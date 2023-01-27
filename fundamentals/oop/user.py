# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.
# Add the display_info(self) method to the User class
# In the outer scope, create a user instance and call the display_info method to test
# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
# Make 2 more instances of the User class.
# Implement the spend_points(self, amount) method
# Have the first user spend 50 points
# Have the second user enroll.
# Have the second user spend 80 points
# Call the display method on all the users.
# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.

class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_pts = 0
        

    def display_info(self):
        print("-----------------------")
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is a rewards memeber : {self.is_rewards_member}")
        print(f"Total points: {self.gold_card_pts}")
        print("-----------------------")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print(f"{self.first_name} {self.last_name} is already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_pts = 200
        return self

    def spend_pts(self, amount):
        if self.gold_card_pts < amount:
            "You don't have enough points."
            return 
        self.gold_card_pts -= amount
        return self

user1= user("Conor", "Mcgregor", "Cmcgregor@yahoo.com", 32)
# user2= user("Jon", "Jones", "Jbonejones@gmail.com", 36)
# user3= user("Alex", "Perrera", "Atown@hotmail.com", 39)

# user1.enroll()
# user1.spend_pts(250)
# user2.enroll()
# user2.spend_pts(80)
# user1.display_info()
# user2.display_info()
# user3.display_info()
# user1.enroll()

user1.display_info().enroll().spend_pts(50).display_info()


