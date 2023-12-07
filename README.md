# Spectral Manor 1.0
#### Video Demo:  <URL HERE>
## Description:
Spectral Manor 1.0 is a game I created to utilize my python knowledge and to give myself an introduction to game development and design. The finished game consist of 235 lines of code. I drew all of the art and used a song from YouTube's Audio Library.

The game involves a ghost player that earns points by feeding the various animals. Each animal spawns at a random location and has a different hunger speed. When touching an animal they player can click the mouse and earn a point if the animal was not full. As the game progresses, the animals spawn faster and faster. The player looses when 5 animals starve.
#### Implemented Components
- Start Screen
- Background Music
- Custom Animated Cursor
- Random Spawn Locations within range and without overlap
- Varying Hunger Speed
- Friend Animation
- Hunger Meter Animation
- Increasing Difficulty with Spawn Speed
- Player Score
- Game Over Screen
## My Story
I decided to learn python when several coworkers had been laid off. I wanted to ensure I had additional skills just incase I was next. At this same time, I was kind of bored at home and considering additional entrepenuer opportunities. I decided that making a video game would be challenging but fun. After taking time to learn python and pygame, I do not think I will be making another game anytime soon. I enjoy my free time too much. :) For anyone curious, my only prior coding has been mostly in Excel & SQL with VBA, PowerQuery, some Dax, HTML, CSS, and AutoHotKey.

## What's in each file?
- **project.py** - used to launch the game
- **test_project.py** - used to test project.py
- **19 .pngs** - used for the background, animaiton, and cursor
- **BGSound.mp3** - for the background music
- **requirements.txt** - a list of modules to install

## Challenges
### General
- **Learning Python** - In general CS50P has been a great course but I did find myself having to use additional resources to fully understand why and how x is related to y. With a full time job, I was able to submit my first assignment on Sept. 4, 2023 and will submit my final project Dec. 7, 2023.
- **Learning Pygame** - For pygame I used a few tutorials on YouTube but for the most part I used the pygame documentation. This module has some of the best documentation for beginners.
### With the Final Project
- **Understanding how to properly use classes** - I think Google Bard is what finally was able to break it down for me. When I had finally completed my game, I rechecked the project requirements and realized I could not have nested functions. This required some additional coding but it did lead to start screen, gameover screen, and background music.
- **Game Design** - Once I decided to make a game, I had to come with the idea. My original idea was a cutsey graveyard cozy game but I had to simplify that in order to produces something by the end of 2023. When I decided on a ghost and animal based game, I did not want to scare the animals away, so I switched to collecting points by feeding them.
- **Game Art** - I quickly learned that the image size I was use to using for digital/print art would not work for game art. It is important to consider image size for performance. Ultimately, I made the images in the exact size I needed without scaling. Either solution led to the somewhat pixely images because of the scale of the game.
- **Game Development** - When making a game, it is important to understand how to break down each function into the tiniest part. For example: I wanted my cursor to be an animated ghost that changed animation when the player fed an animal. For this I had to learn how to change the cursor, how to loop through images, how to change the animaiton time, and how to check for collision. Each element of the game led to 3 and 4 implementaiton aspects.
- **Testing** - I was able to fully play test my game, but I found it difficult to use the required pytest to write test.

## Potential Improvements
- Remove the 1 global variable used
- Add a sound effect when the friends eat
- Better testing

