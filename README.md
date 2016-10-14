# proj3-anagrams
Vocabularly anagrams game for primary school English language learners (ELL)


## Overview

A simple anagram game designed for English-language learning students in 
elementary and middle school.  
Students are presented with a list of vocabulary words (taken from a text file) 
and an anagram.  The anagram is a jumble of some number of vocabulary words, randomly chosen.  Students attempt to type vocabularly words that can be created from the  
jumble.  When a matching word is typed, it is added to a list of solved words. 

The vocabulary word list is fixed for one invocation of the server, so multiple
students connected to the same server will see the same vocabulary list but may 
have different anagrams.

## Authors 

Initial version by  

## Status

flask_vocab.py and the template vocab.html are a 'skeleton' version 
use AJAX interaction on each keystroke to send and revieve message to server through json 

Use TrieTree replace vocab for search word in wordlist,which is faster than binary search

trietree use dict for search and return the prefix match wordlist for highlight

If the user types a character is not in the anagram, erase it, so that the user gets the illusion that only letters from the anagram "work".

At each keystroke, highlight words from the vocabulary list that contain all the characters that have been typed so far


## To run automated tests 
* `nosetests`

There are currently nose tests for vocab.py, letterbag.py, and jumble.py. 
now add trie test for trietree.py to nose tests

## To Install and Run
    bash ./configure
    make test    # make all test, should pass 
    make service # service run background



