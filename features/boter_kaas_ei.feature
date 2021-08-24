
Feature: Tic-Tac-Toe

  The Tic-Tac-Toe game does the best move depending on the previous human
  move. Test these moves.

Background: 
Given we have an empty tic-tac-toe board

  Scenario: First move
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O
   Then the board has a O in column 1 and row 1 on the board

  Scenario: Computer wins
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 2 and row 3 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 1 and row 3 on the board
    And I ask the computer to do its best move for O 
   Then O is the winner of the game

   Scenario: It's a tie
   When I play X on column 1 and row 2 on the board
    And I ask the computer to do its best move for O
    And I play X on column 2 and row 1 on the board
    And I ask the computer to do its best move for O
    And I play X on column 3 and row 3 on the board
    And I ask the computer to do its best move for O
    And I play X on column 1 and row 3 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 3 and row 2 on the board
    Then its a tie!