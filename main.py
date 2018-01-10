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
        maxRange = 26
    elif userInput == 2:
        maxRange = 702
    elif userInput == 3:
        maxRange = 18278
    else:
        print("Please input a valid/smaller range: ")
    loops = 1
    iterate3(loops, maxRange)


def iterate(loops, maxRange, lst, carry):
    while maxRange > 0:
        if loops == 1:
            lst.append(str(carry) + "a")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 2:
            lst.append(str(carry) + "b")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 3:
            lst.append(str(carry) + "c")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 4:
            lst.append(str(carry) + "d")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 5:
            lst.append(str(carry) + "e")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 6:
            lst.append(str(carry) + "f")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 7:
            lst.append(str(carry) + "g")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 8:
            lst.append(str(carry) + "h")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 9:
            lst.append(str(carry) + "i")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 10:
            lst.append(str(carry) + "j")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 11:
            lst.append(str(carry) + "k")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 12:
            lst.append(str(carry) + "l")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 13:
            lst.append(str(carry) + "m")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 14:
            lst.append(str(carry) + "n")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 15:
            lst.append(str(carry) + "o")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 16:
            lst.append(str(carry) + "p")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 17:
            lst.append(str(carry) + "q")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 18:
            lst.append(str(carry) + "r")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 19:
            lst.append(str(carry) + "s")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 20:
            lst.append(str(carry) + "t")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 21:
            lst.append(str(carry) + "u")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 22:
            lst.append(str(carry) + "v")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 23:
            lst.append(str(carry) + "w")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 24:
            lst.append(str(carry) + "x")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 25:
            lst.append(str(carry) + "y")
            loops += 1
            maxRange -= 1
            print("".join(lst))
        elif loops == 26:
            lst.append(str(carry) + "z")
            loops = 0
            maxRange -= 1
            print("".join(lst))
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


def iterate3(loops, maxRange):
    currentList = []
    while maxRange > 0:
        if maxRange == 26:
            iterate(1, maxRange, [], "")
            maxRange -= 26
        elif maxRange == 702:
            iterate2(1, maxRange, [], "")
            maxRange -= 702
        elif loops == 1:
            iterate2(1, 676, currentList, "a")
            loops += 1
            maxRange -= 676
        elif loops == 2:
            iterate2(1, 676, currentList, "b")
            loops += 1
            maxRange -= 676
        elif loops == 3:
            iterate2(1, 676, currentList, "c")
            loops += 1
            maxRange -= 676
        elif loops == 4:
            iterate2(1, 676, currentList, "d")
            loops += 1
            maxRange -= 676
        elif loops == 5:
            iterate2(1, 676, currentList, "e")
            loops += 1
            maxRange -= 676
        elif loops == 6:
            iterate2(1, 676, currentList, "f")
            loops += 1
            maxRange -= 676
        elif loops == 7:
            iterate2(1, 676, currentList, "g")
            loops += 1
            maxRange -= 676
        elif loops == 8:
            iterate2(1, 676, currentList, "h")
            loops += 1
            maxRange -= 676
        elif loops == 9:
            iterate2(1, 676, currentList, "i")
            loops += 1
            maxRange -= 676
        elif loops == 10:
            iterate2(1, 676, currentList, "j")
            loops += 1
            maxRange -= 676
        elif loops == 11:
            iterate2(1, 676, currentList, "k")
            loops += 1
            maxRange -= 676
        elif loops == 12:
            iterate2(1, 676, currentList, "l")
            loops += 1
            maxRange -= 676
        elif loops == 13:
            iterate2(1, 676, currentList, "m")
            loops += 1
            maxRange -= 676
        elif loops == 14:
            iterate2(1, 676, currentList, "n")
            loops += 1
            maxRange -= 676
        elif loops == 15:
            iterate2(1, 676, currentList, "o")
            loops += 1
            maxRange -= 676
        elif loops == 16:
            iterate2(1, 676, currentList, "p")
            loops += 1
            maxRange -= 676
        elif loops == 17:
            iterate2(1, 676, currentList, "q")
            loops += 1
            maxRange -= 676
        elif loops == 18:
            iterate2(1, 676, currentList, "r")
            loops += 1
            maxRange -= 676
        elif loops == 19:
            iterate2(1, 676, currentList, "s")
            loops += 1
            maxRange -= 676
        elif loops == 20:
            iterate2(1, 676, currentList, "t")
            loops += 1
            maxRange -= 676
        elif loops == 21:
            iterate2(1, 676, currentList, "u")
            loops += 1
            maxRange -= 676
        elif loops == 22:
            iterate2(1, 676, currentList, "v")
            loops += 1
            maxRange -= 676
        elif loops == 23:
            iterate2(1, 676, currentList, "w")
            loops += 1
            maxRange -= 676
        elif loops == 24:
            iterate2(1, 676, currentList, "x")
            loops += 1
            maxRange -= 676
        elif loops == 25:
            iterate2(1, 676, currentList, "y")
            loops += 1
            maxRange -= 676
        elif loops == 26:
            iterate2(1, 676, currentList, "z")
            loops = 0
            maxRange -= 676
        currentList.clear()

listGenerate()
