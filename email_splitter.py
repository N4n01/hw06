#Modified code from phone number task.

def clean_email(text) :
    text = text.replace(" ", "")
    return text

def is_valid(email) :
    position = email.rfind("@")
    if "@" not in email or email[:position] == "" or email[position+1:] == "" :
        return None
    else :
        return email

def main() :
    while True :
        email = input("Email: ")
        if email == "q" :
            break
        email = clean_email(email)
        position = email.rfind("@")
        if is_valid(email) == None: 
            print("Invalid email.")
        else :
            print("Username: ", email[:position])
            print("Domain: ", email[position+1:])

main()