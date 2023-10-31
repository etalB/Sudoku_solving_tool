import streamlit as st
import pandas as pd
import numpy as np

def board_show():
  st.dataframe(sudoku_board)

def is_number_Valid(board, vtc, hrz, n):
  verticalValid = all([n != board[vtc][x] for x in range(9)])
  if verticalValid:
    horizontalValid = all([n != board[x][hrz] for x in range(9)])
    if horizontalValid:
      tripleX, tripleY = 3 * (vtc // 3), 3 * (hrz // 3)
      for x in range(tripleX, tripleX + 3):
        for y in range(tripleY, tripleY + 3):
          if board[x][y] == n:
            return False
      return True
  return False

def nexttofill(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        return i, j
  return -1, -1

# 스도쿠 풀이 함수

def Solve_Sudoku(board, vtc=0, hrz=0):
  global tries
  vtc, hrz = nexttofill(board)
  if vtc == -1:
    return True
  for n in range(1,10):
    if is_number_Valid(board, vtc, hrz, n):
      board[vtc][hrz] = n
      if Solve_Sudoku(board, vtc, hrz):
        return True
  board[vtc][hrz] = 0
  tries += 1
  return False


sudoku_board = ([0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0])
tries = 0
def main():
    st.title('스도쿠 풀이 사이트')
    
    global sudoku_board
    
    sudoku_nums1 = st.number_input('첫번째 줄', 0, 999999999)
    sudoku_nums2 = st.number_input('두번째 줄', 0, 999999999)
    sudoku_nums3 = st.number_input('세번째 줄', 0, 999999999)
    sudoku_nums4 = st.number_input('네번째 줄', 0, 999999999)
    sudoku_nums5 = st.number_input('다섯번째 줄', 0, 999999999)
    sudoku_nums6 = st.number_input('여섯번째 줄', 0, 999999999)
    sudoku_nums7 = st.number_input('일곱번째 줄', 0, 999999999)
    sudoku_nums8 = st.number_input('여덟번째 줄', 0, 999999999)
    sudoku_nums9 = st.number_input('아홉번째 줄', 0, 999999999)
    
    if st.button('스도쿠 풀이 시작하기'):
      sudoku_nums = [sudoku_nums1, sudoku_nums2, sudoku_nums3, sudoku_nums4, sudoku_nums5, sudoku_nums6, sudoku_nums7, sudoku_nums8, sudoku_nums9]
      
      
      
      for vtc in range(9):
        for hrz in range(len(str(sudoku_nums[vtc]))):
          sudoku_board[vtc][8-hrz] = int(str(sudoku_nums[vtc])[len(str(sudoku_nums[vtc]))-hrz-1])

      Solve_Sudoku(sudoku_board)
      board_show()
      st.write("뒤로 돌아간 횟수 :",str(tries))


if __name__ == '__main__' :
    main()