import random
import time

trip = random.choice(["Beach", "Safari"])


def print_slow(message):
    print(message)
    time.sleep(2)


def intro():
    print_slow("Welcome to the " + trip)
    print_slow("We are glad you chose to be here.")
    print_slow("We are hoping your time here will be memorable.")
    print_slow("Have Fun!")


def valid_response(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_slow("Invalid Response!! Please try again")
    return response


def safari_trip():
    print_slow("Welcome to the National Park.")
    response1 = valid_response("Please choose between Museum and Drive \n",
                               "drive", "museum")
    if "drive" in response1:
        print_slow("You chose Drive.")
        print_slow("Welcome to the home of The Big Five")
        print_slow("You will see Lions, Elephants, Buffalos, "
                   "Rhinos and Leopards in their natural habitats."
                   "Feel free to take pictures.")
        print_slow("Lets go on a drive around the national park.")
        print_slow("The tour shuttle pulls up by the entrance")
        print_slow("Your tour begins...")
        print_slow("You drive down the street and you see a "
                   "Buffalo in the nearby bush.")
        print_slow("The shuttle slows down and tourists take pictures")
        print_slow("Your tour continues...")
        print_slow("You move further down and you see an "
                   "Elephant with her calves")
        print_slow("On the opposite side you see a Rhino strolling")
        print_slow("You move further down. You see a Leopard "
                   "chasing after an Antelope.")
        print_slow("This is an amazing sight to behold!")
        print_slow("You then run into a pride of Lions. "
                   "They see the shuttle and come closer.")
        print_slow("They stare at you and start roaring loudly "
                   "and aggressively")
        print_slow("Everyone is scared. Others are screaming "
                   "and hiding under the seats")
        print_slow("The bus returns to the reception")

        response2 = valid_response("Did you take more than 10 pictures? \n"
                                   "Please enter Yes or No \n", "yes", "no")

        if "yes" in response2:
            print_slow("Congratulations!!! You won.")
        elif "no" in response2:
            print_slow("Better luck next time.")

    elif "museum" in response1:
        print_slow("You chose Museum")
        print_slow("Welcome to the National Park Museum")
        print_slow("Here is where you will learn about "
                   "the national museum.")
        print_slow("Feel free to take selfies!")
        print_slow("Your tour guide will be walk with you"
                   " throughout the museum")
        print_slow("You start from the left side of the museum")
        print_slow("On this side you will see artifacts collected and kept"
                   "from the communities neighboring the museum")
        print_slow("These communities livelihoods depended on the park")
        print_slow("This was detrimental to the ecosystem as "
                   " many animals were killed.")
        print_slow("They have since stopped poaching animals")
        print_slow("On the opposite side of the museum "
                   "are pictures and artifacts"
                   " of animals that at one point in their"
                   " lifetime spent time in this park.")
        print_slow("These artifacts include the skin,"
                   " skulls and tusks etc.")
        print_slow("This is the end of your tour.")

        response3 = valid_response("Did you take more than 10 pictures? \n"
                                   "Please enter Yes or No \n", "yes", "no")
        if "yes" in response3:
            print_slow("Congratulations!!! You won.")
        elif "no" in response3:
            print_slow("Better luck next time.")


def beach_trip():
    print_slow("Lets go on a VACAY!!")

    response4 = valid_response("Would you like to go to the "
                               "North or South coast? \n", "north", "south")

    if "north" in response4:
        print_slow("You chose North Coast")
        print_slow("The North Coast is the economic hub"
                   " of the coastal region.")
        print_slow("It is the home of Marine life")
        print_slow("It hosts the largest port of the region")
        print_slow("You tour the port and see massive boats and yachts")
        print_slow("You go snorkeling and sky diving")
        print_slow("You visit century old forts")

        response5 = valid_response("Did you take more than 10 pictures? \n"
                                   "Please enter Yes or No \n", "yes", "no")
        if "yes" in response5:
            print_slow("Congratulations!!! You won.")
        elif "no" in response5:
            print_slow("Better luck next time.")

    elif "south" in response4:
        print_slow("You chose South Coast")
        print_slow("The South Coast has the most beautiful sandy"
                   " beaches in the region.")
        print_slow("It is a popular holiday destination for couples")
        print_slow("It is normally referred to as 'The Romantic get away'")
        print_slow("It is home of World Class beach resorts")
        print_slow("You visit this beach and enjoy "
                   "beautiful sunrises each morning.")
        print_slow("You get to try authentic cuisines"
                   " from around the world")
        print_slow("You get to swimming the sea and enjoy the stroke"
                   "of waves on your feet as you walk")

        response6 = valid_response("Did you take more than 10 pictures? \n"
                                   "Please enter Yes or No \n", "yes", "no")
        if "yes" in response6:
            print_slow("Congratulations!!! You won.")
        elif "no" in response6:
            print_slow("Better luck next time.")


def begin_trip():
    if trip == "Safari":
        safari_trip()
    elif trip == "Beach":
        beach_trip()


def repeat_trip():
    response7 = valid_response("Would you like to go take the trip again? \n"
                               "Please enter Yes or No \n", "yes", "no")
    if "yes" in response7:
        print_slow("Awesome! Lets do this again")
        begin_trip()
    elif "no" in response7:
        print_slow("We hope you had a good time. Bye")


def play_game():
    intro()
    begin_trip()
    repeat_trip()


play_game()
