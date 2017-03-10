# MayaTools
A series of useful utility scripts that I have created for myself for working in Maya

**AttrAdder.py:** a script allowing a user to simultaneously add multiple attributes to an object. There are still some bugs with it, and I havent put any safeties on the text fields or readio buttons yet, so it may not work exactly as intended

**ColorOverrider.py:**  GUI based tool that will set the drawing override color of an object. Useful for changing the color of controllers

**batchRename.py:**  a script that will currently take a given filename and extension and swap the number and extension. I use this when I forget to change the render output settings to NAME.###.EXT. Right now you have to manually adjust the code to choose the file, but I am working on making it more generalized as well as providing a GUI in Maya for any potential students working on machines without access to the python executable

**ControlCreate.mel:**  a mel script that allows the creation of custom controllers. only a few available now. There will be more in addition to an eventual GUI implementation and a translation to python

**uiConverter.py:** a simple python gui for converting a Qt .ui file into a python file via pysideuic