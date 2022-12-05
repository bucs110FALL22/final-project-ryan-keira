:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Air Hockey Game 
## CS 110 Final Project
### Fall Semester, 2022
### [We will make an air hockey game which consists of two players using their paddles to move the puck towards their opponent's goal. The goals will end when 1 player scores 5 goals.](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/ttoakbpsvm-ryanfanchiotti1

https://docs.google.com/presentation/d/1MsZPW9eEHG65eU5tRXVBQ07tW_jwpzvwOKNaoQly8Xg/edit?usp=sharing

### Team: Ryan & Keira
#### Ryan Fanchiotti, Keira Talty

***

## Project Description

We will create an air hockey game with the standard components: a puck, 2 strikers, 2 goals, and a table. The two players will compete until 1 of them has scored 3 goals. After a goal is scored, the puck and the two strikers are reset to their respective positions. Once a player has scores 3 goals, the game closes. In the consoloe, it will state which player has won.

***    

## User Interface Design

- **Initial Concept**
-Start Screen/Game Screen/Game Over Screen Drawings:
https://drive.google.com/file/d/1GM5FpswUzscjdpm713d-OdZ16uIIxaca/view?usp=sharing

 
    
- **Final GUI*

-Start Screen Screenshot: https://drive.google.com/file/d/1gxEEs9YsMZUFj3sLQdDJNebifuPAJCL6/view?usp=share_link

-Game Play Screen Screenshot:
https://drive.google.com/file/d/1sc0B6OMv7V45DVEQoSJLosXkOBMxZ-RV/view?usp=sharing

-Game Over Screen Screenshot:
https://drive.google.com/file/d/1p4b3sUsOBAftyNDoZAXyawzoUXTog0mR/view?usp=sharing

***        

## Program Design

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
    
* assets
   
* etc
   

***

## Tasks and Responsibilities 

   * We worked together on all parts.

## Testing

* We plan to fix any bug as we go

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Open terminal, enter 'python3 main.py' | Opens start screen where directions show up explaining rules and score |
|  2                   | Player 1 uses keys w,s,a,d to control player. Player 2 uses the 4 arrow keys| Strikers move accordingly |                        
|  3                   | Player scores a goal by moving puck into opponent's goal| Player who scored earns one point |
|  4                   | A player scores 3 goals | Game closes|   

