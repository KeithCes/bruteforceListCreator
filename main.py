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


f1 = open("LOG.txt", "w+")


def listGenerate():
    print("Please input the max value of digits you want the generator \
to create(1-6): ")
    userInput = int(input())
    print()
    maxRange = 0
    if userInput == 1:
        maxRange = 26
    elif userInput == 2:
        maxRange = 702
    elif userInput == 3:
        maxRange = 18278
    elif userInput == 4:
        maxRange = 475254
    elif userInput == 5:
        maxRange = 12356630
    elif userInput == 6:
        maxRange = 321272406
    else:
        print("Please input a valid/smaller range: ")
    loops = 1
    iterate6(loops, maxRange)


def iterate(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            lst.append(str(carry) + "a")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 2:
            lst.append(str(carry) + "b")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 3:
            lst.append(str(carry) + "c")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 4:
            lst.append(str(carry) + "d")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 5:
            lst.append(str(carry) + "e")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 6:
            lst.append(str(carry) + "f")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 7:
            lst.append(str(carry) + "g")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 8:
            lst.append(str(carry) + "h")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 9:
            lst.append(str(carry) + "i")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 10:
            lst.append(str(carry) + "j")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 11:
            lst.append(str(carry) + "k")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 12:
            lst.append(str(carry) + "l")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 13:
            lst.append(str(carry) + "m")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 14:
            lst.append(str(carry) + "n")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 15:
            lst.append(str(carry) + "o")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 16:
            lst.append(str(carry) + "p")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 17:
            lst.append(str(carry) + "q")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 18:
            lst.append(str(carry) + "r")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 19:
            lst.append(str(carry) + "s")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 20:
            lst.append(str(carry) + "t")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 21:
            lst.append(str(carry) + "u")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 22:
            lst.append(str(carry) + "v")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 23:
            lst.append(str(carry) + "w")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 24:
            lst.append(str(carry) + "x")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 25:
            lst.append(str(carry) + "y")
            loops += 1
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        elif loops == 26:
            lst.append(str(carry) + "z")
            loops = 0
            maxRange -= 1
            f1.write("".join(lst) + "\n")
        lst.clear()


def iterate2(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            iterate(1, 26, lst, str(carry) + "a")
            loops += 1
            maxRange -= 26
        elif loops == 2:
            iterate(1, 26, lst, str(carry) + "b")
            loops += 1
            maxRange -= 26
        elif loops == 3:
            iterate(1, 26, lst, str(carry) + "c")
            loops += 1
            maxRange -= 26
        elif loops == 4:
            iterate(1, 26, lst, str(carry) + "d")
            loops += 1
            maxRange -= 26
        elif loops == 5:
            iterate(1, 26, lst, str(carry) + "e")
            loops += 1
            maxRange -= 26
        elif loops == 6:
            iterate(1, 26, lst, str(carry) + "f")
            loops += 1
            maxRange -= 26
        elif loops == 7:
            iterate(1, 26, lst, str(carry) + "g")
            loops += 1
            maxRange -= 26
        elif loops == 8:
            iterate(1, 26, lst, str(carry) + "h")
            loops += 1
            maxRange -= 26
        elif loops == 9:
            iterate(1, 26, lst, str(carry) + "i")
            loops += 1
            maxRange -= 26
        elif loops == 10:
            iterate(1, 26, lst, str(carry) + "j")
            loops += 1
            maxRange -= 26
        elif loops == 11:
            iterate(1, 26, lst, str(carry) + "k")
            loops += 1
            maxRange -= 26
        elif loops == 12:
            iterate(1, 26, lst, str(carry) + "l")
            loops += 1
            maxRange -= 26
        elif loops == 13:
            iterate(1, 26, lst, str(carry) + "m")
            loops += 1
            maxRange -= 26
        elif loops == 14:
            iterate(1, 26, lst, str(carry) + "n")
            loops += 1
            maxRange -= 26
        elif loops == 15:
            iterate(1, 26, lst, str(carry) + "o")
            loops += 1
            maxRange -= 26
        elif loops == 16:
            iterate(1, 26, lst, str(carry) + "p")
            loops += 1
            maxRange -= 26
        elif loops == 17:
            iterate(1, 26, lst, str(carry) + "q")
            loops += 1
            maxRange -= 26
        elif loops == 18:
            iterate(1, 26, lst, str(carry) + "r")
            loops += 1
            maxRange -= 26
        elif loops == 19:
            iterate(1, 26, lst, str(carry) + "s")
            loops += 1
            maxRange -= 26
        elif loops == 20:
            iterate(1, 26, lst, str(carry) + "t")
            loops += 1
            maxRange -= 26
        elif loops == 21:
            iterate(1, 26, lst, str(carry) + "u")
            loops += 1
            maxRange -= 26
        elif loops == 22:
            iterate(1, 26, lst, str(carry) + "v")
            loops += 1
            maxRange -= 26
        elif loops == 23:
            iterate(1, 26, lst, str(carry) + "w")
            loops += 1
            maxRange -= 26
        elif loops == 24:
            iterate(1, 26, lst, str(carry) + "x")
            loops += 1
            maxRange -= 26
        elif loops == 25:
            iterate(1, 26, lst, str(carry) + "y")
            loops += 1
            maxRange -= 26
        elif loops == 26:
            iterate(1, 26, lst, str(carry) + "z")
            loops = 0
            maxRange -= 26
        elif maxRange == 26:
            iterate(1, maxRange, [], "")
            maxRange -= 26
        lst.clear()


def iterate3(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            iterate2(1, 676, lst, str(carry) + "a")
            loops += 1
            maxRange -= 676
        elif loops == 2:
            iterate2(1, 676, lst, str(carry) + "b")
            loops += 1
            maxRange -= 676
        elif loops == 3:
            iterate2(1, 676, lst, str(carry) + "c")
            loops += 1
            maxRange -= 676
        elif loops == 4:
            iterate2(1, 676, lst, str(carry) + "d")
            loops += 1
            maxRange -= 676
        elif loops == 5:
            iterate2(1, 676, lst, str(carry) + "e")
            loops += 1
            maxRange -= 676
        elif loops == 6:
            iterate2(1, 676, lst, str(carry) + "f")
            loops += 1
            maxRange -= 676
        elif loops == 7:
            iterate2(1, 676, lst, str(carry) + "g")
            loops += 1
            maxRange -= 676
        elif loops == 8:
            iterate2(1, 676, lst, str(carry) + "h")
            loops += 1
            maxRange -= 676
        elif loops == 9:
            iterate2(1, 676, lst, str(carry) + "i")
            loops += 1
            maxRange -= 676
        elif loops == 10:
            iterate2(1, 676, lst, str(carry) + "j")
            loops += 1
            maxRange -= 676
        elif loops == 11:
            iterate2(1, 676, lst, str(carry) + "k")
            loops += 1
            maxRange -= 676
        elif loops == 12:
            iterate2(1, 676, lst, str(carry) + "l")
            loops += 1
            maxRange -= 676
        elif loops == 13:
            iterate2(1, 676, lst, str(carry) + "m")
            loops += 1
            maxRange -= 676
        elif loops == 14:
            iterate2(1, 676, lst, str(carry) + "n")
            loops += 1
            maxRange -= 676
        elif loops == 15:
            iterate2(1, 676, lst, str(carry) + "o")
            loops += 1
            maxRange -= 676
        elif loops == 16:
            iterate2(1, 676, lst, str(carry) + "p")
            loops += 1
            maxRange -= 676
        elif loops == 17:
            iterate2(1, 676, lst, str(carry) + "q")
            loops += 1
            maxRange -= 676
        elif loops == 18:
            iterate2(1, 676, lst, str(carry) + "r")
            loops += 1
            maxRange -= 676
        elif loops == 19:
            iterate2(1, 676, lst, str(carry) + "s")
            loops += 1
            maxRange -= 676
        elif loops == 20:
            iterate2(1, 676, lst, str(carry) + "t")
            loops += 1
            maxRange -= 676
        elif loops == 21:
            iterate2(1, 676, lst, str(carry) + "u")
            loops += 1
            maxRange -= 676
        elif loops == 22:
            iterate2(1, 676, lst, str(carry) + "v")
            loops += 1
            maxRange -= 676
        elif loops == 23:
            iterate2(1, 676, lst, str(carry) + "w")
            loops += 1
            maxRange -= 676
        elif loops == 24:
            iterate2(1, 676, lst, str(carry) + "x")
            loops += 1
            maxRange -= 676
        elif loops == 25:
            iterate2(1, 676, lst, str(carry) + "y")
            loops += 1
            maxRange -= 676
        elif loops == 26:
            iterate2(1, 676, lst, str(carry) + "z")
            loops = 0
            maxRange -= 676
        elif maxRange == 26:
            iterate(1, maxRange, [], "")
            maxRange -= 26
        elif maxRange == 702:
            iterate2(1, maxRange, [], "")
            maxRange -= 702
        lst.clear()


def iterate4(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            iterate3(1, 17576, lst, str(carry) + "a")
            loops += 1
            maxRange -= 17576
        elif loops == 2:
            iterate3(1, 17576, lst, str(carry) + "b")
            loops += 1
            maxRange -= 17576
        elif loops == 3:
            iterate3(1, 17576, lst, str(carry) + "c")
            loops += 1
            maxRange -= 17576
        elif loops == 4:
            iterate3(1, 17576, lst, str(carry) + "d")
            loops += 1
            maxRange -= 17576
        elif loops == 5:
            iterate3(1, 17576, lst, str(carry) + "e")
            loops += 1
            maxRange -= 17576
        elif loops == 6:
            iterate3(1, 17576, lst, str(carry) + "f")
            loops += 1
            maxRange -= 17576
        elif loops == 7:
            iterate3(1, 17576, lst, str(carry) + "g")
            loops += 1
            maxRange -= 17576
        elif loops == 8:
            iterate3(1, 17576, lst, str(carry) + "h")
            loops += 1
            maxRange -= 17576
        elif loops == 9:
            iterate3(1, 17576, lst, str(carry) + "i")
            loops += 1
            maxRange -= 17576
        elif loops == 10:
            iterate3(1, 17576, lst, str(carry) + "j")
            loops += 1
            maxRange -= 17576
        elif loops == 11:
            iterate3(1, 17576, lst, str(carry) + "k")
            loops += 1
            maxRange -= 17576
        elif loops == 12:
            iterate3(1, 17576, lst, str(carry) + "l")
            loops += 1
            maxRange -= 17576
        elif loops == 13:
            iterate3(1, 17576, lst, str(carry) + "m")
            loops += 1
            maxRange -= 17576
        elif loops == 14:
            iterate3(1, 17576, lst, str(carry) + "n")
            loops += 1
            maxRange -= 17576
        elif loops == 15:
            iterate3(1, 17576, lst, str(carry) + "o")
            loops += 1
            maxRange -= 17576
        elif loops == 16:
            iterate3(1, 17576, lst, str(carry) + "p")
            loops += 1
            maxRange -= 17576
        elif loops == 17:
            iterate3(1, 17576, lst, str(carry) + "q")
            loops += 1
            maxRange -= 17576
        elif loops == 18:
            iterate3(1, 17576, lst, str(carry) + "r")
            loops += 1
            maxRange -= 17576
        elif loops == 19:
            iterate3(1, 17576, lst, str(carry) + "s")
            loops += 1
            maxRange -= 17576
        elif loops == 20:
            iterate3(1, 17576, lst, str(carry) + "t")
            loops += 1
            maxRange -= 17576
        elif loops == 21:
            iterate3(1, 17576, lst, str(carry) + "u")
            loops += 1
            maxRange -= 17576
        elif loops == 22:
            iterate3(1, 17576, lst, str(carry) + "v")
            loops += 1
            maxRange -= 17576
        elif loops == 23:
            iterate3(1, 17576, lst, str(carry) + "w")
            loops += 1
            maxRange -= 17576
        elif loops == 24:
            iterate3(1, 17576, lst, str(carry) + "x")
            loops += 1
            maxRange -= 17576
        elif loops == 25:
            iterate3(1, 17576, lst, str(carry) + "y")
            loops += 1
            maxRange -= 17576
        elif loops == 26:
            iterate3(1, 17576, lst, str(carry) + "z")
            loops = 0
            maxRange -= 17576
        elif maxRange == 26:
            iterate(1, maxRange, [], str(carry) + "")
            maxRange -= 26
        elif maxRange == 702:
            iterate2(1, maxRange, [], str(carry) + "")
            maxRange -= 702
        elif maxRange == 18278:
            iterate3(1, maxRange, [], str(carry) + "")
            maxRange -= 18278
        lst.clear()


def iterate5(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            iterate4(1, 456976, lst, str(carry) + "a")
            loops += 1
            maxRange -= 456976
        elif loops == 2:
            iterate4(1, 456976, lst, str(carry) + "b")
            loops += 1
            maxRange -= 456976
        elif loops == 3:
            iterate4(1, 456976, lst, str(carry) + "c")
            loops += 1
            maxRange -= 456976
        elif loops == 4:
            iterate4(1, 456976, lst, str(carry) + "d")
            loops += 1
            maxRange -= 456976
        elif loops == 5:
            iterate4(1, 456976, lst, str(carry) + "e")
            loops += 1
            maxRange -= 456976
        elif loops == 6:
            iterate4(1, 456976, lst, str(carry) + "f")
            loops += 1
            maxRange -= 456976
        elif loops == 7:
            iterate4(1, 456976, lst, str(carry) + "g")
            loops += 1
            maxRange -= 456976
        elif loops == 8:
            iterate4(1, 456976, lst, str(carry) + "h")
            loops += 1
            maxRange -= 456976
        elif loops == 9:
            iterate4(1, 456976, lst, str(carry) + "i")
            loops += 1
            maxRange -= 456976
        elif loops == 10:
            iterate4(1, 456976, lst, str(carry) + "j")
            loops += 1
            maxRange -= 456976
        elif loops == 11:
            iterate4(1, 456976, lst, str(carry) + "k")
            loops += 1
            maxRange -= 456976
        elif loops == 12:
            iterate4(1, 456976, lst, str(carry) + "l")
            loops += 1
            maxRange -= 456976
        elif loops == 13:
            iterate4(1, 456976, lst, str(carry) + "m")
            loops += 1
            maxRange -= 456976
        elif loops == 14:
            iterate4(1, 456976, lst, str(carry) + "n")
            loops += 1
            maxRange -= 456976
        elif loops == 15:
            iterate4(1, 456976, lst, str(carry) + "o")
            loops += 1
            maxRange -= 456976
        elif loops == 16:
            iterate4(1, 456976, lst, str(carry) + "p")
            loops += 1
            maxRange -= 456976
        elif loops == 17:
            iterate4(1, 456976, lst, str(carry) + "q")
            loops += 1
            maxRange -= 456976
        elif loops == 18:
            iterate4(1, 456976, lst, str(carry) + "r")
            loops += 1
            maxRange -= 456976
        elif loops == 19:
            iterate4(1, 456976, lst, str(carry) + "s")
            loops += 1
            maxRange -= 456976
        elif loops == 20:
            iterate4(1, 456976, lst, str(carry) + "t")
            loops += 1
            maxRange -= 456976
        elif loops == 21:
            iterate4(1, 456976, lst, str(carry) + "u")
            loops += 1
            maxRange -= 456976
        elif loops == 22:
            iterate4(1, 456976, lst, str(carry) + "v")
            loops += 1
            maxRange -= 456976
        elif loops == 23:
            iterate4(1, 456976, lst, str(carry) + "w")
            loops += 1
            maxRange -= 456976
        elif loops == 24:
            iterate4(1, 456976, lst, str(carry) + "x")
            loops += 1
            maxRange -= 456976
        elif loops == 25:
            iterate4(1, 456976, lst, str(carry) + "y")
            loops += 1
            maxRange -= 456976
        elif loops == 26:
            iterate4(1, 456976, lst, str(carry) + "z")
            loops = 0
            maxRange -= 456976
        elif maxRange == 26:
            iterate(1, maxRange, [], str(carry) + "")
            maxRange -= 26
        elif maxRange == 702:
            iterate2(1, maxRange, [], str(carry) + "")
            maxRange -= 702
        elif maxRange == 18278:
            iterate3(1, maxRange, [], str(carry) + "")
            maxRange -= 18278
        elif maxRange == 475254:
            iterate4(1, maxRange, [], str(carry) + "")
            maxRange -= 475254
        lst.clear()


def iterate6(loops, maxRange):
    currentList = []
    while maxRange > 0:
        if maxRange == 26:
            iterate(1, maxRange, [], "")
            maxRange -= 26
        elif maxRange == 702:
            iterate2(1, maxRange, [], "")
            maxRange -= 702
        elif maxRange == 18278:
            iterate3(1, maxRange, [], "")
            maxRange -= 18278
        elif maxRange == 475254:
            iterate4(1, maxRange, [], "")
            maxRange -= 475254
        elif maxRange == 12356630:
            iterate5(1, maxRange, [], "")
            maxRange -= 12356630
        elif loops == 1:
            iterate5(1, 11881376, currentList, "a")
            loops += 1
            maxRange -= 11881376
        elif loops == 2:
            iterate5(1, 11881376, currentList, "b")
            loops += 1
            maxRange -= 11881376
        elif loops == 3:
            iterate5(1, 11881376, currentList, "c")
            loops += 1
            maxRange -= 11881376
        elif loops == 4:
            iterate5(1, 11881376, currentList, "d")
            loops += 1
            maxRange -= 11881376
        elif loops == 5:
            iterate5(1, 11881376, currentList, "e")
            loops += 1
            maxRange -= 11881376
        elif loops == 6:
            iterate5(1, 11881376, currentList, "f")
            loops += 1
            maxRange -= 11881376
        elif loops == 7:
            iterate5(1, 11881376, currentList, "g")
            loops += 1
            maxRange -= 11881376
        elif loops == 8:
            iterate5(1, 11881376, currentList, "h")
            loops += 1
            maxRange -= 11881376
        elif loops == 9:
            iterate5(1, 11881376, currentList, "i")
            loops += 1
            maxRange -= 11881376
        elif loops == 10:
            iterate5(1, 11881376, currentList, "j")
            loops += 1
            maxRange -= 11881376
        elif loops == 11:
            iterate5(1, 11881376, currentList, "k")
            loops += 1
            maxRange -= 11881376
        elif loops == 12:
            iterate5(1, 11881376, currentList, "l")
            loops += 1
            maxRange -= 11881376
        elif loops == 13:
            iterate5(1, 11881376, currentList, "m")
            loops += 1
            maxRange -= 11881376
        elif loops == 14:
            iterate5(1, 11881376, currentList, "n")
            loops += 1
            maxRange -= 11881376
        elif loops == 15:
            iterate5(1, 11881376, currentList, "o")
            loops += 1
            maxRange -= 11881376
        elif loops == 16:
            iterate5(1, 11881376, currentList, "p")
            loops += 1
            maxRange -= 11881376
        elif loops == 17:
            iterate5(1, 11881376, currentList, "q")
            loops += 1
            maxRange -= 11881376
        elif loops == 18:
            iterate5(1, 11881376, currentList, "r")
            loops += 1
            maxRange -= 11881376
        elif loops == 19:
            iterate5(1, 11881376, currentList, "s")
            loops += 1
            maxRange -= 11881376
        elif loops == 20:
            iterate5(1, 11881376, currentList, "t")
            loops += 1
            maxRange -= 11881376
        elif loops == 21:
            iterate5(1, 11881376, currentList, "u")
            loops += 1
            maxRange -= 11881376
        elif loops == 22:
            iterate5(1, 11881376, currentList, "v")
            loops += 1
            maxRange -= 11881376
        elif loops == 23:
            iterate5(1, 11881376, currentList, "w")
            loops += 1
            maxRange -= 11881376
        elif loops == 24:
            iterate5(1, 11881376, currentList, "x")
            loops += 1
            maxRange -= 11881376
        elif loops == 25:
            iterate5(1, 11881376, currentList, "y")
            loops += 1
            maxRange -= 11881376
        elif loops == 26:
            iterate5(1, 11881376, currentList, "z")
            loops = 0
            maxRange -= 11881376
        currentList.clear()


listGenerate()
