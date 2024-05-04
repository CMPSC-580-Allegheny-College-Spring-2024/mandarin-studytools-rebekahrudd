# Project Prototype

TODO: The result of your work will be the delivery of some type of proof-of-concept prototype which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). All source code for the prototype must be stored in this directory. If your prototype uses data, please create `data/` subdirectory in `src/` and include your data file(s) in `src/data/` directory.

To allow the user to experience and execute your prototype, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Key Features

This prototype opens a file and crops a file. In addition this prototype has the foundational outline of a website to make flashcards.

## Requirements

* This program runs using Python so some version of Python 3.8 or newer is necessary.

* Future work: installing poetry

## Using the Prototype

### Opening a Photo

In order to use this prototype the command `python main.py` must be run from inside the `a_readin_copy` folder. The reason it must be run from inside this folder is because I was trying to set of the `a_photo_readin` with poetry so that `main.py` file utilizes the `poetry run` and different command line input run promts.
1. Run `python main.py` from inside the `a_readin_copy` directory
2. When the computer prompts you to "Enter the image name:" Enter: "img1.png" but with out quotations
3. Based on the image pulled up and dimension markers of it put in the amount you want cropped
4. Close the image in order to be prompted to crop the photo.

### Using the Flashcard Website

1. Visit the `c_flashcards` directory
2. In Finder/Your Files double click on the `edit.html` file in order to make a flashcard
