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
All inputs are set to .lower() except the Guardian name which uses capitalize(), the .lower() inputs have been tested with lowercase & uppercase letters, and all work as expected. All user inputs were printed back to the console to check all functions and methods were correctly applied to the input. The below flowchart shows each input within the adventure tested. 
![Flowchart](/docs/flowchart/testing_flowchart.webp)

[Back to top &uarr;](#contents)

## **Manual Testing**

- The game was deployed early on in development and checked regularly to ensure game flow and any errors were handled early on.

- print() method was used throughout to test for errors. This helped check everything was behaving as expected and that functions such as generating the random numbers for the Guardian/Enemy stats were being generated correctly. It was also used to check that the loot values i.e. name, value, assignment, etc. were displaying as expected.

- Errors or warnings were fixed as they appeared such as indentation errors, lines too long, or extra space issues. This helped keep the code clean and readable so that other errors or bugs that arose were identified more easily.

- The code has been separated into separate files to be cleaner and also for easier management of future updates, all files that linked with other files were tested throughout development.

- Throughout development, I was testing the game in the terminal of VScode as well as playing multiple rounds in the Code Institute terminal template for each deployment to Heroku.

- After deployment, all features were checked on a laptop and ticked off if they functioned as expected. The app was sent out to my peers for testing and any issues reported back were resolved and tested. The app was tested on mobile and although it is functional it was not built for mobile gameplay as the terminal window is too big and requires user scrolling.

[Back to top &uarr;](#contents)

## **Functions**

All functions were tested throughout development.

### ***welcome_screen()***
The welcome_screen() is the first function used in the game and displays a screen containing 3 choices Start, Mission Log, and About. All inputs were tested and error handled. Ascii Text displayed as expected and the pause() function worked as expected.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***gen_char()***
Each stage of the gen_char() function was tested as the code was written. It started with the input testing as outlined above, then the stats for each class were tested by calling the function and then printing the Guardian stats using pprint.
Guardian stats are set for each character class with exception of the luck stat which is generated using random.randint, this was tested also and showed no errors in testing. Guardian luck and defence stats have been set to a maximum value regardless of further loot drops to combat bugs which can be reviewed in the Bugs & Fixes section.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***gen_enemy()***
Each stage of the gen_enemy() function was tested as the code was written. The enemy name is randomly chosen from the enemy.txt file using random and is working as expected. All enemy stats are generated using random.randint and are passed specific ranges i.e. health = random.randint(80, 100)
This was tested and adjusted several times during gameplay to allow for a far battle experience.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***path_choice()***
The path_choice() function was created so I wouldn't be repeating code throughout the adventure. It takes the arguments (choice, select_1, select_2, error, function_1, function_2) and was used throughout the project in all narrative functions.
There was one bug encountered which can be reviewed in the Bugs & Fixes section. The function was tested and worked as expected.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***strike_chance()***
This function generates a random value between 1 & 6 if the player's luck stat is < than the value provided the enemy will dodge the player's attack and the player will be alerted to this. If the player's luck stat is > then the value provided the player will strike the enemy successfully and the player will be alerted to this. The value range in this function was found to be the best in testing for a better player experience. It was adjusted on several occasions to find the right balance.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***enemy_attack()***
This function generates a random value between 1 & 10 if the enemy chance stat is >= the value provided the enemy will successfully strike the player. The value range here was adjusted throughout tested to allow the enemy a fair chance of striking the player and allowed for a better combat experience. No errors arose in testing.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***found_loot() & loot()***
This found_loot() function was created for the player to discover loot in their surroundings. The loot() function is based around battle and whether the enemy will drop loot upon being defeated. Loot is broken down into 4 values - rarity, name, value, and assignment and those values are retrieved from 3 files - game_docs/common.txt", "game_docs/legandary.txt", "game_docs/exotic.txt". They are chosen randomly by placing the files in a list and using random to choose a file in the list. When loot has dropped the value is assigned to the player's character using the getter/setter methods in the Guardian class. In the loot() a random number between 1 & 7 is generated if this number is higher than the player's luck stat the enemy will not drop loot and the player will be advised of this. If the value generated is less than the player's luck stat the enemy will drop loot and the player will be advised of this and the value of loot will be added to the character's specific stat.

The values have been adjusted throughout testing to correct some bugs which can be reviewed in the Bugs & Fixes section.

**Conclusion: This function and all its elements work as expected and no bugs appear.**

### ***battle()***
The battle function is the most extensive function in the project. It first acknowledges that a battle has begun and introduces the enemy to the player and reveals the enemy's stats. Then an input will be displayed to the user to choose their attack - "C" for "Close", "R" for "Ranged" or "M" for "Magic" attack.

It will then call the strike_chance() function and if the strike is successful it will call on the is_dead() function which will check if the enemy's health is < then 1 using the Enemy class get_e_health method after a successful hit, if the enemy isn't dead it will set the enemy's new health using the Enemy class set_e_health method minus the damage value from the players stat value. Example below:

damage = guardian.get_ranged() - enemy.get_e_defence()
if strike:
            enemy.set_e_health(enemy.get_e_health() - damage)

Next, it will call the enemy_attack() function, and similar to the above it will call on the is_dead() function which will check if the player's health is < then 1 using the Guardian class get_health method after a successful hit, if the player isn't dead it will set the player's new health using the Guardian class set_health method minus the damage value from the enemy's attack stat value. Example below:

loss = attack_value - defence
guardian.set_health(guardian.get_health() - enemy_attack
                                (enemy.get_e_chance(),
                                enemy.get_e_attack(),
                                enemy.get_e_name(),
                                guardian.get_defence()))

This will continue until either the Player or the Enemy are dead at which stage either the loot() function will be called or the game_over() function.

At the end of each battle if the Player's health is < than 100 the Player's is restored to full health using the Guardian get/set health method see below:

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

## **Bugs & Fixes**

|   **Bug**                                                    |   **Issue**                                                                                                                                                                                                                                                                                                                  |   **Resolution**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Directional buttons used for Name input                |   When user entered directional buttons in the Name input text was shifted upwards and over lapped ascii text                                                                                                                                                                                                             |   Added isalnum() to the input to resolve the issue and handled errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|   Guardian Luck stat > than 10                           |   When multiple luck loot dropped players luck stat would go above 10, this meant player always hit the enemy which wasn’t intended                                                                                                                                                                                       |   After every loot drop I set the function to check if the luck stat was > than 10 and if it was I used the Guardian set_luck method to set the Luck stat to 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|   Guardian Defence Stat > than Enemy Attack              |   When multiple Defence loot dropped the player's Defence stat could become higher then the Enemy's attack stat which ended up applying a minus attack value which added health to the Player instead of taken health away                                                                                                |   After every loot drop I set the function to check if the Defence stat was > than 13 and if it was I used the Guardian set_defence method to set the Defence stat to 13 as the Enemy stat is between 14 & 20 for base enemy and 15 & 25 for Boss                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|   Enemy Defence Stat > than Gaurdians lowest Attack      |   Guardian attack stats are set values depending on class chosen, some attack stats were set to 5. When testing I originally had the Enemy Defence stat set to a random value between 1& 10 so when it was above 5 and Player used that attack instead of health being taken off the Enemy it was adding health to them.  |   To resolve I set the Enemy Defence stat to the max value of the lowest Player attack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|   Path choice function was showing previous input        |   As the path_choice function takes in the users input as an argument when it was incorrect the user would be asked for the input again but would display the last input entered - this was occuring because I was trying to change the variable when the user was asked again to input choice                            |   To resolve I changed choice to choice2 in the function and issue was resolved.     `   def path_choice(choice, select_1, select_2,                   error, function_1, function_2):       '''       Function used throughout the game to       direct the story depending on your choice.       '''       choice2 = input(Fore.GREEN + Style.BRIGHT + choice +                       Style.RESET_ALL).lower().strip(" ")       if choice2 == select_1:           function_1()       elif choice2 == select_2:           function_2()       else:           print(error)           path_choice(choice, select_1, select_2, error, function_1, function_2)       print(Style.RESET_ALL)   `  |
|   Guardian Luck stat set to random value between 7 & 10  |   For the enemy to drop loot the Guardians luck stat would have to be above 7, with the initaial values this meant the enemy always dropped loot which was not intended                                                                                                                                                   |   To resolve I changed the Guardians luck stat to start between a value of 4 & 6 to vary loot drops                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|   Ascii art showing error                                |   When I pasted in Ascii art I received a lot of errors like the below:   invalid escape sequence '\'   Anomalous backslash in string: '\'                                                                                                                                                                                |   Upon investigating and many searches on Stackoverflow I was advised to convert the string to a raw string by placing a lowercase "r" in front of the text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|   App not launching after Heroku deployment              |   App would not open when deployed on Heroku - this was caused by the Requirements.txt being empty                                                                                                                                                                                                                        |   To resolve I entered the command pip3 list to get the list of modules being used and manually placed them in the Requirements.txt       I later found you could use the below commands to avoid manually doing this:       pip freeze > requirements.txt       pip install -r requirements.txt                                                                                                                                                                                                                                                                                                                                                                                              |

[Return to README.md](README.md)