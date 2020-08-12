import random


class Bot:
    def __init__(self,notation,level):
        self.notation = notation
        self.level = level
        self.name = "Bot"
    
    def make_move(self,board):
        """
        function makes move depending on bot's
        level of difficulty
        param board: game board to make move
        return tuple with indexes(row,element)
        """
        while True:
            if self.level == 'easy':
                move = random.randint(0,8)
                for row in board:
                    if move in row:
                        row_index = board.index(row)
                        field_index = row.index(move)
                        return row_index,field_index
                
            elif self.level == 'medium':
                move = self.seek_win(board,1)
                if not move:
                    move = self.seek_win(board,0)
                else:
                    return move
                if not move:
                    move = random.randint(0,8)
                    print('Move: {}'.format(move))
                    for row in board:
                        if move in row:
                            row_index = board.index(row)
                            field_index = row.index(move)
                            return row_index,field_index
                else:
                    return move

                    
            elif self.level == 'hard':
                move = self.seek_win(board,1)
                if not move:
                    move = self.seek_win(board,0)
                else:
                    return move
                if not move:
                    corners = [1,3,7,9]
                    if corners:
                        move = random.choice(corners)
                        corners.remove(move)
                    else:
                        move = random.randint(0,8)
                    
                    for row in board:
                        if move in row:
                            row_index = board.index(row)
                            field_index = row.index(move)
                            return row_index,field_index

                else:
                    return move
            

            
    def is_available(self,field,board):
        """
        param field: certain value('X','O', or number(1-9))
        returns True if the given field exists
        returns False if there's no field with given value
        """
        for row in board:
            if field in row:
                return True
        return False
    
    def seek_win(self,board,ind):
        """
        param board: game board
        param ind: index of notation
        returns False if there's no way to win
        return tuple with row index and field 
        index, indicating on spot
        """
        notations=['X','O']
        #check rows
        for row in board:
            if row.count(notations[ind]) == 2:
                for field in row:
                    if field not in notations and self.is_available(field,board):
                        row_index = board.index(row)
                        field_index = row.index(field)
                        print('Rows: ',row_index,field_index)

                        return row_index,field_index
        
        #check columns
        column = []
        for i in range(3):
            column.clear()
            for j in board:
                column.append(j[i])
            if column.count(notations[ind])==2:
                for field in column:
                    if field not in notations and self.is_available(field,board):
                        row_index = column.index(field)
                        field_index = i
                        
                        return row_index,field_index
            else:
                column.clear()
        #check diagonal
        diagonal = [j[i] for i,j in enumerate(board)]
        if diagonal.count(notations[ind])==2:
            for field in diagonal:
                if field not in notations and self.is_available(field,board):
                    field_index = diagonal.index(field)
                    return field_index,field_index
        #check second diagonal
        diagonal = [j[i] for i,j in enumerate(reversed(board))]
        diagonal = list(reversed(diagonal)) # reversed to set the indexes right
        if diagonal.count(notations[ind])==2:
            for field in diagonal:
                if field not in notations and self.is_available(field,board):
                    
                    row_index = diagonal.index(field)
                    field_index = board[row_index].index(field)
                    return row_index,field_index
        
        
        return False
