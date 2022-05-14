email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
if domain_name == "gmail":
    print(username + "@" + domain_name + ".com")
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)