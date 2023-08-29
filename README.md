# RIOWPW

Python Wrapper for Raytracing Program Written in C++

# Usage:

Select a `json file` containing an existing scene structure (see examples for now).

Now you can either edit the objects or start generating an image.
Just select the image format such as `PNG` or `JPG` and then press generate.
When the image finished generating you should see it on screen.
You can also select to store the image after generation if you wish to.

# Editing Objects:
Press on an Object or Group, this will open their according GUI.
Here you can modify size, scale, rotation or special attributes such
as reflection and so on.
After you have modified it, save it.
After saving, if you wish to apply the modifcation, save the `json file` in
the bottom right corner and load the changes by loading the same file now. 
This is not how we want to do it, but we currently handle it this way.
