print("welcome to my game \n pro gamer!")
name = input("enter your name: ")
age = float(input("enter your age:"))
if age >= 14 and age < 60:
    print(name + " you are eligible for playing this game")
    print("lets start the game....")
    f_s = input(
        "there is a jungle and a sea \nwould you like to swim in the sea or walk around jungle(swim/walk)? ").lower()
    if f_s == "swim":
        print("sorry.. you were eaten by shark and dead")
    else:
        print("you crossed the jungle safely lets continue")
        v_s = input(
            "after crossing jungle due to some glitches \n you entered PUBG map \n which map would you like to enter(miramer/erangel)?")
        if v_s == "erangel":
            print("you entered erangel map....")
            b_s = input("would you like to pick up M416 or GROZA: ").upper()
            if b_s == "M416":
                print("you are out of ammo and enemy killed you")
            else:
                print("you sucessfull completed came ....\n see you in an other game")
        else:
            print("you came out of PUBG due to ban in india! and died due to \n fall from high location")
else:
    print(name + " sorry.... you are not eligible for this game")
