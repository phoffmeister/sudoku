import json
import sys

class Sudoku(object):
    board = []

    def solve(self, max_iterations):
        posi = []
        for i in range(9):
            row = []
            for p in range(9):
                row.append([1,2,3,4,5,6,7,8,9])
            posi.append(row)

        iterations = 0
        while not self.solved():
            # update posi
            for r in range(9):
                for c in range(9):
                    if self.board[r][c] != 0:
                        # this position is already done
                        posi[r][c] = [self.board[r][c]]
                    else:
                        # check same row
                        for n in self.get_row(r):
                            if n in posi[r][c]:
                                posi[r][c].remove(n)
                        # check same col
                        for n in self.get_col(c):
                            if n in posi[r][c]:
                                posi[r][c].remove(n)
                        # check same box
                        for n in self.get_box(int(r/3), int(c/3)):
                            if n in posi[r][c]:
                                posi[r][c].remove(n)
            # if a posi has only one element put it in the board
            for r in range(9):
                for c in range(9):
                    if len(posi[r][c]) == 1:
                        self.board[r][c] = posi[r][c][0]
            iterations += 1
            if max_iterations != 0:
                if iterations >= max_iterations:
                    print("no solution found after {} iterations.".format(iterations))
                    return posi
        print("done after {} iterations".format(iterations))

    def solved(self):
        for r in self.board:
            for c in r:
                if c == 0 or c > 9:
                    return False
        return True

    def get_box(self, r, c):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[i+r*3][j+c*3])
        return box

    def get_row(self, r):
        return self.board[r]

    def get_col(self, c):
        col = []
        for r in self.board:
            col.append(r[c])
        return col

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
        try:
            data = json.load(open(filename))
            self.board = data["puzzle"]
        except:
            print("error reading file")
            exit(0)

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
    usage = "usage:\npython solver.py <json file> <max_iterations>\n"
    a = Sudoku()
    print( "This is your input\n" )
    if len(sys.argv) != 3:
        print(usage)
        exit(0)

    # read the puzzle file
    a.read_json(sys.argv[1])

    # print the input board
    print( a )

    # check if the file is valid
    if a.is_valid():
        print("your input is valid")
    else:
        print("your input is invalid")

    #solve it
    p = a.solve(int(sys.argv[2]))

    if a.is_valid():
        if a.solved():
            print(a)
        else:
            for r in p:
                print (r)
            print(a)
