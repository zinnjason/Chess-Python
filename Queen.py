class Queen(Piece):
    def __init_subclass__(cls):
        return super().__init_subclass__()