def wordsearch(search_string):
    result = []
    search_string.replace(" ", "")
    if search_string.isalpha():
        search_string = search_string.upper()
    else:
        result = "Not found!"
        return result

    def up(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif i > 0 and puzzle[i-1][j] == search_string[0]:
            if up(i-1, j, search_string[1:]):
                result.append((i, j))
                return True

    def down(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif i < len(puzzle) - 1 and puzzle[i+1][j] == search_string[0]:
            if down(i+1, j, search_string[1:]):
                result.append((i, j))
                return True

    def left(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j > 0 and puzzle[i][j-1] == search_string[0]:
            if left(i, j-1, search_string[1:]):
                result.append((i, j))
                return True

    def right(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j < len(puzzle[0])-1 and puzzle[i][j+1] == search_string[0]:
            if right(i, j+1, search_string[1:]):
                result.append((i, j))
                return True

    def rightdown(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j < len(puzzle[0])-1 and i < len(puzzle) - 1 and\
                puzzle[i+1][j+1] == search_string[0]:
            if rightdown(i+1, j+1, search_string[1:]):
                result.append((i, j))
                return True

    def leftdown(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j > 0 and i < len(puzzle) - 1 and\
                puzzle[i+1][j-1] == search_string[0]:
            if leftdown(i+1, j-1, search_string[1:]):
                result.append((i, j))
                return True

    def leftup(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j > 0 and i > 0 and puzzle[i-1][j-1] == search_string[0]:
            if leftup(i-1, j-1, search_string[1:]):
                result.append((i, j))
                return True

    def rightup(i, j, search_string):
        if search_string == "":
            result.append((i, j))
            return True
        elif j < len(puzzle[0])-1 and i > 0 and\
                puzzle[i-1][j+1] == search_string[0]:
            if rightup(i-1, j+1, search_string[1:]):
                result.append((i, j))
                return True

    puzzle = [['R', 'U', 'N', 'A', 'R', 'O', 'U', 'N', 'D', 'D', 'L'],
              ['E', 'D', 'C', 'I', 'T', 'O', 'A', 'H', 'C', 'Y', 'V'],
              ['Z', 'Y', 'U', 'W', 'S', 'W', 'E', 'D', 'Z', 'Y', 'A'],
              ['A', 'K', 'O', 'T', 'C', 'O', 'N', 'V', 'O', 'Y', 'V'],
              ['L', 'S', 'B', 'O', 'S', 'E', 'V', 'R', 'U', 'C', 'I'],
              ['B', 'O', 'B', 'L', 'L', 'C', 'G', 'L', 'P', 'B', 'D'],
              ['L', 'K', 'T', 'E', 'E', 'N', 'A', 'G', 'E', 'D', 'L'],
              ['I', 'S', 'T', 'R', 'E', 'W', 'Z', 'L', 'C', 'G', 'Y'],
              ['A', 'U', 'R', 'A', 'P', 'L', 'E', 'B', 'A', 'Y', 'G'],
              ['R', 'D', 'A', 'T', 'Y', 'T', 'B', 'I', 'W', 'R', 'A'],
              ['T', 'E', 'Y', 'E', 'M', 'R', 'O', 'F', 'I', 'N', 'U']]
    for i in range(len(puzzle)):

        for j in range(len(puzzle[0])):

            if puzzle[i][j] == search_string[0]:
                up(i, j, search_string[1:])
                down(i, j, search_string[1:])
                left(i, j, search_string[1:])
                right(i, j, search_string[1:])
                rightdown(i, j, search_string[1:])
                rightup(i, j, search_string[1:])
                leftdown(i, j, search_string[1:])
                leftup(i, j, search_string[1:])
    result.reverse()
    if result == []:
        result = "Not found!"
    elif len(result) != len(search_string):
        result = [result[i:i+len(search_string)] for
                  i in range(0, len(result), len(search_string))]
    return result
