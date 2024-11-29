python3 sudoku.py
def main():
  pygame.init()
  screen = pygame.display.set_mode((450,500))
  pygame.display.set_caption("Sudoku")
  clock = pygame.time.clock()

  board = Board(450,450,screen,difficulty = 'easy')
  running = True
    while running:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x,y = pygame.mouse.get_pos()
      if x < 450 and y < 450:
        row, col = y // 50, x // 50
        board.select(row,col)