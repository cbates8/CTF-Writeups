## Challenge: Titanic
## Category: Crypto

### Prompt:
> Written by jpes707 I wrapped tjctf{} around the lowercase version of a word said in the 1997 film "Titanic" and created an MD5 hash of it: 9326ea0931baf5786cde7f280f965ebb.

### Solution:
To solve this challenge, I knew I had to make a wordlist from the script of the movie "Titanic."

I used the tool [Mentalist](https://github.com/sc0tfree/mentalist) to make a custom wordlist of every word found in the script of "Titanic" wrapped inside tjct{}. And for good measure, I also added every word in the english dictionary to the wordlist.

I then used [Hashcat](https://github.com/hashcat/hashcat) to crack the given MD5 hash using my custom wordlist. At first it worked, and Hashcat cracked the **old** hash `e246dbab7ae3a6ed41749e20518fcecd` to get the flag `tjctf{ismay's}`.

However, the admin had to change the flag do to another team leaking the original flag, so this method no longer produced the correct flag. My original wordlist no longer worked for the new hash, so instead of using the film's script for my wordlist, I used the film's subtitles.

Adding subtitles to my wordlist did the trick, and Hashcat cracked the new hash `9326ea0931baf5786cde7f280f965ebb` to get the flag `tjctf{marlborough's}`.

### Flag:
tjctf{marlborough's}