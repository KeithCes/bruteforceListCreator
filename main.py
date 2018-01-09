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
    loops2 = 1
#    loops3 = 0
    if maxRange > 0:
        iterate(loops1, 3, 1)
        maxRange -= 3
    if maxRange > 0:
        iterate(loops2, 9, 2)
        maxRange -= 9


def iterate(loops, localRange, loopNumber):
    currentList = []
    while localRange > 0:
        if loops == 1:
            currentList.append("a")
            loops += 1
        elif loops == 2:
            currentList.append("b")
            loops += 1
        elif loops == 3:
            currentList.append("c")
            loops = 0
        localRange -= 1
        resetList(currentList)


def resetList(lst):
    print("".join(lst))
    lst.clear()


listGenerate()
