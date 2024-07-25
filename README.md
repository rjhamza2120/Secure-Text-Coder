# Secure-Text-Coder
SecureTextCoder is designed to meet these needs by providing an intuitive and interactive platform for encoding and decoding messages. It offers you a robust set of features that allow users to transform their text into secure, coded messages and effortlessly decode them when needed. 

Here's a breakdown of its functionality:
## Key Features:

The program displays a welcome message with three options:

• Check the rules

• Encode or decode a message

• Exit

### Check the Rules:

When the user selects this option, they are prompted to enter a code to access the rules.
If the entered code matches one of the predefined codes ("bravo", "dragon", "itshello"), the program displays the encoding and decoding rules:

#### • Encoding Rules:

  » If the word has at least 3 characters, remove the first letter and append it at the end.
  
  » Append three random characters at the beginning and end.
  
  »For words with fewer than 3 characters, simply reverse the string.

#### • Decoding Rules:

  » For words with fewer than 3 characters, reverse it.
  
  » Otherwise, remove 3 random characters from the start and end, then move the last letter to the beginning.
  
  » If the entered code is incorrect, the program prompts the user to enter the correct code.

### Encode or Decode:

When the user selects this option, they are prompted to choose between encoding or decoding a message.

#### • Encoding:

The user enters a message, which is then encoded based on the rules:

  »For single-character words, the word is unchanged.
  
  »For two-character words, the characters are swapped.
  
  »For words with three or more characters, the first letter is moved to the end, and "cbi" is appended at the start and end.
  
  »The encoded message is displayed.


#### • Decoding:

The user enters a message, which is then decoded based on the rules:

  »For single-character words, the word is unchanged.

  »For two-character words, the characters are swapped.
  
  »For words with three or more characters, the first and last three characters are removed, and the last letter is moved to the beginning.

  »The decoded message is displayed.


### Exit:

The program terminates when the user selects this option.
