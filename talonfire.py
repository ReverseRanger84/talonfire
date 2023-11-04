name = input('Enter your name: ')
print(f'Greetings, {name}!')

start = input('Want to play my Adventure Game TalonFire? (yes or no): ')

if start == 'yes':
    print('Great! Off we go!')
    print('Welcome to this mythical realm. Any failed attempt or death in the game will result in the termination of the game...')

    setting = input('This adventure begins with you walking down a path when you run into a fork in the road. (Left or Right?): ')

    if setting == 'left':
        print('You find yourself surrounded by a vast forest. Trees 5 stories tall, lush with green leaves.')

        response = input('You have been walking for a while when you reach a waterfall with crystal clear water. Do you take a break and drink the water or keep following the path? (take a break or follow): ')

 
    if response == 'take a break':
        print('You go over to the waterfall and find a nice rock to sit on next to the water. You reach down to scoop up some water. As you drink from the waterfall, you start to feel weird. Your body feels lighter, and you start to hear the trees speak.')

        communicate_choice = input('You can hear the whispers of the trees. They offer you a choice: Do you want to communicate with them or continue your journey? (communicate or continue): ')
        if communicate_choice == 'communicate':
            print('You decide to communicate with the trees, and they share their ancient wisdom with you. The trees grant you the power of forest manipulation. You can now control and shape the trees and plants in the forest.')
            print('After you gain the power of forest manipulation, you spend a couple of days learning from the trees on how to harness this new power. On the last day, they send you back on your journey through the magical forest with your newfound abilities.')

            # Now, let's add the jaguar encounter and fight sequence
            print('As you continue your journey, you feel a newfound connection with the forest, and you're filled with confidence in your abilities.')
            print('However, suddenly, a powerful jaguar leaps out from the shadows, its fierce eyes locked onto you. The jaguar growls menacingly, ready to pounce.')

            fight_choice = input('Do you decide to fight the jaguar or use your forest manipulation powers to protect yourself? (fight or manipulate): ')

            if fight_choice == 'fight':
                print('You decide to stand your ground and fight the jaguar. The battle is intense, with the jaguar's agility and strength posing a formidable challenge.')
                
                # You can add more details and decisions for the fight here, like using the environment to your advantage or specific actions.

                # For this example, let's assume you manage to defeat the jaguar after a fierce battle.
                print('After a strenuous fight, you manage to defeat the jaguar, but you are left bruised and exhausted.')

            elif fight_choice == 'manipulate':
                print('You use your newfound forest manipulation powers to create a protective barrier of thorny vines and trees between you and the jaguar.')
                print('The jaguar, unable to reach you, eventually retreats, realizing it can't get to you through your forest defenses.')

            else:
                print('Invalid Response! You Lose!')

        elif communicate_choice == 'continue':
            print('You choose to continue your journey, leaving the waterfall behind and continuing your adventure.')

        else:
            print('Invalid Response! You Lose!')

        elif response == 'follow':
            response = input('You walk down the path for a while and find that the forest is now gone and opens to Great plains. You notice a cabin alone in the plains. Do you approach the cabin? (approach or continue): ')
            if response == 'approach':
                print('You walk up towards the cabin and knock on the door... No response. You yell HELLO! but there is no answer.')
                open_door_choice = input('Do you want to try to open the door? (yes or no): ')
                if open_door_choice == 'yes':
                    print('You try to open the door, and it creaks open to reveal a cozy interior of the cabin. ')
                    cabin_choice = input('Do you explore the cabin or leave? (explore or leave): ')
                    if cabin_choice == 'explore':
                        print('You find a chest in the closet. You pull it out and open it. Inside you find an enchanted sword and shield. In the chest is a note saying ""Shield of speed, Sword of Strength"".')
                        print('As you pick up the weapons you feel a rush of adrenaline and the strength of 10 men course through your body.')
                    else:
                        print('As you turn away you hit a trip wire. You hear a click and you are knocked uncocious. You lose!')
                elif open_door_choice == 'no':
                    print('You decide not to open the door and continue your adventure.')
                else:
                    print('Invalid Response! You Lose.')
            elif response == 'continue':
                print('You choose to continue your journey across the Great plains, leaving the cabin behind and continuing your adventure.')
            else:
                print('Invalid Response! You Lose!')

if setting == 'right':
    print('You head down the right path and soon find yourself climbing a steep mountain.')

    mountain_choice = input('You reach a point where you have to make a decision: Do you want to descend down the mountain or continue on the mountain peak trail to find a monastery of monks? (descend or continue): ')

    while True:  # Start a loop to handle the mountain choice
        if mountain_choice == 'descend':
            print('You carefully descend down the mountain, navigating the rocky terrain. As you reach the bottom, you find a hidden cave entrance.')

            while True:  # Start a loop to handle the cave choice
                cave_choice = input('Do you want to explore the cave or continue your journey? (explore or continue): ')

                if cave_choice == 'explore':
                    print('You enter the cave. Congratulations, you have found the Easter Egg! Creator - Caleb Hatfield.')
                    return_to_mountain = input('Do you want to return to the mountain peak trail? (yes or no): ')

                    if return_to_mountain == 'yes':
                        print('You choose to return to the mountain peak trail.')
                        break  # Exit the cave choice loop and return to the mountain choice

                else:
                    print('Invalid Response! Please choose "explore" or "continue".')

        elif mountain_choice == 'continue':
            print('You choose to continue on the mountain peak trail. After a peaceful and scenic walk, you eventually stumble upon a secluded monastery of monks.')

            monastery_choice = input('Do you want to interact with the monks or continue your journey? (interact or continue): ')

            if monastery_choice == 'interact':
                print('You enter the monastery and spend some time with the monks. They share their wisdom and offer you their blessings.')

                print('The monks see great potential in you and decide to grant you mystic psychic abilities. You can now sense and manipulate the unseen energies of the world.')

            else:
                print('Invalid Response! Please choose "interact" or "continue."')

        else:
            print('Invalid Response! Please choose "descend" or "continue."')

        mountain_choice = input('You reach a point where you have to make a decision: Do you want to descend down the mountain or continue on the mountain peak trail to find a monastery of monks? (descend or continue): ')

    print('Thank you for playing the game!')
else:
    print('Invalid Response! You Lose!')

print('Thank you for playing the game!')
