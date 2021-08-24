from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move

def kolom(col):
    return col - 1 # Python col is Gherkin col minus 1
    
def rij(row):
    return row - 1 # Python row is Gherkin row minus 1

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD # clear the 3 x 3 tictactoe board
    context.winner = None

@when(u'I play X on column {k} and row {r} on the board')
def step_impl(context, k, r):
    context.board, context.winner = play(context.board,"X", kolom(int(k)), rij(int(r))) 


@when(u'I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, 'O')


@then(u'the board has a O in column 1 and row 1 on the board')
def step_impl(context):
    assert context.board[0] == "O"


@then(u'O is the winner of the game')
def step_impl(context):
    assert context.winner == "O"

@then(u'its a tie!')
def step_impl(context):
    assert context.winner != 'O' and "X" 