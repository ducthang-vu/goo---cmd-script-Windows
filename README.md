# GOO
GOO is a simple python script for Windows command line for automatic searching on Google.


## FEATURES
This script accepts one or more arguments to be used for searching on google. 

The google page shall be opened on the browser.

The script will also parse the google page and get all links. Then, it will open on the browser up to five links, provided that those links contain any of the keywords stored in goo.txt.

goo.txt contains the following text: "mozilla,programiz,reddit,stackoverflow,twitter,w3school". goo.txt can of course be modified at will, provided that the keywords are separated only by commas (,).


## Usage
1 - Download the repository.  
2 - Modify goo.bat by writing the full path of goo.py.  
3 - You may modify goo.txt at will and at any time, when necessary. Keywords must be separated only by commas (,).  
4 - Set environment variables by adding the folder path of goo.bat.  
5 - Open Command Prompt and write "goo" followed by an arbitrary number of arguments. Then press "enter" to start the script.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
