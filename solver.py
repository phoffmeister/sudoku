import json

class Sudoku(object):
    board = []

    def is_valid(self):
        # check boad size
        if len(self.board) != 9:
            return false
        for r in self.board:
            if len(r) != 9:
                return false

        # check for doubles in rows
        for r in self.board:
            for n in range(1,10):
                if r.count(n) > 1:
                    return False

        # check for doubles in cols
        col = []
        for n in range(9):
            for r in self.board:
                col.append(r[n])
            for p in range(1,10):
                if col.count(p) > 1:
                    return False
            col = []

        # check boxes
        box = []
        for n in range(3):
            for o in range(3):
                for i in range(3):
                    for j in range(3):
                        box.append(self.board[i+n*3][j+o*3])
                for p in range(1,10):
                    if box.count(p) > 1:
                        return False
                box = []

        return True

    def read_json(self, filename):
        data = json.load(open(filename))
        self.board = data["puzzle"]

    def __str__(self):
        out = ""
        outer_count = 0
        for r in self.board:
            outer_count += 1
            count = 0
            for c in r:
                count += 1
                if c == 0:
                    out += "  "
                else:
                    out += "{} ".format(c)
                if count == 3 or count == 6:
                    out += "| "
            out += "\n"
            if outer_count == 3 or outer_count == 6:
                out += "----------------------\n"
        return out+"\n"

if __name__ == '__main__':
    a = Sudoku()
    print( "This is your input\n" )

    # read the puzzle file
    a.read_json('puzzles/puzzle1.json')

    # print the input board
    print( a )

    # check if the file is valid
    if a.is_valid():
        print("valid")
    else:
        print("invalid")
