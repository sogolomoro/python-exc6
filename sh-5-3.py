class Soldier:


    soldierids = []


    
    def __init__(self, stype, sid, x, y):
        self.sid = sid

        self.stype = stype
        
        self.health = 100


        self.y = y
        self.x = x
        

        Soldier.soldierids.append (self.sid)





class Archer (Soldier):

    
    def __init__ (self, sid, x, y):

        super().__init__("archer", sid, x, y)




class Melee(Soldier):
    
    def __init__(self, sid, x, y):

        super().__init__("melee", sid, x, y)


class Game:

    
    def __init__(self,n):
    
        self.positions = {0:{},1:{}}
        
        self.players = {0: [], 1: []}
        
        self.n=n
        self.turn = 0
        
    
    def invswturn(self):
        self.turn = 1 - self.turn  

    
    def crsol(self, stype, sid, x, y):
        pid = [i.sid for i in self.players[self.turn]]
        
        if sid in pid:
            
            print ("duplicate tag")
            return

        
        if (x, y) not in self.positions[self.turn]:
            self.positions[self.turn][(x, y)] = []

        
        if stype == "archer":
            sol = Archer(sid, x, y)

        
        elif stype == "melee":
            sol = Melee(sid, x, y)
        
        else: 
        
            
            print ("Invalid soldier type")
            return


        self.positions[self.turn][(x, y)].append(sol)
        self.players[self.turn].append(sol)
        self.invswturn()



    
    def moves(self, sid, direction):
        sol = self.finds(sid)

        
        if sol is not None:

            oldp = (sol.x, sol.y)

            
            if direction == "up":
                new_x, new_y = sol.x, sol.y-1

            
            elif direction == "down":
                new_x, new_y = sol.x, sol.y+1
            
            
            elif direction == "left":
                new_x, new_y = sol.x-1, sol.y
            
            
            elif direction == "right":
                new_x, new_y = sol.x+1, sol.y 
            
            else:
                
                print ("Invalid direction")
                return



            
            if not  (0 <= new_x < self.n and 0 <= new_y < self.n):
             
                
                print ("out of bounds")
                return

            
            self.positions[self.turn][oldp].remove(sol)

            
            if (new_x, new_y) not in self.positions[self.turn]:
                self.positions[self.turn][(new_x, new_y)] = []
            

            self.positions[self.turn][(new_x, new_y)].append(sol)


            sol.y = new_y
            sol.x = new_x
            

            
            self.invswturn()
            return

        else:
            
            print (f"soldier does not exist")
            return
        
    
    
    def attack(self, attacker_id, target_id):

        attacker = self.sforattack(attacker_id,"atacker")
        target = self.sforattack(target_id,"defender")


        
        if attacker is None or target is None:
            return

        
        if isinstance(attacker, Archer):

            
            if self.distance(attacker.x, attacker.y, target.x, target.y) > 2:
                 
                 print ("the target is too far")
                 return

            target.health -= 10

        
        elif isinstance(attacker, Melee):

            
            if self.distance(attacker.x, attacker.y, target.x, target.y) > 1:
                 
                 print ("the target is too far")
                 return

            target.health -= 20
     

        
        if target.health <= 0:
            
            print ("target eliminated")
            target_position = (target.x, target.y)

            
            if target_position in self.positions[1 - self.turn]:

                
                if target in self.positions[1 - self.turn][target_position]:
                    self.positions[1 - self.turn][target_position].remove(target)

            
            if target in self.players[1 - self.turn]:
                self.players[1 - self.turn].remove(target)

        self.invswturn()
        return

    
    def getinfo(self, sid):
        sol = self.finds(sid)

        
        if sol is None:
            
            print (f"soldier does not exist")
            return

        
        print (f"health:  {sol.health}")
        
        print (f"location:  {sol.x}   {sol.y}") 
        self.invswturn()
        return


    
    def pinlead(self):
        score = {0: 0, 1: 0}
        for player, soldiers in self.players.items():
            for sol in soldiers:
                score[player] += sol.health

        
        if score[0] > score[1]:
            
            print ("player  1")
        
        elif score[0] < score[1]:
            
            print ("player  2")
        else:
            
            print ("draw")

    

    def finds(self, sid):
        for soldiers_list in self.positions[self.turn].values():
            for sol in soldiers_list:
                
                if sol.sid == sid:
                    return sol
    
    
    def sforattack(self, sid,whois):
        
        if whois=="atacker":
            for soldiers_list in self.positions[self.turn].values():
                for sol in soldiers_list:
                    
                    if sol.sid == sid:
                        return sol
        else:
            for soldiers_list in self.positions[1-self.turn].values():
                for sol in soldiers_list:
                    
                    if sol.sid == sid:
                        return sol
        
        print (f"soldier does not exist")
        return None


    
    def distance(self, x1, y1, x2, y2):
        
        return abs(x1 - x2) + abs(y1 - y2)

commands=[]

n = int(input())

game = Game(n)



while True:
            
            try:
                line = input().split(" ")
                
                if 'end' in line :
                    break
                commands.append(line)
            
            except EOFError:
                break


poin=0

while True:
    
    if poin==len(commands):
        break
    command = commands[poin]
    
    if command[0] == "new":
        game.crsol(command[1], int(command[2]), int(command[3]), int(command[4]))
    
    elif command[0] == "move":
        game.moves(int(command[1]), command[2])
    
    elif command[0] == "attack":
        game.attack(int(command[1]), int(command[2]))
    
    elif command[0] == "info":
        game.getinfo(int(command[1]))
    
    elif command[0] == "who":
        game.pinlead()
    poin+=1