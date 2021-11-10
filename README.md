# malicious_commits

Inspired by [The Invisible JavaScript Backdoor](https://certitude.consulting/blog/en/invisible-backdoor/).

Variables in python can start with any [start characters](https://www.asmeurer.com/python-unicode-variable-names/start-characters.html).

An example of using Unicode characters to create secret variables in python can
be shown by creating source code that appears to have a strange arithmetic result.

This is accomplished by using a Halfwidth Hangul Filler (0xffa0) to create a variable
that appears to be another variable and a space character.

```
a = 1       # 'a' followed by a space
b = 1
aﾠ= 2       # 'aﾠ' is the variable using an 'a' and a halfwidth hangul filler
c = aﾠ+ b
print(c)    # prints 3
c = a + b
print(c)    # prints 2
```

[Trojan Source](https://www.trojansource.codes/trojan-source.pdf) is a good
research paper on the topic.
