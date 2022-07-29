from character import knight, wizard, rouge, archer
from scenes import archer_profil, cave_scene, dragon_scene, dream_scene, enchatned_forest, goblin_camp, knight_profil, rouge_profil, start_screen, wizard_profil, goblin_fight, town_scene
import m_battle 
import sys

#notes
#battle system is not currently working because of some import issue
print("")
print("To understand this quest you must understand how a D20 works.")
print("")
print("During crucial events in this quest a dice will be rolled landing 10 or above on the dice will always result in good outcomes.")
print("")
print("landing anything lower and some unforeseen consequences will occur. it is up to you to take those chances.")



while True:
    playerchoice = input("Press 1 to Continue: ")
    if playerchoice == "1":
        print(dream_scene())
        print("""
            ==================================================================
                        a vivid dream occures to you... 
                    
                        what was your name again?""")
        name = input("What is your name: ")
        break
    else:
        print("Please type 1 to continue: ")

while True:
    print("""
            =============================================================================
                    Ah right right it was """, name , """how could I forget?
    
    do you remember what you said you always wanted to be? I think it was one of these options...
    lets try to remember

[Option 1] your dream is to be a Knight

[Option 2] your dream is to be a Rouge

[Option 3] your dream is to be a Wizard

[Option 4]  your dream is to be a Archer
    """)

    player = input("Choose a option....")
    if player == "1":
        print(knight_profil())
        player = knight
        my_hp = knight.hp
        my_damage = knight.attk
        my_gold = 0
        break
    elif player == "2":
        print(rouge_profil())
        player = rouge
        my_hp = rouge.hp
        my_damage = rouge.attk
        my_gold = 0
        break
    elif player == "3":
        print(wizard_profil()) #you are a wizard harry!
        player = wizard
        my_hp = wizard.hp
        my_damage = wizard.attk
        my_gold = 0
        break
    elif player == "4":
        print(archer_profil())
        player = archer
        my_hp = archer.hp
        my_damage = archer.attk
        my_gold = 0
        break
    else: 
        print("Please choose 1 - 4")
print("---------------------------------")
print("Health: ", my_hp)
print("Damage: ", my_damage)
print("---------------------------------")

    #this is how a battle should start
    #m_battle.test(my_hp, my_damage, m_battle.goblin.hp, m_battle.goblin.attk)

while True:
    playerchoice =input("type 1 to continue: ")

    if playerchoice == "1":
        print("")
        break
    else:
        print("Please type in 1 to continue")

print(cave_scene())
print("""
        =====================================================================================
                        *You feel a strong precences watching over you...*

Did you feel that???

                *As you look around you slowly start to noice that you are inside a cave...*
                        there seems to be hole ahead that you can go to...

[Option 1] *Look around the cave before entering the hole*
[Option 2] *Go to the hole*""")

while True:
    playerchoice = input("Choose an Option: ")
    if playerchoice == "1":
        print("""
            ========================================================================================

                    *Looking at the cave walls you see scorch marks as dark as the night sky...*

my only guess is that people dont come to this cave and make it out in one peiece.... 

[Option 2] *Go to the hole*

        """)
    elif playerchoice =="2":
        print(""" 
        ========================================================================================

            *you barely squeeze through the hole with your gear... as you look onward the strong precences becomes even stronger*

this is getting dangerous.... but there is no other way out of this cave... we must go further in and fight whatever is at the end of this.
            """)
        break
    else:
        print("Please choose a valid option")

while True:
    print(dragon_scene())
    playerchoice = input("""
        ========================================================================================
                        *Before your very eyes... An Elder Dragon....*
                You can feel your bones shake by just its glance, it is to late to run now... you must fight

Press 1 to continue to fight: 
""")
    if playerchoice == "1":
        print("")
        break
    else:
        print("Please choose a valid option")

#m_battle.test(my_hp, my_damage, m_battle.elder_dragon.hp, m_battle.elder_dragon.attk, m_battle.alive)
# ask about getting the death system working.

while True:
    print(start_screen())
    print("""
        =====================================================================================
                            You wake up from your dream covered in sweat...  

Inside your room in the castle you hear a knock from the door... a guard speaks: *""", name, """, King Yoto wishes to see you now, please get up and go to the throne room*
""")
    playerchoice = input("Press 1 to get up and leave room: ")

    if playerchoice == "1":
        print("""
        =======================================================================================

You stand up and get dressed and take a walk through the great halls of the Eastern Rise Kingdom,
As you make your way to the throne room you see a painting of the King


[Option 1] *Observe the painting*
[Option 2] *Continue to the throne room*""")

        break
    else:
        print("please press 1 to continue....")

while True:
    playerchoice = input("Please choose a option: ")
    if playerchoice == "1":
        print("""
        ====================================================================
                *King Yoto ... the king of the eastern rise kingdom*

He was made king after his fathers death during the Great demon war
and is well respected through out the East. 
I wonder what he could have planned for me* """)

        print("\n \n [Option 2] *Continue to the throne room*")

    elif playerchoice == "2":
        print("""
        ====================================================================
                    *its best I dont keep the king waiting*

You go ahead and proceed down the hallway, the throne room doors opening infront of you
as you are greeted by King Yoto. 
""")
        break
    else:
        print("Please choose a valid option")

while True: 
    print("""
        ====================================================================

[King Yoto]: Well if it isnt """, name, """ 
I have an extremly important mission for you and you alone.

*as you see the king nod his head as everyone clears out the room* 
""")
    playerchoice = input("Press 1 to continue: ")

    if playerchoice == "1":
        print("")
        break

print("""
    ========================================================================================================================================

[King Yoto:] now that we have the room, as you may remember... Trog the Elder Dragon has been up on the mountain for as long as we remember...

dormaint like always.

Well as of recently Trog has risen and is awake once again.

normally I would send an army off to fight Trog. But its no use we need someone who bares the scar of the Elder Dragon in order to enter his chamber...

It comes to no shock that that means you... as you have fought Trog before if you remember..

""")

print(name,": Yes.... about 5 years ago I fought back that dragon into that cave... I still have dreams of it to this day.")

while True:

    print(""" 
        ========================================================================================================================================

[King Yoto]: Well for the sake of the Eastern Rise Kingdom, I King Yoto Ask.

Will you go and Slay the Elder Dragon known as Trogdoor The Burninator?

[Option 1] Of Course my king.

[Option 2] No.
""")
    playerchoice = input("Choose an option: ")
    if playerchoice == "1":
        print("I could always count on you ",name,"now go there is not much time to waste!")
        print("             *you leave for the town below in a hurry*           ")
        break
    elif playerchoice =="2":
        print("[King Yoto]: HAHAHAHAH always fun with the jokes, now hurry you do not have much time left.")
        print("     *You relucently go as the gaurds lead you out the castle towards the town below*    ")
        break
    else:
        print("Please choose a valid option.")

print(town_scene())

while True:
 
    print("""
        =============================================================================================
                            *you look around the busy town...*
there a many people around... some adventures, news paper boy, citizens... you see the exit of the town straight ahead to the enchanted forest.

[Option 1] Talk to the adventures
[Option 2] Talk to the news paper boy
[Option 3] Talk to the citizens
[Option 4] Exit to the Enchanted Forest
    """)
    playerchoice = input("Choose an option: ")

    if playerchoice == "1":
        print("""
            =============================================================================================
        *You approch the adventures and talk about past quests/fights
    While talking with them one of the adventures mentions a dangeours goblin camp on the First path of the enchanted forest...
    but they say the goblins gaurd some kind of weapon....
""")
    elif playerchoice == "2":
        print("""
            ==========================================================================================================
        *You approch the news paper boy as he is talking about a rare tresure on the Second path of the enchanted forest...
    he seems to be to focused on his work trying to sell his papers and wont anwser your question about the treasure....
        """)
    elif playerchoice == "3":
        print("""
            ========================================================================
                *You approch 3 citizens who are all together and talk about the weather...*
        you overhear one of them talking about moving to the next town over on the Third path of the enchanted forest...
        one of the citizens says that its to dangerous with the cave next to that town having a strong monster inside...
        the last citizens says thats just a myth...
        """)
    elif playerchoice =="4":
        print("""
            ========================================================================
                    *you leave the town towards the enchanted forest*
        """)
        break
    else:
        print("Please choose a valid option...")


def path_1():
    print(goblin_camp())
    while True:
        print("""
            ============================================================
        *On your way down the first path you come across a goblin camp...*

[Option 1] Fight Goblins
[Option 2] Run away!
[Option 3] Sneak through [Rouge Only]
    """)
        playerchoice = input("Choose an option: ")
        if playerchoice == "1":
            print("you prepare for battle!")
            print(goblin_fight())
            m_battle.test(my_hp, my_damage, m_battle.goblin.hp, m_battle.goblin.attk)

        elif playerchoice == "2":
            print("you get away before the goblins see you")
            return E_forest() 

        elif playerchoice == "3" and player == rouge:
            print("You sneak past all the goblins... easily stealing what they were guarding")
            break
        
        elif playerchoice =="3" and player != rouge: 
            print("you try and sneak past but fail! the goblin leader immedeitly notices you, the massive Orc fights you!")
            m_battle.test(my_hp, my_damage, m_battle.orc.hp, m_battle.orc.attk)

        else:
            print("Please choose a valid option")

def E_forest():
    print(enchatned_forest())
    while True:
        print("""
            =============================================================================
                *You enter a calm and peaceful forest.... Ahead of you are 4 paths...*
                King Yotos instructions say that that path to Trog is on Path 4...

[Option 1] Path 1....
[Option 2] Path 2....
[Option 3] Path 3....
[Option 4] Path 4....
    """)
        playerchoice = input("Choose an option: ")
        if playerchoice == "1":
            print("You head towards path 1")
            print(path_1())
        else:
            print("Please choose valid option")


while True:
    print(E_forest())
