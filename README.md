# Reclaim The Light

## **Overview**

Reclaim The Light is a text based adventure game that includes PVE elements. It is loosly based on the Destiny Universe and this is where I drew my inspiration the project.

The game is aimed at every audience but may be enjoyed alot more by the older generations who grew up with text adventure games and fans of the Destiny universe.

Developed by Sean Finn.

![EZGIF Animation](/docs/gifs/reclaim_1.gif)

[Reclaim The Light - Live Webpage](https://reclaim-the-light.herokuapp.com/) (Right-click to open in a new tab)

## **Project Goals**

This is my third portfolio project for [Code Institute](https://codeinstitute.net/) and my goal with this project is to display my newly acquired Python skills. I decided to build a classic text based adeventure game that included some PvE battle elements. The adventure is led by the players choices and each choice has an impact on how the story progresses.

## **Contents**

1. [Overview](#overview)
1. [Project Goals](#project-goals)
1. [Design](#design)
    - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
1. [How to Play](#how-to-play)
    - [Setup Phase](#setup-phase)
    - [How to Win](#how-to-win)
    - [Wireframes](#wireframes)
1. [Features](#features)
1. [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks and Tools Used](#frameworks-and-tools-used)
1. [Testing](#testing)
    - [Validators](Validators)
    - [Accessibility and Performance](#accessibility-and-performance)
    - [Further Testing](#further-testing)
    - [Testing User Stories from the User Experience (UX) Section](#testing-user-stories-from-the-user-experience-ux-section)
    - [Bugs and Fixes](#bugs-and-fixes)
1. [Future Updates](#future-updates)
1. [Deployment](#deployment)
1. [Credits](#credits)
1. [Acknowledgements](#acknowledgements)

## **Design**

### **Imagery**

I have included Ascii text and Ascii art throughout the adventure to grab the users attention and provide and asthectically pleasing experience.

### **Colour Scheme**

I used the Colorama Library to apply coloring to my project. Green and Red are used the most throughout along with Blue for the pause() functions. CYAN, MAGENTA & YELLOW were used to display the loot items. I have changed the background of the page to Black and added a White border to the terminal to contrast well with the text and colors used.

## **How to Play**

Reclaim The Light is a very easy game to play, all the player needs to do is input letters that correspond to the the choices provided to the player. The player's goal is to retrieve the Light cyrstal that was stolen by the evil creatures known as the Darkness. The Player will be sent on an adventure to the planet Nessus to fight the Darkness and Reclaim The Light.

### **Setup Phase:**

The player will be asked for their name and be requested to pick a class for their "Guardian", the classes are "W" for "Warrior" , "A" for "Assasin" or "M" for "Mage". After that they will shown a screen containing their Guardian stats.

### **How to Win:**

The player will make choices that will lead them into battles on occasion, if the players survives they will move on to the next part of the adventure leading to a boss battle at the end. If they defeat the boss they will Reclaim The Light and win the game. 

## **User Stories:**
As a user, I want to be able to:
* Understand the aim of the story.
* Have a straightforward way to read the game instructions from within.
* To access a fun engaging story narrative throughout the game.
* Find loot and upgrade my stats.

## **Features**

### **Welcome Screen**
The user is met with a bright Welcome Screen with some colored ascii text to provide an asthectically pleasing experience. There are 3 options to choose from Start, Mission Log or About.
![Welcome Screen](/docs/screenshots/welcome.webp)

### **Mission Log**
`
User Story: As a user, I want to be able to understand the aim of the story.
`

The Mission Log provides the user with the backstory and the aim of the game. It is displayed to the user using the type print animation followed up with the pause function imported from the py-getch Library. This allows the user to take their time reviewing the Mission Log text before pressing any key to return to Welcome Screen.
![Mission Log](/docs/screenshots/mission_log.webp)

### **About**
`
User Story: As a user, I want to have a straightforward way to read the game instructions from within.
`

The About section provide the user with details of what the game is and the instructions for the game. There is also a section that provides information on each Guardian class Warrior, Assassin or Mage. This will give the user a better idea on what class they would like to pick for the game.
![About](/docs/screenshots/about.webp)

### **Start**

When the user selects Start they will be brought to a screen with some bright ascii text welcoming them to the game. They will then be prompted to enter a name for their Guardian which consists of only letters and numbers. The user upon completing that stage will be prompted to select 1 of the 3 possible classes provided Warrior, Assassin or Mage. After the user completes that step they will see the text - "Generating Guardian"
![Start](/docs/screenshots/setup.webp)

### **Stats**

When the user has completed the Start setup they will be provided with a screen that displays some wepaon related ascii art along with their Guardian stats. The stats consist of 6 values (Attack, Defense, Health, Luck, Magic and Range) followed by the users name. The stats are all generated using the gen_char() function that calls on the Guardian class. The stats change based off the class chosen by the the user i.e. If they choose Mage the Magic stat will be higher compared to the other classes. The only stat that doesnt have a set value is the Luck stat which is generated within the gen_char() function and is setup to be a random value i.e. luck = random.randint(4, 6)
![Stats](/docs/screenshots/stats.webp)

### **Adventure Story**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the user has reviewed their stats they can press and button to begin the adventure. Each of the main narratives provides the user with a either bright ascii text or some ascii art that is related to that narrative the user is currently viewing. The text will again be displaying using the type print animation to draw the users attention to the screen. At the end of the narrative the user will be offered 2 choices, each choice sends the user on a different path allowing for a fun and engaging game.
![Adventure Story](/docs/screenshots/nessus.webp)

### **Loot**
`
User Story: As a user, I want find loot and upgrade my stats.
`

Theres are three forms of loot in the game - Common, Legendary & Exotic. Each item of loot contains a Rarity, Name, Value & stat Assignement i.e. Common - Worn Sword - 1 - Attack.

Common items have a Value of 1, Legendary items have a Value of 2 and Exotic items have a Value of 3. Loot values are added to the players stats when the are found in chests or dropped from enemies. Image below consists of what the user will see (examples):

Common items are displayed in the color CYAN

Legendary items are displayed in the color MAGENTA

Exotic items are displayed in the color YELLOW
![Loot](/docs/screenshots/loot.webp)

### **Battle Sequence**

#### **Initiating Battle**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the user has entered into a fight with an enemy a new screen will display containing the following:

Ascii art - I choose a skull head to engage the user and its colored in red to draw the users attention to the screen.

Enemy name - The enemy name is taken randomly from the enemy.txt file. Its colored in red to draw the users attention to the screen.

Enemy stats - The enemy stats are generated using the gen_enemy() function that calls the Enemy class. The stats consist of Health, Attack, Defense, Chance and Name. Each stat generates a random number between the values set in the function i.e. health = random.randint(80, 100)
![Initiating Battle](/docs/screenshots/battle.webp)

#### **Engaged in Battle**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the battle begins user will have first turn to attack, they will be prompted to enter "C" for "Close attack", "R" for "Ranged" attack or "M" for "Magic" attack.

After selecting an attack the following text will display: "You wind up for the attack..."

The strike_chance() function is called to determine whether the players attack is successful. If attack is successful the amount of health lost by the enemy is calculated by the attack value used minus the enemys defense value i.e. 

if choice == "c":
            damage = guardian.get_attack() - enemy.get_e_defence()

The user will be alerted that their attack was successful and the enemy's new health stat will be displayed. If the user's attack was not successful the following text will be displayed: "You missed! Enemy dodged your attack".

It will be the enemy's turn now, the enemy_attack() function is now called to determine if enemy attack will be successful. If attack is successful the amount of health lost by the user is calculated by the attack value used minus the user's defense value i.e. 

loss = attack_value - defence

If enemy attack is successful the user will be alerted and their new health stat will be displayed.

Some of the text displayed with the color Red to engage the user and signify the imagery of blood lost.

![Engaged in Battle](/docs/screenshots/battle1.webp)

#### **Battle Victory**
`
User Story: As a user, I want find loot and upgrade my stats.
`

If the enemy is defeated by the user the user will be alerted i.e. "Centurian, has been slain!"

The loot() function is then called. It picks a randomint between 0 and 7 and if the value provided is greater then the users current luck value the enemy wont drop any loot and the following text will display: "That creature dropped no loot..."

If the users luck value is greater then the randomint then the enemy will drop loot. It will be displayed to the user with the text "The enemy dropped an....." along with the loot values retreived from the loot .txt files. The value of the loot will be added to the user's current stats and stats will be displayed to the user.

![Battle Victory](/docs/screenshots/battle2.webp)

#### **Battle Lost**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

If the user is defeated a new screen will be displayed alerting the user that they have been slain along with some Game Over ascii art. The user will also see some text advising to press any key to return to Welcome Screen.

![Battle Lost](/docs/screenshots/gameover.webp)

### **Adventure Victory Screen**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

If the user completes the adventure without dying they will be provided a message stating that they "Reclaimed The Light" and a thank you message. Ascii Text along with ascii art is used here to grab the users attention. The user will be then prompted to return to the Welcome Screen where they can start another adventure if they choose to do so.

![EZGIF Animation](/docs/gifs/reclaim_2.gif)




## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks and Tools Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Poppins' font into the .css files used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for the icons throughout the project and the social media icons in the footer for aesthetic and UX purposes.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/seanf316/P1-Vanguard/tree/main/assets/wireframes) during the design process.
1. [XConvert](www.xconvert.com)
    - XConvert was used to convert images to webp or png where required.
1. [Stackoverflow](https://stackoverflow.com/)
    - Stackoverflow was used on many occasions to figure out some troublesome code.
1. [W3schools](https://www.w3schools.com/)
    - W3schools provided the tutorial to create the ["Modal Box"](https://www.w3schools.com/howto/howto_css_modals.asp) that was used for the site instructions.
1. [W3C HTML Validator](https://validator.w3.org/)
    - I used W3C HTML Validator for the validation of the site's HTML code.
1. [W3C JigSaw Validator](https://jigsaw.w3.org/css-validator/)
   - I used W3C JigSaw Validator for the validation of the site CSS code.
1. [JSHint](https://jshint.com/)
   - I used JSHint for the validation of the site js code.
1. [Grammarly](https://www.grammarly.com/)
    - Grammarly was used to check typography.
1. [Techsini.com](https://techsini.com/multi-mockup/)
    - Techsini.com was used to produce the website mockup.
1. [favicon.io](https://favicon.io/)
    - favicon.io was used to create my site's favicon.
1. [Canva](https://www.canva.com/)
    - Canva was used to create the site logo.

[Back to top &uarr;](#contents)

## Testing

### Validators

The W3C Markup Validator, W3C CSS Validator & JSHint Services were used to validate the code used in the project to ensure there were no syntax errors.
<details><summary>W3C Markup Validator</summary>

![W3C Markup Validator Homepage Results](/docs/readme/validation/homepage-results.PNG)
![W3C Markup Validator Quiz Results](/docs/readme/validation/quiz-results.PNG)
![W3C Markup Validator Highscores Results](/docs/readme/validation/highscores-results.PNG)
![W3C Markup Validator Thank You Results](/docs/readme/validation/thankyou-results.PNG)
![W3C Markup Validator 404 Results](/docs/readme/validation/404-results.PNG)

</details>
<details><summary>W3C CSS Validator</summary>

![W3C CSS Validator Results](/docs/readme/validation/css-results.PNG)

</details>

<details><summary>JSHint</summary>

![JSHint Results](/docs/readme/validation/jshint-results.PNG)

</details>

### Accessibility and Performance

To check the accessibility of my site, I used the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) and received no errors in the result:
<details><summary>WAVE Web Accessibility Evaluation Tool</summary>

![WAVE Web Accessibility Evaluation Tool Results](/docs/readme/validation/wave-results.PNG)

</details>

For performance and more accessibility testing, I used Google Lighthouse throughout:

#### Lighthouse Results

<details><summary>Desktop</summary>

Homepage

![Lighthouse Desktop Score](/docs/readme/validation/desktop-homepage-results.PNG)

Highscores

![Lighthouse Desktop Score](/docs/readme/validation/desktop-highscores-results.PNG)

Quiz

![Lighthouse Desktop Score](/docs/readme/validation/desktop-quiz-results.PNG)

Thank You

![Lighthouse Desktop Score](/docs/readme/validation/desktop-thankyou-results.PNG)

404

![Lighthouse Desktop Score](/docs/readme/validation/desktop-404-results.PNG)

</details>

<details><summary>Mobile</summary>

Homepage

![Lighthouse Mobile Score](/docs/readme/validation/mobile-homepage-results.PNG)

Highscores

![Lighthouse Mobile Score](/docs/readme/validation/mobile-highscores-results.PNG)

Quiz

![Lighthouse Mobile Score](/docs/readme/validation/mobile-quiz-results.PNG)

Thank You

![Lighthouse Mobile Score](/docs/readme/validation/mobile-thankyou-results.PNG)

404

![Lighthouse Mobile Score](/docs/readme/validation/mobile-404-results.PNG)

</details>

#### Lighthouse errors

At Mobile, the Performance score is between 95-100 - This is due to Cumulative Layout Shift. As the site is setup to move dynamically depending on what should be displayed this is the highest score achievable at the moment, in future I will look to see what else can be done.

### Further Testing

The site was scaled from a width of 320px in Chrome Dev Tools to check that the site was responsive. There were no apparent issues but it is worth mentioning that the site was built with Portrait orientation in mind but user can view in Landscape although there would be some scrolling to do which would be expected. I found a site called browserstack.com that simulated some of the most recent mobile phones and I just tested the quiz output on a variety of devices - again this is a simulation in the lines of the Dev Tools offered by chrome.

<details><summary>Manual Testing</summary>

| **Location** | **Feature Tested**       | **Expected Result**                                                                                                                                        | **Actual Result** | **Pass/Fail** |
|--------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|---------------|
| Homepage     | Logo Anchor To Homepage  | Clicking Logo returns user to Homepage                                                                                                                     | As Expected       | Pass          |
|              | Highscores Button        | Clicking Highscores button sends user to the Highscores Page                                                                                               | As Expected       | Pass          |
|              | Instructions Modal       | Clicking Instructions button opens Instructions modal                                                                                                      | As Expected       | Pass          |
|              |                          | Clicking close icon or clicking out outside modal closes modal                                                                                             | As Expected       | Pass          |
|              | Let's get started Button | Clicking Let's get started Button starts the quiz                                                                                                          | As Expected       | Pass          |
|              | Sign Up inputs -required | User cannot sign up without filling in inputs                                                                                                              | As Expected       | Pass          |
|              | Sign Up email input      | Email input requires "@" or user cant signup                                                                                                               | As Expected       | Pass          |
|              | Sign Up Button           | Clicking Sign Up button sends user to the Thank You Page                                                                                                   | As Expected       | Pass          |
|              | Social Media Icons       | Clicking the individual Social Media Icons opens their site in a blank tab                                                                                 | As Expected       | Pass          |
|              | Github Icon              | Clicking the Github Icon opens up the project repo                                                                                                         | As Expected       | Pass          |
| Thank You    | Return Home Button       | Clicking Return Home button sends user to the Homepage                                                                                                     | As Expected       | Pass          |
| Quiz         | Loader                   | Loader should display before the quiz is ready                                                                                                             | As Expected       | Pass          |
|              | Logo Anchor To Homepage  | Clicking Logo returns user to Homepage                                                                                                                     | As Expected       | Pass          |
|              | Timer                    | Timer starts at 90 seconds and counts down to 0                                                                                                            | As Expected       | Pass          |
|              |                          | Timer at 0 quiz closes and end results show                                                                                                                | As Expected       | Pass          |
|              | Sound                    | Clicking sound icon turns on/off audio                                                                                                                     | As Expected       | Pass          |
|              |                          | Audio On - clicking on an answer plays the button click audio                                                                                              | As Expected       | Pass          |
|              |                          | Audio On - correct answer plays the correct audio                                                                                                          | As Expected       | Pass          |
|              |                          | Audio On - incorrect answer plays the incorrect audio                                                                                                      | As Expected       | Pass          |
|              |                          | Audio Off - No Audio                                                                                                                                       | As Expected       | Pass          |
|              | Questions                | Question received from API and displayed in the question text area                                                                                         | As Expected       | Pass          |
|              | Answers                  | Answers received from API and displayed in the answers text area                                                                                           | As Expected       | Pass          |
|              | Check Answer Button      | Clicking Check Answer button without selecting an answer displays - Please select an Answer                                                                | As Expected       | Pass          |
|              |                          | Display  - Please select an Answer hides after .5sec                                                                                                       | As Expected       | Pass          |
|              |                          | Clicking Check Answer button after selecting the correct answer displays - Correct Answer (also applies .correct css class)                                | As Expected       | Pass          |
|              |                          | Clicking Check Answer button after selecting the incorrect answer displays - Incorrect Answer and shows correct Answer (also applies .incorrect css class) | As Expected       | Pass          |
|              | Question Counter         | Question counter increments with each new question                                                                                                         | As Expected       | Pass          |
|              | Progress Bar             | Progress Bar increments with each new question                                                                                                             | As Expected       | Pass          |
| End Results  | Logo Anchor To Homepage  | Clicking Logo returns user to Homepage                                                                                                                     | As Expected       | Pass          |
|              | Score = 0                | Displays message advising users they scored 0 and the need to play again to get their name on Leaderboard, Displays Play Again & Home buttons              | As Expected       | Pass          |
|              |                          | Play Again button restarts quiz                                                                                                                            | As Expected       | Pass          |
|              |                          | Home button returns user to Homepage                                                                                                                       | As Expected       | Pass          |
|              | Score > 0                | Under logo final score is shown i.e. - "You got (correctscore) out of 10"                                                                                  | As Expected       | Pass          |
|              |                          | Final text/quote displays i.e. "Good job my friend"  & "Movie Quote"                                                                                       | As Expected       | Pass          |
|              |                          | Final text produces different results based off user score                                                                                                 | As Expected       | Pass          |
|              |                          | Username input and instruction text appears & Save Button appears                                                                                          | As Expected       | Pass          |
|              | Username Input           | Username between 4 & 10 characters enables the save button                                                                                                 | As Expected       | Pass          |
|              |                          | Username with less than 4 or more than 10 characters disables the save button                                                                              | As Expected       | Pass          |
|              |                          | Use of spaces in input disabled                                                                                                                            | As Expected       | Pass          |
|              |                          | Entering in between 4 & 10 characters hides username instruction text                                                                                      | As Expected       | Pass          |
|              | Save Button              | Clicking Save button sends user to Highscores page                                                                                                         | As Expected       | Pass          |
|              |                          | Highscores displays the username and their score and date                                                                                                  | As Expected       | Pass          |
| Highscores   | Logo Anchor To Homepage  | Clicking Logo returns user to Homepage                                                                                                                     | As Expected       | Pass          |
|              | 10 Highscores            | Only 10 scores are displayed in the Leaderboard                                                                                                            | As Expected       | Pass          |
|              |                          | If recent score is less then the top 10 scores in the Leaderboard then it is not updated                                                                   | As Expected       | Pass          |
|              | Home Button              | Clicking Home button sends user to Homepage                                                                                                                | As Expected       | Pass          |
|              | Play Again Button        | Clicking Play Again button starts Quiz                                                                                                                     | As Expected       | Pass          |
|              | Clear Highscores         | Clicking Clear Highscores button clears Leaderboard and returns user to Homepage                                                                           | As Expected       | Pass          |
| 404          | 404 Page                 | When user navigates to a location on site that doesn’t exist 404 page displays                                                                             | As Expected       | Pass          |
|              | Return Home Button       | Clicking Return Home button returns user to Homepage                                                                                                       | As Expected       | Pass          |

</details>

<details><summary>Browser Testing</summary>

| **Browser Tested** | **Actual Result** | **Pass/Fail** |
|--------------------|-------------------|---------------|
| Chrome             | As Expected       | Pass          |
| Firefox            | As Expected       | Pass          |
| Edge               | As Expected       | Pass          |
| Mac OS Safari      | As Expected       | Pass          |

</details>

<details><summary>Physical Device Testing</summary>

| **Device Tested** | **Actual Result** | **Pass/Fail** |
|-------------------|-------------------|---------------|
| Samsung Note 10+  | As Expected       | Pass          |
| Samsung S21+      | As Expected       | Pass          |
| Samsung Tab S7+   | As Expected       | Pass          |
| iPhone 13 Pro Max | As Expected       | Pass          |
| iPhone 11         | As Expected       | Pass          |
| iPad Pro 12 inch  | As Expected       | Pass          |
| One Plus 8T  | As Expected       | Pass          |
| Alcatel (Unsure of model) | As Expected       | Pass          |

</details>

<details><summary>Browserstack.com</summary>

![Browserstack Image](/docs/readme/validation/mobile-simulator.PNG)

</details>

### Testing User Stories from the User Experience (UX) Section

- #### First Time Visitor Goals

    -   As a First Time Visitor, I want to easily understand the main purpose of the site.
        - Upon entering the site, users are automatically greeted with a clean homepage with site logo.
        - The user will be able to understand what the site is about with the text that appears under the logo.
    -   As a First Time Visitor, I want to understand the rules of the quiz.
        - The user will be greeted with some descriptive text of the quiz but there is also an Instructions button that the user can access that goes into further detail on the quiz.
    -   As a First Time Visitor, I want to be able to view the site on multiple devices.
        - I have applied media queries to allow the site to function responsively across multiple devices.

- #### Returning Visitor Goals

    -   As a Returning Visitor, I want to see new questions.
        - The quiz has been setup to fetch questions from the Opentdb API so the user should see new questions when playing again.
    -   As a Returning Visitor, I want to learn more about any updates.
        - There is a sign up section included on the site, by signing up the user will be registered for the site newsletter which will include news on future updates to the site and any new content released.
    -   As a Returning Visitor, I want to find the best way to get in contact with the site developer.
        - The user can sign up and offer their feedback on the site, alternatively they can contact the developer via the social media links provided in the footer. 

-   #### Frequent User Goals

    -   As a Frequent User, I want to be able to view my best scores
        - The site contains a highscores page containing a Leaderboard. The quiz is setup to store the users Quiz scores via local storage of the users device.
    -   As a Frequent User, I want to check to see if there are any new sections added to the site.
        - The user would already be familiar with the website layout and would be able to navigate the site to see if new sections have been added.
    -   As a Frequent User, I want to sign up so that I am emailed any major updates and/or changes to the website.
        - If user signs up they will receive a newsletter containing updates.

### Bugs and Fixes

<details><summary>Bug - User receiving Incorrect result after selecting Correct Answer.</summary>

When questions were fetched from the API special characters were causing an issue when the user would select the correct answer they would get the incorrect result.
![Question Bug](/docs/readme/bugs/question-bug.PNG)
![Question Bug Reason](/docs/readme/bugs/question-bug-reason.PNG)

Fix - Upon researching this issue, I was able to resolve this by taking a function from a GeekProbin video to decode the Html of the correct answer and just display the plain text.
</details>

<details><summary>Bug - At end page browser/mobile back button not reloading quiz</summary>

When the user was on the end of quiz results page they are indicated to enter a username if they score more then 0 or if 0 they are indicated to play again. There is a play again button that would direct them back to the quiz page and all worked as expected but if the user was to click the browser/mobile back button instead the quiz would start again but would not be reloaded to its original state. This caused the amount of questions to go over what was expected and the progress bar width grew outside its container. The problem was not evident in VS Code and could not be replicated there so several commits where done in the testing period to try and resolve.
![End Page Bug](/docs/readme/bugs/endpage-bug.png)

Fix - After numerous attempts and a lot of commits testing various code to try and override/change the back button behavior I decided to remove the endpage.html and implement all the code into the quiz.html. I set the end page section to hidden and revealed it with javascript code at the time required. Now when a user presses the browser/mobile back button they are brought back to the homepage instead of the quiz.
</details>

<details><summary>Bug - Mobile Lighthouse Performance</summary>

Maybe technically not a bug but when the quiz was created and styled I ran my lighthouse checks, on desktop I was getting 100% in Performance but on mobile Performance was between 60%-70%.
![Mobile Performance](/docs/readme/bugs/mobile-lighthouse-bug.png)

Fix - To increase Performance there were several actions I made:
1. Removed Font Awesome script in Header and placed at end of body.
2. Added the following to the Head - link rel="preconnect" href="https://opentdb.com/api.php?amount=10&category=11&type=multiple"
3. Removed the global media queries css file and placed the required css into the quiz.css file.
4. Removed the mediaqueries.css link from the head
5. Went through the css and removed or altered css that was not need or was duplicated for some properties.
6. Reduced margins of the quiz container. Gave some specific widths to elements.
7. Added favicon to remove console errors.
</details>

<details><summary>Bug - API Fetch Issues</summary>

Originally I had the quiz setup to fetch 10 questions and display 1 at a time. I quickly noticed from testing and feedback that there was a small delay between each question as instead of displaying the next question of the 10 fetched it was fetching 10 questions each time.

Fix - To resolve this issue I had watched a James Q Quick video on fetching from an API and took some of the code he had written and applied it to the quiz I had setup. It took awhile to understand the API call but after hours of testing and gaining knowledge it now fetches the 10 questions only once and displays each question from the 10 fetched without delays.

Another issue that came up in testing and from feedback was that the user was sometimes seeing the same question in the same instance of a quiz i.e. 2 of the 10 questions in one game were the same

Fix - To resolve this I simply removed the question that was displayed from the questions array using splice - availableQuestions.splice(questionIndex, 1);
</details>

<details><summary>Bug - Username Input Issues</summary>

Originally I had the input function set to "keyup" event and all seemed well until a class mate noticed that the "Save" button was disabled when they tried to copy and paste their username in.

Fix - To resolve this issue I changed the "keyup" event to "input" and user was now able to copy and paste.

I noticed with testing the user could enter 4 blank spaces as a username and was able to save. This caused the Leaderboard to look bad with no names showing.
![Mobile Performance](/docs/readme/bugs/username-code.PNG)

Fix - To resolved I disabled spaces in the input field and added some instruction text under the input field for the user to review.
</details>

[Back to top &uarr;](#contents)

## Future Updates

I would like to add the following updates in the future when time permits:

1. Global Leaderboard - Instead of scores being saved locally on the user's device they would instead be saved to a database where every user's score would be stored.
2. Categories - I would like to add specific Movie categories like Action, Comedy, Thriller, Sci-Fi, etc.
3. Difficulty Levels - I would like to incorporate difficulty levels like Easy, Medium & Hard.
4. Remaining Time added to the overall score - I want the timer to be more of just a countdown and have more influence on the overall score i.e. Answering correctly faster adds more points to the score.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the repository [P2-Movie-Buff-Or-Bluff](https://github.com/seanf316/P2-Movie-Buff-Or-Bluff)
2. At the top of the Repository (not the top of the page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "Pages" Section on the left side of the page. Click "Pages".
4. In the "Pages" section under "Source" there is a "Branch" section, click the dropdown called "None" select "main" and click save.
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://seanf316.github.io/P2-Movie-Buff-Or-Bluff/) in the "GitHub Pages" section.

### Version Control

For version control the following steps were made:

1. Changes made to files in Gitpod
2. Files made ready for commit with command - git add .
3. For the commits the following command was run along with commit description - git commit -m "This is my commit etc"
4. To move the changes to Github the following command was run - git push  

Please note due to a bug that could not be replicated locally there were a series of commits made to test resolution of bug via published link. - (At end page browser/mobile back button not reloading quiz)

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the repository [P2-Movie-Buff-Or-Bluff](https://github.com/seanf316/P2-Movie-Buff-Or-Bluff)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

[Back to top &uarr;](#contents)

## Credits

1. [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template)
    - This repository was created using the template provided by Code Institute. Also, without the knowledge gained through the course work, I would not be able to create this site so thank you Code Institute.
1. [W3schools](https://www.w3schools.com/)
    - W3schools was used throughout the project process for answering any queries I had.
1. [James Q Quick](https://www.youtube.com/c/JamesQQuick), [Kevin Powell](https://www.youtube.com/kepowob), [Web Dev Simplified](https://www.youtube.com/c/WebDevSimplified), [Code with Ania Kubów](https://www.youtube.com/c/AniaKub%C3%B3w), [Brian Design](https://www.youtube.com/channel/UCsKsymTY_4BYR-wytLjex7A).
    - All of the above for creating fantastic videos on HTML/CSS & Javascript. Javascript was very tough to grasp but with what was learned on the course coupled with the knowledge gained from all of the above and the tutorial videos they produced it slowly started to make sense. I reviewed several videos on building a quiz and took some ideas from different videos and applied them to my own. Any code that was used has been credited in comments in js files. The videos used for inspiration and where some code was acquired are listed below:
    GeekProbin - https://youtu.be/-cX5jnQgqSM
    James Q Quick - https://youtu.be/3aKOQn2NPFs
    Web Dev Simplified - https://youtu.be/riDzcEQbX6k
    Brian Design - https://youtu.be/f4fB9Xg2JEY
1. [Stackoverflow](https://stackoverflow.com/)
    - I found myself on Stackoverflow so many times researching issues with javascript code or the occasional Html/CSS issue. This a fantastic place to learn and troubleshoot code.
1. [Slack](https://slack.com/intl/en-ie/)
    - After finishing the javascript essentials and Love Maths project it was very daunting sitting in front of an empty .js file. The people on Slack and especially my class mates were always willing to lend a hand and some of the mentors on there are just amazing.

## Acknowledgements

- To my amazing wife Denise who has supported me every day and kept me motivated while I have been spending long hours studying and building the site she had to look after and entertain our 5-year-old son so I think I had an easier time of it.
- My son Alex for always making me laugh when I'm tired from a long night of study/coding.
- To my sister Mari for all the help she provided testing on all the Apple devices.
- To my family and friends - for being a great support and providing a lot of the user testing for me.
- To my mentor Daisy Mc Girr, we have only had a few sessions together but she has been a huge help to me.
- My class mates Sean Johnston & Victoria Traynor for reviewing and testing my Project throughout the course.

[Back to top &uarr;](#contents)