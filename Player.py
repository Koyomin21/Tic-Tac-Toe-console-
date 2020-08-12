class Player:
    Id = 0
    def __init__(self,name,notation):
        Player.Id+=1
        self.Id = Player.Id+1 
        self.name = name
        self.notation = notation


    

    def get_move(self):
        """
        function takes input from Player,
        it also checks if the input is
        correct
        """
        while True:
            try:
                move = int(input())
                if 0 > move or move > 9:
                    raise InvalidInputError
                break
            except ValueError:
                print("Input Error!")
            except InvalidInputError:
                print("Input Error!")
            except ReservedFieldError:
                print("This field is already taken! Please try another")
        return move

    def __del__(self):
        """"
        destructor
        """
        Player.Id-=1
    


    
