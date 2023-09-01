# Set up guide:

If you are using Unix-style operating system, you might have to replace all the "python" parts of the invoke commands to "python3" in the tasks.py file.


You can have virtualenv installed by using pip install virtualenv. This might make easier to remove unnecessary
dependencies after testing my application.

If you are using virtualenv, first use the command 
```bash
virtualenv venv
```
to create a virtual environment.


Start the application with 
```bash
source venv/Scripts/activate
```
or
```bash
source venv/bin/activate
```

inside virtualenv or normally use 
```bash
pip install -r requirements.txt
```
to install dependencies


## Other commands:

To change the configuration of the application use the command
```bash
invoke config 
```
You can change the configurations by adding one or more of the following lines to the end of the command.
```bash
--length integer_here
```
This will be the length of the generated cave, measured in cells. Input a positive integer.


```bash
--width integer_here
```
This will be the width of the generated cave, measured in cells. Input a positive integer.


```bash
--spanning string_here
```
This will determine whether the process uses minimum spanning tree for the paths, or just the Delaunay triangulation. Type True if you want to use spanning and False if you do not.


So for example, to restore the original configurations, use the command

```bash
invoke config --length 30 --width 30 --spanning True
```


Note: the application does not work well with width and length of 13 or less for each. That is why I removed the option to generate maps with lengths or widths of under 20.


To test the app use the command 
```bash
invoke test
```


To get the coverage report use the command
```bash
invoke coverage-report
```
The command also executes all the tests required. The report will be generated to the directory htmlcov 
