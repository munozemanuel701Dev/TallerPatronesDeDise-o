from factory import ChessPiceFactory

def main():
    piece1 = ChessPiceFactory.get_flyweight(name='Rook', color='Black')
    piece2 = ChessPiceFactory.get_flyweight(name='Rook', color='Black')
    
    print(piece1 is piece2)
    
    piece1.display("A8")
    piece1.display("H8")
    
if __name__ == "__main__":
    main()