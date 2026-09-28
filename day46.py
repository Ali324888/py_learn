import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("Debug Message")
# logging.info("Program Started")
# logging.warning("Low balance")
# logging.error("Payment failed")
# logging.critical("System Failure")


# logging.basicConfig(filename="app.log",level=logging.INFO)

# logging.info("Application started")
# logging.info("User logged in")
# logging.warning("Low balance")
# logging.error("Payment failed")

# logging.basicConfig(level=logging.DEBUG)

# def withdraw(balance, amount):
#     if amount <= 0 :
#         logging.warning("Invalid amount")
#     elif amount > balance:
#         logging.error("Insufficient balance")
#     else:
#         logging.info("Successfull withdrawl")

# withdraw(15000,2000)

logging.basicConfig(filename="login.log",level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def login(username, password):
    if username != "admin":
        logging.error("Unknown user: %s", username)
    elif password != "1234":
        logging.warning("Invalid password for user admin")
    else:
        logging.info("User admin logged in successfully")


login("abc", "123")