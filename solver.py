import json

class Sudoku(object):
    board = []

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
    print( a )
    # check if the file is valid
