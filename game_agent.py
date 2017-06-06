"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
from numpy import subtract
from numpy.linalg import norm

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass




def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    

    opp = game.get_opponent(player)
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opp))
    n_moves =  float(own_moves - opp_moves)  
    
    opp_loc = game.get_player_location(opp)
    my_loc = game.get_player_location(player)
    # how far are the players from each other, the further the bigger number
    players_distance = float(norm(subtract(my_loc,opp_loc)))    
    
    center_loc = game.width / 2., game.height / 2.
    # how far are the players from the center of board
    # the closer the bigger value - substracted from constant 6 as max distance from center
    # TODO - the max distance could be rather calculated from board size - width, height
    center_distance = float(6 - norm(subtract(my_loc,center_loc)))        
    
    blank = float(len(game.get_blank_spaces()))
    space = float(game.width * game.height)
    # percengate of space left
    space_left = blank/space 
    
    # during the begining of the game  4 plies each try to stay at the center of the board
    if space_left > 92:
        return center_distance
    else: # consider advantage in number of moves and distance from oponent
        return n_moves + players_distance


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    opp = game.get_opponent(player)
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opp))
    n_moves =  float(own_moves - opp_moves)  
    
    opp_loc = game.get_player_location(opp)
    my_loc = game.get_player_location(player)
    # how far are the players from each other, the further the bigger number
    players_distance = float(norm(subtract(my_loc,opp_loc)))    
    
    center_loc = game.width / 2., game.height / 2.
    # how far are the players from the center of board
    # the closer the bigger value - substracted from constant 6 as max distance from center
    # TODO - the max distance could be rather calculated from board size - width, height
    center_distance = float(6 - norm(subtract(my_loc,center_loc)))        
    
    blank = float(len(game.get_blank_spaces()))
    space = float(game.width * game.height)
    # percengate of space left
    space_left = blank/space 
    # return the value that considers the advandage in number of moves 
    # the more space is left the more we should stay at center
    # plus the more game proceeds the further we want to be from opponent
    return n_moves + (space_left * center_distance) + ((1-space_left) * players_distance)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    opp = game.get_opponent(player)
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opp))
    n_moves =  float(own_moves - opp_moves)  
    
    opp_loc = game.get_player_location(opp)
    my_loc = game.get_player_location(player)
    # how far are the players from each other, the further the bigger number
    players_distance = float(norm(subtract(my_loc,opp_loc)))    
    
    center_loc = game.width / 2., game.height / 2.
    # how far are the players from the center of board
    # the closer the bigger value - substracted from constant 6 as max distance from center
    # TODO - the max distance could be rather calculated from board size - width, height
    center_distance = float(6 - norm(subtract(my_loc,center_loc)))        
    
    blank = float(len(game.get_blank_spaces()))
    space = float(game.width * game.height)
    # percengate of space left
    space_left = blank/space 
    # return the value that considers the stage of the game and distance from center 
    # the more space is left the more we should stay at center
    # plus the more game proceeds the further we want to be from opponent 
    # and we emphasize the number of moves advantage
    return (space_left * center_distance) + ((1-space_left) * (players_distance + n_moves ))

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        _, move = max([(self.__min_value(game.forecast_move(m), depth -1 ), m) for m in legal_moves])
        return move        

    
    def __min_value(self, game, depth):
       if self.time_left() < self.TIMER_THRESHOLD:
           raise SearchTimeout()

       legal_moves = game.get_legal_moves()      
       
       if depth == 0 or not legal_moves:
           return self.score(game, self)
       
       v =  min([(self.__max_value(game.forecast_move(m), depth - 1 )) for m in legal_moves])           
       
       return v

    def __max_value(self, game, depth):
       if self.time_left() < self.TIMER_THRESHOLD:
           raise SearchTimeout()
       
       legal_moves = game.get_legal_moves()

       if depth == 0 or not legal_moves:
           return self.score(game, self)

       v = max([(self.__min_value(game.forecast_move(m), depth - 1 )) for m in legal_moves])           
       return v
       
        

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        no_move = (-1, -1)
        best_move = no_move
        legal_moves = game.get_legal_moves()
        if legal_moves:
            # to return something pick the 1st poss move
            best_move = legal_moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            i = 0
            while True:
                i += 1
                move = self.alphabeta(game, i)
                if move != no_move:
                    best_move = move
        except SearchTimeout:
            return best_move

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        v, move = self.__max_value(game, depth , alpha, beta)
#        print ('alphabeta', v, move)
        return move        
    
    def __max_value(self, game, depth, alpha, beta):
       """
       function returning the max value and corespondng move
       """
       if self.time_left() < self.TIMER_THRESHOLD:
           raise SearchTimeout()
       
       legal_moves = game.get_legal_moves()
       if depth == 0 or not legal_moves:
           return self.score(game, self), (-1,-1)

       move = (-1,-1)
       v = float("-inf")
       for m in legal_moves:
           min_v = self.__min_value(game.forecast_move(m), depth - 1, alpha, beta)
           if (min_v > v) :
               v = min_v
               move = m
           if v >= beta:
               return v, move
           alpha = max (alpha, v)
       return v, move

    def __min_value(self, game, depth, alpha, beta):
       if self.time_left() < self.TIMER_THRESHOLD:
           raise SearchTimeout()
       
       legal_moves = game.get_legal_moves()
       if depth == 0 or not legal_moves:
           return self.score(game, self)
       
       v = float("inf")
       for m in legal_moves:
           max_v, max_m = self.__max_value(game.forecast_move(m), depth - 1, alpha, beta)
           v = min (v, max_v) 
           if v <= alpha:
               return v
           beta = min (beta, v)
       return v
   