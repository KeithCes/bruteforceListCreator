"""Copyright (c) 2017 * Keith Cestaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


def listGenerate():
    print("Please input the max value of digits you want the generator to create: ")
    userInput = int(input())
    print()
    maxRange = 0
    if userInput == 1:
        maxRange = 3
    elif userInput == 2:
        maxRange = 12
    elif userInput == 3:
        maxRange = 39
    else:
        print("Please input a valid/smaller range: ")
    loops1 = 1
    iterate3(loops1, maxRange)


def iterate(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            lst.append(str(carry) + "a")
            loops += 1
            maxRange -= 1
        elif loops == 2:
            lst.append(str(carry) + "b")
            loops += 1
            maxRange -= 1
        elif loops == 3:
            lst.append(str(carry) + "c")
            loops = 1
            maxRange -= 1
        print("".join(lst))
        lst.clear()


def iterate2(loops, maxRange, lst, carry):
    while maxRange > 0:
        if maxRange == 3:
            iterate(1, maxRange, [], "")
            maxRange -= 3
        elif loops == 1:
            iterate(1, 3, lst, str(carry) + "a")
            loops += 1
            maxRange -= 3
        elif loops == 2:
            iterate(1, 3, lst, str(carry) + "b")
            loops += 1
            maxRange -= 3
        elif loops == 3:
            iterate(1, 3, lst, str(carry) + "c")
            loops = 1
            maxRange -= 3
        print("".join(lst))
        lst.clear()
    else:
        iterate(1, maxRange, [], "")


def iterate3(loops, maxRange):
    currentList = []
    while maxRange > 0:
        if maxRange == 3:
            iterate(1, maxRange, [], "")
            maxRange -= 3
        elif maxRange == 12:
            iterate2(1, maxRange, [], "")
            maxRange -= 12
        elif loops == 1:
            iterate2(1, 12, currentList, "a")
            loops += 1
            maxRange -= 12
        elif loops == 2:
            iterate2(1, 12, currentList, "b")
            loops += 1
            maxRange -= 12
        elif loops == 3:
            iterate2(1, 12, currentList, "c")
            loops = 1
            maxRange -= 12
        print("".join(currentList))
        currentList.clear()

listGenerate()


