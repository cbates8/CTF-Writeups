## Challenge: Magically Delicious
## Category: Crypto

### Prompt:
> Can you help me decipher this message?
> Tip: If you're digging into the unicode encoding of the emojis, you're on the wrong track!

```⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄```

### Solution:
I noticed that the emojis were grouped in threes, with a few instances of 🦄🦄 sprinkled in. I assumed this meant that each trio corresponded to a letter, with 🦄🦄 being some sort of word seperating character like '_' or '-'.

The flag format for this CTF is sun{}, so I assumed that the first four trios ⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 correspond to 'sun{' and the last trio ⭐🎈🦄 corresponds to '}'.

Using this information I was able to analyze reppitions in the trios of emojis, I was able to determine the flag looked something like: `ABC{DBEFG-HEIJD-KCEHLMCN-MA-IOK-PKAI-KCEHLMCN-QKIOHL}`. Inputing the characters I already know gave me `sun{DuEFG-HEIJD-KnEHLMnN-Ms-IOK-PKsI-KnEHLMnN-QKIOHL}`.

The title of the challenge and the emojis used reminded me of Lucky Charms cereal, so I guessed that the first word `DuEFG` mapped to `lucky`. This gave me `sun{lucky-HcIJl-KncHLMnN-Ms-IOK-PKsI-KncHLMnN-QKIOHL}`.

Using a combination of frequency analysis techniques and educated guessing, I found that the flag was `sun{lucky-octal-encoding-is-the-best-encoding-method}`

### Flag:
sun{lucky-octal-encoding-is-the-best-encoding-method}