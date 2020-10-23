## Challenge: Bash 1
## Category: Bash

### Solution:
SSHed into the given server using `ssh challenges.auctf.com -p 30040 -l level1` and password `aubie`.

Using `ls` showed that the directory contained a file called "README".

Using `cat README` to print its contents revealed the flag.

### Flag:
auctf{W3lcoM3_2_da_C7F}

