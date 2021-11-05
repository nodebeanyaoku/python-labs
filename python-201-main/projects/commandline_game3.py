import random
drops = ["Rusty Sword","Dagger"]
inventory = ["fists"]
default_inventory = ["fists"]
game = False
torch = False
playerhealth = 100
bothealth = 100
hand = None
gold = 0
looted = False
amount = random.randint(1,150)
options = {"cabin","cave","path","inv","status","skyrim","solid"}
invent = False
playername = input("Enter your heroes name: ")
game = True
merchants_inventory = ["Health potion"]
health_potion_price = 25
merchant_prices = ["Health potion : 25 Gold"]
player_xp = 0

print(f"\n{playername} finds himself on a path which seems to lead to a small village..\nTo his left there is a small cabin, to his right there seems to be a cave.\n")


while game == True:
    print("Go to [cabin]\nFollow [path]\nEnter [cave]\n")
    print("Type [inv] to check your inventory. If you type [status] you can see your current health.\nWhat would you like to do?\n")
    
    prompt = input("Enter a command: ").lower()
    
    if prompt in options:
        if prompt == "skyrim":
            inventory.append("Bucket")
        if prompt == "solid":
            inventory.append("Snake key")
        
        if prompt == "path":
            path = True
            game = False
            print(f"{playername} finds himself in a small village, there seems to be a merchant, a little chapel and a castle ")
            
            while path == True:
                print("What would you like to do?\nGo to [merchant]\nWalk to the [chapel]\nEnter the [castle]\nGo [back]\n")

                
                prompt = input("Enter a command: ").lower()
                
                if prompt == "chapel" and "Snake key" not in inventory:
                    print(f"{playername} approaches the front of the chapel..\n The door seems to be locked!\n 'requires S-shaped key'\n")
                
                elif prompt == "chapel" and "Snake key" in inventory:
                    chapel = True
                    print(f"{playername} unlocks the door of the chapel..\nA dragon like creature appears as you enter!\n")
                    while chapel == True:
                        
                        prompt = input("[flee] from the fight or [fight] the creature?\n")

                        if prompt == "flee":
                            print("This doesnt work, the door seems to be jammed!!\n")
                        
                        elif prompt == "fight":
                            bossfight = True
                            print("The dragon spits fire into your direction, he seems to be ready to fight.\nBut are you ready?\n")
                            while bossfight == True:
                                
                                draw_damage = 5
                                player_damage = 25
                                bot_damage = 40
                                if hand == None:
                                    player_damage = 5
                                elif hand == "Dagger":
                                    player_damage = 40
                                elif hand == "Rusty Sword":
                                    player_damage = 30
                                elif hand == "Bucket":
                                    player_damage = 100
                                
                                playernumber = random.randint(1,6)
                                botnumber = random.randint(1,6)
                               
                                prompt = input("Press Enter key to roll the dice!\n")
                                print(f"you roll a {playernumber}, the bot roles a {botnumber}\n")

                                if playernumber > botnumber:
                                    bothealth -= player_damage
                                    print(f"Monster takes damage of {player_damage}\n HP left:{bothealth}\n")
        

                                elif playernumber < botnumber:
                                    playerhealth -= bot_damage
                                    print(f"You take damage by the Monster {bot_damage}\n You have {playerhealth} HP left.\n")
        

                                elif playernumber == botnumber:
                                    playerhealth -= draw_damage
                                    bothealth -= draw_damage
                                    print(f"draw!!\nYou both take {draw_damage} damage.\nPlayer health: {playerhealth}\nBot health: {bothealth}\n")

                                if playerhealth <= 0:
                                    print("You try tried your best to fight this majestic creature but you have FAILED!\nGAME OVER!\nYou have returned to the start of the game, your items and progress is gone..\nGood Luck next time!")
                                    inventory = default_inventory
                                    chapel = False
                                    bossfight = False
                                    hand = None
                                    battle = False
                                    castle = False
                                    torch = False
                                    path = False
                                    looted = False
                                    game = True
                                    gold = 0
                                    playerhealth = 100
                                    bothealth = 100
                                    break
                                
                                elif bothealth <= 0:
                                    print(f"As {playername} prepares for his last attack and stabs the dragon like creature..\nThe creature slowly goes down and turns into dust.\nYOU WIN THE GAME!!\n")
                                    
                                    game = False
                                    path = False
                                    chapel = False
                                    bossfight = False
                                    break
                        else:
                            print("Unknown command!\n")

                

                elif prompt == "castle":
                    print(f"As {playername} approaches the castle he hears screams at the gate...\n")

                    prompt = input("[Enter] or go [back] ?\n")

                    if prompt == "enter":
                        castle = True
                        
                        while castle == True:
                            prompt = input("[w]alk through the corridors or [leave] ?\n")

                            if prompt == "w":
                                radnomizer = random.randint(1,100)
                                if radnomizer <= 50:
                                    amount = random.randint(1,50)
                                    gold += amount
                                    print(f"you found some gold while you walk through the corridors +{amount}")
                                
                                else:
                                    print("You encounter a demonic creature !!!\n Get ready to fight!\n")
                                    battle = True
                                    
                                    while battle == True:
                                        
                                        draw_damage = 5
                                        player_damage = 25
                                        bot_damage = 20
                                        if hand == None:
                                            player_damage = 5
                                        elif hand == "Dagger":
                                            player_damage = 40
                                        elif hand == "Rusty Sword":
                                            player_damage = 30
                                        elif hand == "Bucket":
                                            player_damage = 100

                                        playernumber = random.randint(1,6)
                                        botnumber = random.randint(1,6)
                                        amountgold = random.randint(1,150)
                                        xp_gain = random.randint(1,100)
                                        
                                        prompt = input("Press Enter key to roll the dice!\n")
                                        print(f"you roll a {playernumber}, the bot roles a {botnumber}\n")

                                        if playernumber > botnumber:
                                            bothealth -= player_damage
                                            print(f"Monster takes damage of {player_damage}\n HP left:{bothealth}\n")
        

                                        elif playernumber < botnumber:
                                            playerhealth -= bot_damage
                                            print(f"You take damage by the Monster {bot_damage}\n You have {playerhealth} HP left.\n")
        

                                        elif playernumber == botnumber:
                                            playerhealth -= draw_damage
                                            bothealth -= draw_damage
                                            print(f"draw!!\nYou both take {draw_damage} damage.\nPlayer health: {playerhealth}\nBot health: {bothealth}\n")
                                        
                                        
                                        if bothealth <= 0:
                                            print("You have defeated the demonic creature!\n")
                                            gold += amountgold
                                            player_xp +=xp_gain
                                            print(f"You have looted {amountgold} Gold!\nYou gained {player_xp}XP in this battle.")
                                            playerhealth += 25
                                            bothealth = 100
                                            prompt = input("You now have a chance to get a drop!\nPress Enter key to roll the dice!\n")
                                            
                                            dropnumber = random.randint(0,100)
                                            
                                            if dropnumber > 50:
                                                reward = random.choice(drops)
                                                inventory.append(reward)
                                                print(f"You found a special item!\n{reward} added to your inventory..")
                                                battle = False
                                            
                                            elif dropnumber <=10:
                                                print(f"You found 'Snake key'")
                                                inventory.append("Snake key")
                                                battle = False
                                            else:
                                                print("No drop was found, maybe next time :)\n")
                                                battle = False
                                        
                                        elif playerhealth <= 0:
                                            print("You have lost the Battle!\nGAME OVER!\You have returned to the start of the game, your items and progress is gone..\nGood Luck next time!")
                                            
                                            inventory = default_inventory
                                            hand = None
                                            battle = False
                                            castle = False
                                            torch = False
                                            path = False
                                            looted = False
                                            game = True
                                            gold = 0
                                            playerhealth = 100
                                            bothealth = 100
                                            break

                            elif prompt == "leave":
                                castle = False
                    
                    elif prompt == "back":
                        continue

                    else:
                        print("unknown command!\n")



                elif prompt == "merchant":
                    merchant = True
                    
                    print("Welcome Traveler!\nIam willing to make you a good offer\n")
                    
                    while merchant:
                        prompt = input("[show] merchants inventory or go [back]?\n".lower())
                        
                        if prompt == "back":
                            merchant = False
                        
                        elif prompt == "show":
                            print(f"Inventory: {', '.join(merchants_inventory)}\n Current Prices: {', '.join(merchant_prices)}\nType [exit] inventory or [choose] item? \n")
                            
                            prompt = input("What do you wish to do? \n".lower())
                            
                            if prompt == "choose":
                                print("item index starts at 1.")
                                
                                prompt = input("Choose an item: ")
                                
                                if prompt.isdigit():
                                    index = int(prompt) -1
                                    
                                    if index in range(len(merchants_inventory)):
                                        item = merchants_inventory[index]
                                        
                                        prompt = input(f"Do you wish to buy {item}?\n[y]es or [n]o ?\n".lower())
                                        
                                        if prompt == "y":
                                            inventory.append(item)
                                            print(f"{item} was added to your inventory..\n")
                                            
                                        
                                        elif prompt == "n":
                                            continue
                                        
                                        else:
                                            print("unknown command!\n")
                                else:
                                    print("not a number!\n")
                                    
                            
                            elif prompt == "exit":
                                continue

                            else:
                                print("unknown command!\n")
                        else:
                            print("unknown command!\n")



                elif prompt == "back":
                    path = False
                    game = True

                else:
                    print("Unknown command!\n")



        if prompt == "cave" and hand == "torch":
            cave = True
            print(f"{playername} is slowly walking into the cave\nThere is a little river inside that cave..")
            while cave == True:
                
            
                prompt = input("Do you wish to [go] inside the water or [leave] the cave ? \n").lower()
            
                if prompt == "go" and looted == False:
                    print(f"{playername} is slowly making his way into the water.. 'brrrr' this must be cold.\n\n You find some gold!\n +{amount} gold\n\n")
                    gold += amount
                    looted = True
            
                elif prompt == "go" and looted == True:
                    print("nothing else to be found!\n\n")

                elif prompt == "leave":
                    cave = False

                else:
                    print("Unknown command!\n")
        
        elif prompt == "cave" and hand != "torch":
            print(f"{playername} is slowly walking into the cave, its so dark that he cant see his own hands no more\n Next to him there is a big growl occuring, a werewolf approaches him and rips him apart..\n\nGAME OVER!\n\nHINT:Find the torch before you enter the cave and make sure the player is holding it!")
            break
        
        elif prompt == "cabin":
            cabin = True
            print(f"As {playername} enters the old and abandoned cabin .. \nThere seems to be a bunch of old boxes\n")
            while cabin == True:
                
            
                prompt = input("Do you wish to [search] the room or go [back] ? \n").lower()
        
                if prompt == "search" and  torch == True:
                    print("There is nothing else to be found..\n")

                elif prompt == "back":
                    cabin = False

                elif prompt == "search":
                    print(f"\nAs you search through the old and half broken crates you find what seems to be a 'torch'.\n")
                
            
                    prompt = input("[Take] the 'torch' with you or [leave] it? \n").lower()
                
                    if prompt == "take":
                        inventory.append('torch')
                        print(" 'torch' was added to your inventory\n")
                        torch = True
                
                    elif prompt == "leave":
                        print("You leave the 'torch' behind!\n")

                    else:
                        print("Unknown command\n")
                else:
                        print("Unknown command\n")
            
        
        elif prompt == "status":
            print(f"Equiped Weapon: {hand}\nHealth: {playerhealth}%\nCurrent Gold: {gold}\n")
        
        if prompt == "inv" and len(inventory) == 0:
                print("Inventory is empty.")


        elif prompt == "inv":
            invent = True
        while invent == True:
            
            print(f"Inventory: {', '.join(inventory)}\nType [exit] inventory or [choose] item? \n")
        
            prompt = input("What do you wish to do? ".lower())
            
            if prompt == "exit":
                invent = False
            
            
            if prompt == "choose":
                print("item index starts at 1.")
                
                prompt = input("Choose an item: ")
                
                if prompt.isdigit():
                    index = int(prompt) -1
        
                    if index in range(len(inventory)):
                        item = inventory[index]
                        
                        if item == "Health potion":
                            prompt = input(f"Do you wish to use {item} y/n ? ".lower())
                            
                            if prompt == "y":
                                playerhealth += 25
                                inventory.pop(index)
                                print(f"You have used {item} and increased your health by +25hp!\n New Playerhealth {playerhealth}")
                            elif prompt == "n":
                                continue

                            else:
                                print("Unknown command!")

                        else:
                            prompt = input(f"What do you wish to do with {item}?\n[Equip] or [Discard] ? ".lower())
                        
                        if prompt == "equip" and hand == None:
                            item = inventory.pop(index)
                            hand = item
                            print(f"\n{item} has been equipped.")
                        
                        elif prompt == "equip":
                            inventory.append(hand)
                            item = inventory.pop(index)
                            hand = item
                            print(f"\n{item} has been equipped.")
                        
                        elif prompt == "discard":
                            
                            if item == "fists":
                                print("This item cant be discarded!")

                            else:
                                inventory.pop(index)
                    else:
                        print("Item not found\n")
                else:
                    print("not a number!\n")   
                    


    
    
    else:
        print("unknown command!\n")
    
    
print("Thanks for trying out my project! :)\nThis was made as a project during self studying python at codingnomads.\nThis was my first script that exceeded 100 + lines.")
    