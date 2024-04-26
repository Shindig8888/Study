import requests

class UserGen:
    def __init__(self):
        self.firstname = input("\nWhat is your first name?\n").title()
        self.lastname = input("\nWhat is your last name?\n").title()
        while True:
            self.email_1 = input("\nWhat is your email?\n")
            self.email_2 = input("\nType your email again.\n")

            if self.email_1 == self.email_2:
                break
            else:
                print("\nEmail does not match. Please enter your email again.")
                continue

    def user_write(self):
        query = {
            "sheet": "users",
            "First Name": self.firstname,
            "Last Name": self.lastname,
            "Email": self.email_1
        }
        SPREAD_ENDPOINT = "https://sheetdb.io/api/v1/lie2kynwg51hl"
        response = requests.post(url=SPREAD_ENDPOINT, json=query)
        response.raise_for_status()
        print(response.text)