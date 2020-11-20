# Caesar-Cipher
Hey Hackers! Blue Cosmo from CCS here and today I want to give an update on the progress of the CodeX Project. I have started work on the first cipher of the project, The Caesar Cipher! Here's a an overview of the cipher and a video will be releasing soon. Make sure to subscribe to the channel to be notified of it's release.

## Project Name: The CodeX Project [Caesar-Cipher]


## Implementation:
-Symmetric Encryption Method

-Named after Julius Caesar

-Works through index change down the alphabet
```
	WITHOUT CIPHER - [Shift of 0]

	A=1, B=2, C=3, D=4...Z=26


	WITH CIPHER - [Shift of 1]

	A=26, B=1, C=2, D=3...Z=25


	Plaintext = "Hello, World!"

	Ciphertext = "Ifmmp, Xpsme!" 
```
| Computers don't understand English alphabet indexing, but they do understand UNICODE [A = 65, a = 97]


## Algorithms:
```
Encryption:

		C = (X + N) % 26

Decryption:

		C = (X - N) % 26
```
C - encoded character

X - index of character

N - # of indexes that we need to replace [shift key]


## Algorithms [Python]:
```
Encryption:

		Uppercase: 

                plaintext += chr((ord(letter) + shift - 65) % 26 + 65)
		Lowercase: 

                plaintext += chr((ord(letter) + shift - 97) % 26 + 97)
Decryption:

		Uppercase: 

                ciphertext += chr((ord(letter) - shift - 65) % 26 + 65)
		Lowercase: 

                ciphertext += chr((ord(letter) - shift - 97) % 26 + 97)
```
ord() - matches character to Unicode index

chr() - matches index to Unicode character

| Additional character added at the end of the encryption algorithm's output

## Bruteforcing:
Bruteforcing a Caesar Cipher encryption is pretty easy because there are only 26 possible shift keys. 

| How is that possible? ['A' has an index of 1 & 'Z' has an index of 26] Because 'Z' is the last letter, there is no index higher than 26. So once 'Z' receives a shifted index of 1, it can has to recycle back to 26 because there are no other indexes. Therefore, if the shift key is 36, than the shift key is also equal to 10.

In order to bruteforce this cipher, all we have to do is decrypt the cyphertext 26 times. Each of those times with a different key ranging from 0 to 26.

## Background:
I chose to start with the Caesar Cipher because it was essentially the inspiration for this whole project. This was the encryption that was used in the codex pages from Assassins Creed II. I figured it would be the most appropriate of the ciphers to begin with. Besides that, thanks for reading this weeks issue; and as always,

Happy Hacking!
