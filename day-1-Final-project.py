#Band Name Game : Let's hook up nicknames !

# print("-------Greetings to Band Name Game ! -------")
# print("\n")
# city = input(" in which city did you grow up in ? ")
# print("\n")
# pet = input(" it's nice to have a pet. what is name of yours ? ")
# print("\n")
# print(" your Band Name must be " + " << " + city + " " + pet + " >>\n")

#Bill_Tip Calculator : Tips not to be forgotten !

# print("------Thanks for coming. Be back soon !------\n")
# bill = float(input(" How much do we have ? ($) "))
# print("\n")
# num_friends = int(input(" How many are we ? "))
# print("\n")
# tip = float(input(" How much is the tip ? (%) "))
# print("\n")
# tip = tip / 100
# bill_per_person = ( bill / num_friends ) * ( 1 + tip )
# bill_per_person = "{:.2f}".format(bill_per_person)
# print(f" Each of us has to pay {bill_per_person}$ ")

#Time to Fajr : Don't miss Fajr !

print("------Greetings ! is it dawn time ? -----\n")
fajr_per_hour = 6
fajr_per_minutes = 50
print(f" reminder : Fajr is on {fajr_per_hour}:{fajr_per_minutes} AM \n")
print(" tell the time according to AM and PM. \n")
print(" guide :  --> 06:02 AM is 6:2" )
print("          --> 06:02 PM is 18:2" )
print("          --> 00:00 AM is 0:0\n")
time_per_hours = int(input(" What is hour now ? "))
time_per_minutes = int(input(" how much minutes ? "))
if time_per_hours <= 18 and time_per_hours > 6 :
 hours_to_fajr = ( 18 - time_per_hours ) + 12
elif time_per_hours > 18 :
 hours_to_fajr = ( 24 - time_per_hours ) + 6
else :
 hours_to_fajr = 6 - time_per_hours
minutes_to_fajr = 50 - time_per_minutes
if minutes_to_fajr < 0 :
  hours_to_fajr = hours_to_fajr - 1
  minutes_to_fajr = 60 - time_per_minutes
print("")
print(" it's " + str(hours_to_fajr) + " hours and " + str(minutes_to_fajr)  + " minutes to Fajr. Set up your alarm !" )

#Treasure Island : Sail up over the seven seas !

# print('''---Greetings. Ready to embark on the seven seas ?---

# But you're not in possession for the treasure map
#  ____________________________________________________________________
#  / \-----     ---------  -----------     -------------- ------    ----\
#  \_/__________________________________________________________________/
#  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
#  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
#  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
#  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
#  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
#  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
#  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
#  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
#  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
#  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
#  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
#  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
#  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
#  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
#  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
#  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
#  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
#  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
#  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
#  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
#  / \----- ----- ------------  ------- ----- -------  --------  -------\
#  \_/__________________________________________________________________/

# You will have to sketch it down. I'm here to give you hints !''')

# direction = input(" You're at a crossroad. Going left or right ? ")
# direction_lower = direction.lower()
# if direction_lower == "right" :
#   result = "You fell into a hole. Game Over !"
# elif direction_lower == "left" :
#  print("")
#  decision = input(" You see an island. Wait or swim ? ")
#  decision_lower = decision.lower()
#  if decision_lower == "swim" :
#   result = "You're attacked by a trout. Game Over !"
#  elif decision_lower == "wait" :
#   print("")
#   print(" A castle with portal floats in view.")
#   print(" also, a cave does.")
#   place = input(" Shall we go to the..? ")
#   place_lower = place.lower()
#   if place == "castle" :
#    print("")
#    door = input(" Pick a door: blue, red or yellow ? ")
#    door_lower = door.lower()
#    if door_lower == "blue" :
#     result = "You're eaten by beasts. Game Over !"
#    elif door_lower == "red" :
#     result = "You're burned by fire. Game Over !"
#    elif door_lower == "yellow" :
#     result = "Treasure found ! time to ride on the seas !"
#    else :
#     result = "You're missing treasure. where heading ?"
#   elif place == "cave" :
#    print("")
#    print(" You found a huge bear ! he attacks you !")
#    weapon = input(" You find a sword and a bag by ground.")
#    weapon_lower = weapon.lower()
#    if weapon_lower == "bag" :
#     result= "You're killed by the bear. Game Over !"
#    elif weapon_lower == "sword" :
#     print("")
#     proceed = input(" Bear is killed. Proceed down the cave? ")
#     proceed_lower = proceed.lower()
#     if proceed_lower == "yes" :
#      result = "Treasure found ! let us start our real game !"
#     else :
#      result = "a rock cut the way out. you're stuck."
#    else :
#     result = "You're dead if you wanna fight on hands !"
#   else :
#    result = "You're missing treasure. where heading ?" 
#  else :
#   result = "You're missing treasure. where heading ?"
# else :
#  result = "You're missing treasure. where heading ?"
# print("")
# print(f" {result}")
     