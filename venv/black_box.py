def main():
    LIST_OF_OPTIONS = ["A","B","C","D"]
    FINAL_DICT = {"pole_1":"A","pole_2":"B","pole_3":"C","pole_4":"D"}
    guessing_dict = {"pole_1":"_","pole_2":"_","pole_3":"_","pole_4":"_"}
    user_choices = []

    while guessing_dict != FINAL_DICT:
        user_input = int(input("Zadej číslo od 1 do 8: "))
        user_choices.append(user_input)
        # VKLÁDÁNÍ
        if user_input == 1:                     # A na pole 4
            guessing_dict ["pole_4"] = "A"
        elif user_input == 2:                   # B na pole 3
            guessing_dict["pole_3"] = "B"
        elif user_input == 3:                   # C na pole 3
            guessing_dict["pole_2"] = "C"
        elif user_input == 4:                   # D na pole 4
            guessing_dict["pole_1"] = "D"
        # PŘEHAZOVÁNÍ
        elif user_input == 5:                   # prohoď znaky na polí 1 a 2
            a = guessing_dict.get("pole_1")
            b = guessing_dict.get("pole_2")
            guessing_dict["pole_1"] = b
            guessing_dict["pole_2"] = a
        elif user_input == 6:                   # # prohoď znaky na polí 2 a 3
            a = guessing_dict.get("pole_2")
            b = guessing_dict.get("pole_3")
            guessing_dict["pole_2"] = b
            guessing_dict["pole_3"] = a
        elif user_input == 7:                   # prohoď znaky na polí 4 a 5
            a = guessing_dict.get("pole_3")
            b = guessing_dict.get("pole_4")
            guessing_dict["pole_3"] = b
            guessing_dict["pole_4"] = a
        elif user_input == 8:                   # reset
            guessing_dict["pole_1"] = "_"
            guessing_dict["pole_2"] = "_"
            guessing_dict["pole_3"] = "_"
            guessing_dict["pole_4"] = "_"

        print("-"*20)
        print("Pokus číslo: ", len(user_choices))
        print("Hráč zadal: ", user_choices)
        print("guessing dict: ", guessing_dict.values()) # vrací list hodnot

if __name__ == "__main__":
    main()