from models.players.random_player import RandomPlayer
from models.players.corner_player import CornerPlayer
from views.console_board_view import ConsoleBoardView
from models.board import Board

class BoardController:
  def __init__(self):
    self.board = Board(None)
    self.view  = ConsoleBoardView(self.board)

  def init_game(self):
    self.white_player = CornerPlayer(Board.WHITE)
    self.black_player = RandomPlayer(Board.BLACK)
    self.atual_player = self.black_player

    finish_game = 0

    self.view.update_view()

    while finish_game != 2:
      raw_input("")
      atual_color = self.atual_player.color
      print 'Jogador: ' + atual_color
      if self.board.valid_moves(atual_color).__len__() > 0:
        self.board.play(self.atual_player.play(self.board.get_clone()), atual_color)
        self.view.update_view()
        finish_game = 0
      else:
        print 'Sem movimentos para o jogador: ' + atual_color
        finish_game += 1
      self.atual_player = self._opponent(self.atual_player)

    self._end_game()


  def _end_game(self):
    score = self.board.score()
    if score[0] > score[1]:
      print ""
      print 'Jogador ' + self.white_player.__class__.__name__ + ' Ganhou'
    elif score[0] < score[1]:
      print ""
      print 'Jogador ' + self.black_player.__class__.__name__ + ' Ganhou'
    else:
      print ""
      print 'Jogo terminou empatado'

  def _opponent(self, player):
    if player.color == Board.WHITE:
      return self.black_player

    return self.white_player
