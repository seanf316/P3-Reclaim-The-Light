# **Reclaim The Light Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself and also by my peers. 

## **Contents**

1. [Testing Overview](#testing-overview)
1. [Input Testing](#input-testing)
1. [Manual Testing](#manual-testing)
1. [Functions](#functions)
1. [Validators](#validators)

## **Input Testing**
All inputs are set to .lower() except the Guardian name which uses capitalize(), the .lower() inputs have been tested with lowercase & uppercase letters and all work as expected. All user inputs were printed back to the console to check all functions and methods were correctly applied to the input. The below flowchart shows each input within the adventure tested. 
![Flowchart](/docs/flowchart/testing_flowchart.webp)

[Back to top &uarr;](#contents)

## **Manual Testing**

- The game was deployed early on in development and checked regularly to ensure game flow and any errors were handled early on.

- print() method was used throughout to test for errors. This helped check everything was behaving as expected and functions such as generating the random numbers for the Guardian/Enemy stats were being generated correctly. It was also used to check that the loot values i.e. name, value, assignment etc. were displaying as expected.

- Errors or warnings were fixed as they appeared such as indentation errors, lines too long or extra space issues. This helped keep the code clean and readable so other errors or bugs that arose were identified more easily.

- The code has been seperated in to seperate files to be cleaner and also for easier management of future updates, all files that linked with other files were tested throughout development.

- Throughout development, I was testing the game in the terminal of VScode as well as playing multiple rounds in the Code Institute terminal template for each deployment to Heroku.

- After deployment all features were checked on a laptop and ticked off if they functioned as expected. The app was sent out to my peers for testing and any issues reported back were resolved and tested. The app was tested on mobile and although it is functional it was not built for mobile game play as the terminal window is too big and requires user scrolling. 

[Back to top &uarr;](#contents)

## **Functions**

All functions where tested throughout development.

### ***welcome_screen()***
The welcome_screen() is the first function used in the game and displays a screen containing 3 choices Start, Mission Log and About. All inputs where tested and error handled. Ascii Text displayed as expected and pause() function worked as expected.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***gen_char()***
Each stage of the gen_char() function was tested as the code was written. It started with the input testing as outlined above, then the stats for each class where tested by calling the function and then printing the Guardian stats using pprint.
Guardian stats are set for each character class with exception of the luck stat which is generated using random.randint, this was tested also and showed no errors in testing. Guardian luck and defence stats have been set to a maximum value regardless of further loot drops to combat bugs which can be reviewed in the Bugs & Fixes section. 

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***gen_enemy()***
Each stage of the gen_enemy() function was tested as the code was written. The enemy name is randomly chosen from the enemy.txt file using random and is working as expected. All enemy stats are generated using random.randint and are passed specific ranges i.e. health = random.randint(80, 100)
This was tested and adjusted several times during gameplay to allow for a far battle experience.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***path_choice()***
The path_choice() function was created so I wouldn't be repeating code throughout the adventure. It takes the arguments (choice, select_1, select_2, error, function_1, function_2) and was used throughout the project in all narrative functions.
There was one bug encountered which can be reviewed in the Bugs & Fixes section. Function was tested and worked as expected.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***strike_chance()***
This function generates a random value between 1 & 6 if the players luck stat is < then the value provided the enemy will dodge the players attack and the player will be alerted to this. If the players luck stat is > then the value provided the player will strike the enemy successfully and player will be alerted to this. The value range in this function was found to be the best in testing for a better player experience. It was adjusted on several occasions to find the right balance.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***enemy_attack()***
This function generates a random value between 1 & 10 if the the enemy chance stat is >= the value provided the enemy will successfully strike the player. The value range here was adjusted throughout tested to allow the enemy a fair chance of striking the player and allowed for a better combat experience. No errors arose in testing.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***found_loot() & loot()***
This found_loot() function was created for the player to discover loot in their surroundings. The loot() function is based around battle and whether the enemy will drop loot upon being defeated. Loot is broken down into 4 values - rarity, name, value and assignment and those values are retrieved from 3 files - game_docs/common.txt", "game_docs/legandary.txt","game_docs/exotic.txt". They are chosen randomly by placing the files in a list and using random to choose a file in the list. When loot is dropped the value is assigned to the players character using the getter/setter methods in the Guardian class. In the loot() a random number between 1 & 7 is generated if this number is higher then the players luck stat the enemy will not drop loot and the player will be advised of this. If the value generated is less then the players luck stat the enemy will drop loot and the player will be advised of this and value of loot will be added to the characters specific stat. 

The values have been adjusted throughout testing to correct some bugs which can be reviewed in the Bugs & Fixes section.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***battle()***
The battle function is the most extensive function in the project. It first acknowledges that a battle has begun and introduces the enemy to the player and reveals the enemy's stats. Then an input will be displayed to the user to choose their attack - "C" for "Close", "R" for "Ranged" or "M" for "Magic" attack.

It will then call the strike_chance() function and if strike is successful is will call on the is_dead() function which will check if the enemy's health is < then 1 using the the Enemy class get_e_health method after a successful hit, if the enemy isn't dead it will set the enemy's new health using the Enemy class set_e_health method minusing the damage value from the players stat value. Example below:

damage = guardian.get_ranged() - enemy.get_e_defence()
if strike:
            enemy.set_e_health(enemy.get_e_health() - damage)

Next it will call the enemy_attack() function and similar to the above it will call on the is_dead() function which will check if the players's health is < then 1 using the the Guardian class get_health method after a successful hit, if the player isn't dead it will set the player's new health using the Guardian class set_health method minusing the damage value from the enemy's attack stat value. Example below:

loss = attack_value - defence
guardian.set_health(guardian.get_health() - enemy_attack
                                (enemy.get_e_chance(),
                                enemy.get_e_attack(),
                                enemy.get_e_name(),
                                guardian.get_defence()))

This will continue until either the Player or the Enemy are dead at which stage either the loot() function will be called or the game_over() function.

At the end of each battle if the Player's health is < then 100 the Player's is restored to full health using the Guardian get/set health method see below:

if guardian.get_health() < 100:
                guardian.set_health(100)

All parts of the function were tested on many occasions and adjusted to provide a competitive experience for the player. Any errors or bugs that were found have been resolved and the function is behaving as expected.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

[Back to top &uarr;](#contents)

## **Validators**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project.

<details><summary>run.py</summary>

![run.py Results](/docs/ci_linter/run_results.webp)
</details>

<details><summary>adventure.py</summary>

![adventure.py Results](/docs/ci_linter/adventure_results.webp)
</details>

<details><summary>functions.py</summary>

![functions.py Results](/docs/ci_linter/functions_results.webp)
</details>

<details><summary>guardian.py</summary>

![guardian.py Results](/docs/ci_linter/guardian_results.webp)
</details>

<details><summary>enemy.py</summary>

![enemy.py Results](/docs/ci_linter/enemy_results.webp)
</details>

<details><summary>story.py</summary>

![story.py Results](/docs/ci_linter/story_results.webp)
</details>

<details><summary>ascii_art.py</summary>

![ascii_art.py Results](/docs/ci_linter/ascii_results.webp)

</details>

[Back to top &uarr;](#contents)

[Return to README.md](README.md)