
import pandas as pd

# making data frame
df = pd.read_csv("username-password.csv")
#username index
user_input = input("Type the username:")

index = df.index
condition = df["username"] == user_input
user_indices = index[condition]
user_indices_list = user_indices.tolist()

print(user_indices_list)

#password index

pass_input = input("Type the password:")

index = df.index
condition = df["password"] == pass_input
pass_indices = index[condition]
pass_indices_list = pass_indices.tolist()
print(pass_indices_list)

if user_indices_list == pass_indices_list:
    print("Username and password is correct, you logged in")
else:
    print("The username or password is incorrect")

