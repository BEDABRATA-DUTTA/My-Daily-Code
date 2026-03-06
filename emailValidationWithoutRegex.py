emails = [
    "test@gmail.com",
    "hello@yahoo",
    "user123@domain.com",
    "abc@.com",
    "my_mail@company.org"
]

for email in emails:
    if "@" in email and "." in email:
        parts = email.split("@")
        print(parts)
        
        if len(parts) == 2 and parts[0] != "" and "." in parts[1]:
            print(email, "- Yes (Valid)")
        else:
            print(email, "- Not Valid")
    else:
        print(email, "- Not Valid")