# Greed
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more! 

![image](https://user-images.githubusercontent.com/84346969/155809759-7dc5edd3-d4e2-4a7f-995b-f9a6495d6041.png)

## Getting Started

---

## Run the program from an IDE like Visual Studio Code. Start your IDE and open the greed folder. Then open the __main__.py file. Click the "run" button.

## Project Structure

---

The project files are organized as follows:

```

+-- greed               (contains all files)
  +-- data              (stores data for the game)
    +-- messages.txt    (shows you what you have found)
  +-- game              (contains files needed to run the game)
    +-- casting
      +-- __pycache__   (cache)
      +-- actor.py      (A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position and  velocity in 2d space.)
      +-- artifact.py   (A gem or rock.The responsibility of an Artifact is to provide a message about itself.)
      +-- cast.py       (A collection of actors. The responsibility of a cast is to keep track of a collection of actors. It has methods for adding, removing and   getting them by a group name.)
    +-- directing
      +-- __pycache__   (cache)
      +-- director.py   (Gets directional input from the keyboard and applies it to the robot.)
    +-- services
      +-- __pycache__   (cache)
      +-- keyboard_service.py (Detects player input. The responsibility of a KeyboardService is to detect player key presses and translate them into 
                               a point representing a direction.)
      +-- video_service.py (Outputs the game state. The responsibility of the class of objects is to draw the game state 
                            on the screen.)
    +-- shared
      +-- __pycache__   (cache)
      +-- color.py      (A color. The responsibility of Color is to hold and provide information about itself. Color has a few convenience methods for comparing them and converting to a tuple.)
      +-- point.py      (A distance from a relative origin (0, 0). The responsibility of Point is to hold and provide information about itself. Point has a few convenience methods for adding, scaling, and comparing them.)
  +-- __main__.py     (the game handler where everything is called)
+-- README.md         (general info)
```

## Required Technologies

---

- Python 3.8.0

## Authors

---

- Michelle Caceres Assignment- Create README.md file, Debugging - Email: michelle.h.dewar@gmail.com
- Emily Castillo Sandoval Assignment - Create gems/rocks, remove artifacts - Email: cas20037@byui.edu
- Aaron Eardley Assignment - Movement of Gems/Rocks and Player - Email: AaronEardley@gmail.com
- MyeongSeon Lee Assignment - Assign and display score
- Andrés Perez Assignment - ?
