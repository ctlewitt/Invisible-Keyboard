Invisible-Keyboard
==================

Invisible keyboard project for the purpose of reading Zach's mother's mind.  (Or predicting what words are being typed based on finger-presses detected by gloves.)  

Zach did the hardware (gloves, arduino). I (Charley) did the software (processing word frequency data, interpreting input from gloves, displaying results) which is hosted here.

This is meant to be used with a pair of gloves with censors in the fingertips to detect finger presses (to be used instead of a keyboard.)  The gloves send signals indicating finger presses to the computer, which displays the most likely words the user meant to type.  

To test this online without the gloves, visit the Google App Engine site below.  To simulate the experience of typing with gloves, keep your fingers on the home row keys.  In other words, type words using only the characters: a, s, d, f, j, k, l, ;, and space to represent the finger presses corresponding to the left pinky finger, left ring finger, left middle finger, left pointer, right pointer, right middle finger, right ring finger, right pinkey, and either thumb, respectively.  For example, if you want to type the word "hello", you would type "jdlll".  Different people's experiences may vary since everyone types a little differently, and we haven't accounted for this yet.  (e.g., some people type a 'b' with their left pointer finger, while others type it with their right pointer finger.) <br>
http://invisible-keyboard.appspot.com/

Currently this does the following:<br>
1) Gloves read in sequences of finger presses, corresponding to 10 fingers (rather than the full keyboard complement of characters)<br>
2) After pressing "Submit for Translation," the sequences of finger presses are translated into possible words, sorted by word use frequency.  

This relies on Google's word frequency data, which has been cleaned up and merged with a list of the most commonly used English words.  For speed, these words have been sorted by frequency and mapped to possible finger-press combinations for quick retrieval.  
The outer folder contains the files used to clean the Google 1-gram data, merge it with a list of frequently used words, and create a data stucture for quick retrieval.  The inner folder contains the files used to take users' input and display the words they meant to type.  

Possible next steps:<br>
1) process finger-presses and display words as they're typed, instead of waiting for typing to finish<br>
2) allow user to add words to "dictionary"<br>
3) allow users to train to software to interpret words based on their personal typing style (log in to access your already trained software.)  This would probably work by associating a user with a dictionary/data structure that matches their typing style, or create a new one if no existing one matches their typing style.  

Google N-Gram Data used (I used the 1-gram data, for single words' frequencies):<br>
http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

Most commonly used English words (to help remove superfluous words from Google 1-grams):<br>
http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
