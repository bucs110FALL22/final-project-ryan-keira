:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Air Hockey Game 
## CS 110 Final Project
### Fall Semester, 2022
### [We will make an air hockey game which consists of two players using their paddles to move the puck towards their opponent's goal. The goals will end when 1 player scores 5 goals.](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/ttoakbpsvm-ryanfanchiotti1

<< [link to demo presentation slides](#) >>

### Team: Ryan & Keira
#### Ryan Fanchiotti, Keira Talty

***

## Project Description

We will create an air hockey game with the standard components: a puck, 2 strikers, 2 goals, a table, and a score board. The two players will compete until 1 of them has scored 5 goals.After a goal is scored, the puck and the two strikers are reset to their respective positions. Once a player has scores 5 goals, the game closes.

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components.
  -
  1- The first screen will be of the table, the puck in the middle, and the two strikers on their respective ends
  2-Game in action where the discs (controlled by the two players) are moving 
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 

* Non-Standard libraries
-Import pygame: Imports all available pygame modules
<https://www.pygame.org/docs/>
-Import time: Allows the use of a time limit.
<https://www.programiz.com/python-programming/time>

* Class Interface Design
1.https://drive.google.com/file/d/15NihmahqCwvTF28L0J5oBpENMaMZL49b/view?usp=share_link
2.https://drive.google.com/file/d/1P-p7bvIMJ7E5gX9uqrfvbZYYx0iO-b57/view?usp=share_link
  
* Classes
1.Puck: Puck will move up, down, left, and right.
2.Goal: Goal will move left and right.
3.Table: Table will be an image on which the puck will move on.
3.Player 1: Will be either blue or green team. Will be able to use w, w, s, and d arrowkeys to move puck.
4.Player 2: Will be able to hit the puck using the 4 arrowkeys.

  
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * We worked together on all parts.

## Testing

* We plan to fix any bug as we go

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Open terminal, enter 'python3 main.py' | Opens start screen where player is assigned disc color |
|  2                   | Player 1 uses keys W,S,A,D to control player. Player 2 uses the 4 arrow keys| Strikers move accordingly |                        
|  3                   | Player scores a goal by moving puck into opponent's goal| Counter on scoreboard rises accordingly |
|  4                   | A player scores 5 goals | Game closes|   

