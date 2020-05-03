# GOO
GOO is a simple python script for Windows command line for automatic searching on Google.


## FEATURES
This script accepts one or more arguments to be used for searching on google. The google page shall be open on your browser.

The script will also parse the google page and get all the links. Then it will open the first five links, provided that those links contain any of the keywords stored in goo.txt.

goo.txt contains the following text: "mozilla,programiz,reddit,stackoverflow,twitter,w3school". goo.txt can of course be modified at will, provided that the keywords are separated only by commas (,).


## Usage
1 - Download the repository.  
2 - Modify goo.bat by writing the full path of goo.py.  
3 - Modify line 13 of goo.py by writing the full path of goo.txt.  
4 - Open Command Prompt and write "goo" followed by an arbitrary number of arguments.  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
