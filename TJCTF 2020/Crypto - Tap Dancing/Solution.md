## Challenge: Tap Dancing
## Category: Crypto

### Prompt:
> Written by agcdragon My friend is trying to teach me to dance, but I am not rhythmically coordinated! They sent me a list of dance moves but they're all numbers! Can you help me figure out what they mean so I can learn the dance? NOTE: Flag is not in flag format.

`1101111102120222020120111110101222022221022202022211`

### Solution:
My initial reaction was to check if the given string was base 3. Unsurprisingly, it wasn't.

Given the title "**Tap** Dancing" I suspected the string was obfuscated morse code. Replacing 1 with ".", 2 with "-", and 0 with " ", I got `.. ..... -.- --- - .- ..... . .--- ----. --- - ---.. = I5KOTA5EJ9OT8`.

Replacing 1 with "-", 2 with ".", and 0 with " ", I got `-- ----- .-. ... . -. ----- - -... ....- ... . ...-- = M0RSEN0TB4SE3` which was the flag.

### Flag:
M0RSEN0TB4SE3