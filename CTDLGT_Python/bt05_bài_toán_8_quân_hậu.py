# -*- coding: utf-8 -*-
"""BT05. Bài toán 8 quân hậu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ldthinh220802/cau_truc_du_lieu_va_giai_thuat/blob/main/BT05_B%C3%A0i_to%C3%A1n_8_qu%C3%A2n_h%E1%BA%ADu.ipynb
"""

class NQueens:
   
    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.show_full_board(positions)
            # self.show_short_board(positions)
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    
    NQueens(8)

if __name__ == "__main__":
    # execute only if run as a script
    main()