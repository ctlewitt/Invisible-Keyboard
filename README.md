Invisible-Keyboard
==================

Invisible keyboard project for the purpose of reading Zach's mother's mind.  (Or predicting what words are being typed based on finger-linked keystrokes on an invisible keyboard.)  

This is based on an idea that Zach came up with.  His ideas on how to do this are below:

mom's invisible keyboard project

begun 8/30/14

scheme:

1) record finger sequences (use serial stream to communicate)
2) identify words based on letter timing (or spaces?)
3) for a given word, calculate all possible letter-stroke combinations
4) select only valid words against the dictionary
   http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
5) display these as quickly as they're calculated
