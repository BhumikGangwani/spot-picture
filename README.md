# Spot Picture
A program that attempts to create a potential million-dollar spot-picture.


## Setup
Clone this repository to a local directory. Refer to [GitHub Pages](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for more guidance.

Next, you should install the neccessary packages to run **main.py**: *turtle,* and *random*. You can install these using **pip**:
```
- pip install turtle
```
```
- pip install random
```

Now your setup is completed!

## Running the Code
To run the code, run **main.py**. This will open up a Turtle window and starting drawing spots in a 10 x 10 area with a random color chosen from the pallette of one of many Damian Hirst's spot pictures.

![spot picture](https://github.com/BhumikGangwani/spot-picture/blob/master/hirst%20spot%20picture.jpg)

Pro tip: If you want to extract colors from a different image and update the color pallete, you can open **collect_colors.py** and change the value of the variable "IMAGE" with the absolute or relative location of your image. Make sure that your image is a .jpg file.

Upon changing the code, running **main.py** will extract colors from your image and create a spot picture out of that pallette.
