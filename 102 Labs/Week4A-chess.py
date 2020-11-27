#Anastasia Horne
#​CSCI 102 – Section G
#Week 4 - Lab A - Missing Chess Pieces
#References: no one
#Time:  20 minutes

King_has= int(input('KINGS>'))
Queen_has= int(input('QUEENS>'))
Rook_has= int(input('ROOKS>'))
Bishop_has= int(input('BISHOPS>'))
Knight_has= int(input('KNIGHTS>'))
Pawn_has= int(input('PAWNS>'))

King= 1 - King_has
Queen= 1 - Queen_has
Rook= 2 - Rook_has
Bishop= 2 - Bishop_has
Knight= 2 - Knight_has
Pawn= 8 - Pawn_has

print('Emma, this is how many peices you have of each type(over or under):')
print(f'OUTPUT {King} {Queen} {Rook} {Bishop} {Knight} {Pawn}', end='')
