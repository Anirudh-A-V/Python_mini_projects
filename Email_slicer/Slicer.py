email = input("Enter the email id : ").strip()

username = email[:email.index('@')]
domain = email[email.index('@')+1:-4]

print(f"The username is '{username}' and the domain is '{domain}'")