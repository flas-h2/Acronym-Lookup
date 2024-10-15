# TJ Szoszorek

def dictionary():
    acronym_dictionary = {"BRB": "Be right back", "LOL": "Laugh out loud",
                          "AFK": "Away from keyboard", "BFF": "Best friends forever", "ASAP": "As soon as possible"}
    return acronym_dictionary


def dict_search(user_acro, dictionary):
    if user_acro in dictionary:
        print(dictionary[user_acro])
        return dictionary
    else:
        while True:
            add_new = str(input(
                f"{user_acro} is not in the dictionary. Would you like to add it? (yes/no): ")).lower().strip()
            if add_new == "yes":
                meaning_in = str(input(f"Enter the meaning for {user_acro}: "))
                dictionary[user_acro] = meaning_in
                return dictionary
            elif add_new == "no":
                main()
            else:
                print("Invalid input, try again!")


def main():
    acro_dict = dictionary()

    while True:
        enter_acro = str(
            input("Enter an acronym (or Q to quit): ")).upper().strip()

        if enter_acro == "Q":
            print("Goodbye!")
            quit()
        elif enter_acro == "LIST":
            print(acro_dict)
        else:
            acro_dict = dict_search(enter_acro, acro_dict)


if __name__ == "__main__":
    main()
