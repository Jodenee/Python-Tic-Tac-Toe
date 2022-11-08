import time 

class Player:
    def __init__(self, id, symbol) -> None:
        self.id = id
        self.symbol = symbol

class GridBox:
    def __init__(self, id) -> None:
        self.id: str = id
        self.box_owner: Player | None = None
        self.box_symbol: str = " "

class Grid:
    def __init__(self) -> None:
        self.grid: dict = {}
        for i in range(9): self.grid[f"Gridbox{i+1}"] = (GridBox(i+1))

    def get_gridbox(self, gridbox_number: int) -> GridBox:
        return self.grid[f"Gridbox{gridbox_number}"]

    def render_grid(self) -> None:
        print(f"""
        
        |{self.get_gridbox(1).box_symbol}|{self.get_gridbox(2).box_symbol}|{self.get_gridbox(3).box_symbol}|
        
        |{self.get_gridbox(4).box_symbol}|{self.get_gridbox(5).box_symbol}|{self.get_gridbox(6).box_symbol}|
        
        |{self.get_gridbox(7).box_symbol}|{self.get_gridbox(8).box_symbol}|{self.get_gridbox(9).box_symbol}|
        
        """)


class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1: Player = player1
        self.player2: Player = player2
        self.winner: Player | None = None
        self.current_turn: Player = player1
        self.grid: Grid = Grid()
        self.start_time: float = time.time()
        self.end_time: float = None

    def can_player_play(self, gridbox: GridBox) -> bool:
        if gridbox.box_owner == None: return True
        return False

    def play(self, player: Player, gridbox: GridBox) -> None:
        gridbox.box_owner = player
        gridbox.box_symbol = player.symbol

    def check_for_tie(self) -> bool:
        for gridbox in self.grid.grid.values():
            if gridbox.box_owner == None: return False
        
        self.end_time = time.time()
        return True

    def check_for_win(self, player: Player) -> bool:
        rows = {
            "row1": [self.grid.get_gridbox(1).box_symbol, self.grid.get_gridbox(2).box_symbol, self.grid.get_gridbox(3).box_symbol],
            "row2": [self.grid.get_gridbox(4).box_symbol, self.grid.get_gridbox(5).box_symbol, self.grid.get_gridbox(6).box_symbol], 
            "row3": [self.grid.get_gridbox(7).box_symbol, self.grid.get_gridbox(8).box_symbol, self.grid.get_gridbox(9).box_symbol]
        }

        # Check for horizontal win

        if rows["row1"] == [player.symbol,player.symbol,player.symbol]:
            self.end_time = time.time()
            self.winner = player
            return True
        elif rows["row2"] == [player.symbol,player.symbol,player.symbol]:
            self.end_time = time.time()
            self.winner = player
            return True
        elif rows["row3"] == [player.symbol,player.symbol,player.symbol]:
            self.end_time = time.time()
            self.winner = player
            return True

        # Check for vertical win

        if rows["row1"][0] == player.symbol and rows["row2"][0] == player.symbol and rows["row3"][0] == player.symbol:
            self.end_time = time.time()
            self.winner = player
            return True
        elif rows["row1"][1] == player.symbol and rows["row2"][1] == player.symbol and rows["row3"][1] == player.symbol:
            self.end_time = time.time()
            self.winner = player
            return True
        elif rows["row1"][2] == player.symbol and rows["row2"][2] == player.symbol and rows["row3"][2] == player.symbol:
            self.end_time = time.time()
            self.winner = player
            return True

        # Check for sideways win

        if rows["row1"][0] == player.symbol and rows["row2"][1] == player.symbol and rows["row3"][2] == player.symbol:
            self.end_time = time.time()
            self.winner = player
            return True
        elif rows["row1"][2] == player.symbol and rows["row2"][1] == player.symbol and rows["row3"][0] == player.symbol:
            self.end_time = time.time()
            self.winner = player
            return True

        return False

