#CharadesJS


Charades: Speak, Draw, Act! is JavaScipt based game which is a bit different from classical charades or Pictionary. I created it for my friends when I was hosting one dinner party. The principle of the game is similar. You are in teams. One person performs, the rest is guessing. Goal of the game is to guess as much words as possible.

The game is on http://www.michaelbrabec.com/charades/

Download the code on – https://github.com/voltain/CharadesJS

How do you play it?
Preparation

Print the Game Board – https://github.com/voltain/CharadesJS/blob/master/img/Game_Plan.png
Open the game on smartphone- http://www.michaelbrabec.com/charades/
Split into teams by 2+ members
Put your team figures (we used jelly beans of different colour) on Start
Demo round

Select one member who will be performing. The rest of the team is guessing
The performer selects options 1,2,3 are difficulty. Higher number = higher difficulty level
Press 1 for demo round
Choose drawing for demo round
Performer reads the word, so no one can see the word from his/her team
Performer passes the phone to opponent team(s), because they can see the word
Guessing team needs to guess the word which is performed
If successful = team receives 1 point
The other team(s) follows the same step
All teams moves to first field on game board (which is drawing)
Following rounds

Team selects performer
Chooses difficulty (Higher number = higher difficulty level)
Task is represented by the icon on game board you stand on
Performs the task
If successful they move on game board by number of difficulty points
If failed, they stay on the same spot (the countdown is 90 seconds)
If the word repeats, you skip it and generate another one
Final round

One of the teams reached finish field
Opponent team(s) selects difficulty and chooses task which needs to be performed
Someone measures 90 seconds countdown
If the finishing team wins the round = they won the game.
If not, they stay on the spot and repeats the round when they are on their turn
Rules

Speak – you can only speak. No acting, using objects. You can’t use the root of the word.
Draw – you can only draw. No speaking, head movements for Yes / No is allowed. You can’t use letters and numbers. You can use symbols.
Act – you can only act with no speaking. Making sounds is allowed. You can’t use other objects and point on real objects around you.
Breaking of the rule results in failed round.
How does it work?
The magic happens on not so many lines of code. There is JSON dictionary with information about task type (draw, speak, act) and difficulty. The application picks randomly words from the dictionary based on the difficulty.

The picked word is inserted to HTML immediately and countdown is reset to 90 seconds. Code is at link – https://github.com/voltain/CharadesJS

Space for improvement
Expand the dictionary
Improved graphics
Create dictionary manager – tool where you can quickly decide whether the word is drawable, actable or speakable and on what difficulty level
Build in virtual game board
Show only the task you are on
Self learning model – the game will learn what words are difficult or easy to perform and suggest shift of the words to different difficulty level
 
