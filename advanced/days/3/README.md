# Day 3 - Christmas Challenge!

## Welcome to Day 3, a special challenge!

Merry Christmas! The CISS has a day off today, but crime doesn't take time off. While everyone was gone, there was a break-in at our main headquarters.

The thieves were after a collection of files located on our main server. Our systems show that they were able to steal the encryption key and a few files. However, we don't know exactly what they stole.

We have an idea of which file they stole, but without the encryption key, we don't know what it contains. Your job is to crack the encryption and reveal the file contents.

## Mission

Using a simple set of instructions, reveal the encrypted message.

- Each vowel in the encrypted message should be replaced with the next one in this order: ``A,E,I,O,U``. For example, an 'A' would be replaced with an 'E', and an 'E' would be replaced with a 'I'.
- Each number in the encrypted message correlates with a letter in the alphabet, in order. For example, a 1 would be an 'A', 2 would be 'B', etc. **Note:** A standing pipe (``|``) ends numbers. Example: ``25|`` is 'Y', but ``2|5`` is 'BE'.
- Each symbol in the encrypted message correlates with the number that it is shared with on a keyboard. For example, a ! would be a 1, which would then be an 'A', @ would be 2, which would then be 'B', etc. Symbols only go up to ), (which would be a 10, not a 0), which means they only go up to 'J'.
- An underscore ``_`` after a number means to add 1 to the number before converting it to a letter. Underscores come *after* the | which symbolizes the end of a number. For example: ``25|_`` would be 26, which would then be 'Z'.

## Mission Resources:

- [For Loop](https://github.com/MWCSC/documentation/blob/master/python/05-for-loop.md)
- [If Statements](https://github.com/MWCSC/documentation/blob/master/python/03-if-statement.md)
- [Else/Elif Statements](https://github.com/MWCSC/documentation/blob/master/python/04-else-statement.md)

## Information:

- Refer to the Mission Notes.

## Value:

``*U22|% ! 18|_U^% !14|$ 13|%17|_18|25| #*17|_E19|19|_13|!19|``

## Expected Output Format:

- String value
- No numbers or symbols remaining
- No extra newlines

Example:

``Hello World!``
