import re

emails = [
    "test@gmail.com",
    "hello@yahoo",
    "user123@domain.com",
    "abc@.com",
    "my_mail@company.org"
]

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for email in emails:
    if re.match(pattern, email):
        print(email, "--> Valid)")
    else:
        print(email, "-- > Not Valid")