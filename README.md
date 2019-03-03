To run the program, lemmad.txt and the python script should be in the same folder in your windows computer.
Go to the folder. Then press Shift Key and Right Click. This should give you POWERSHELL in drop-dwon menu.
Open PowerShell. In powershell type:
python AnagramFinder.py and press enter.

This will open a window where you can input your word. Then click the button Find Anagram.
This will show you the result of the word related to lemmad.txt

# findanagraminlemmad.txt
a lemmad.txt file is provided. we write a python program to find anagram in it against the user input.

The program displays the anagram found as well as the time taken to find the Anagram.


I have developed this program for windows, as I am not currently familiar with LINUX. 

The program can be further modified to become a generic anagram finder with any file input, however, in this case I have only made it to run on lemmad.txt

The testing it went through looks like this:
1. Input was given of words whose anagram are there in the lemmad.txt , for example kama. This returns the Anagram found
2. Input was give for words that don't have any matching word or anagram in lemmad.txt , for example ???cdsbbv . This tells user about Angram not found
3. Input was given of words that are in the lemmad.txt as it is but don't have anagrams. For example: word AIDS is found in lemmad.txt but it's anagram is not there in the file. This tells the user that we found the word but not it's Anagram.
4. Input is given with words containing spaces. Space doesn't make any difference and Anagram is found if lemmad.txt has any words in a single line with spaces that happens to be anagram.
5. Fringe cases with strange alphabets and symbols contined in lemmad.txt are tested. For example: one fringe case is "charge d'affaires"
as it contains " ' " in the word.
