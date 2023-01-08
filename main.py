import random

emptySign=' 0 '
assignedSign=' ■ '
attacked=' X '
checkList=[]
lastCoordinates=[None,None]
user='user'
comp='comp'

class Board:

    def __init__(self):
        self.bo={}
        self.X = 6
        self.Y = 6
        self.bo[user] = [[emptySign for i in range(self.X)] for y in range(self.Y)]
        self.bo[comp] = [[emptySign for i in range(self.X)] for y in range(self.Y)]


    def empty_board(self,user_type):
        self.bo[user_type] = [[emptySign for i in range(self.X)] for y in range(self.Y)]

    def create_new_board(self,user_type):
        print('=============================================')
        print(f' W E L C O M E  T O  S E A B A T T L E ! ! ! ')
        print('=============================================\r\n')
        print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ',end='')
        for i in range(self.X):
            print(f'         ', end='\r\n')
            print(f'   {i+1}  | ',end='')
            for y in range(self.Y):
                print(self.bo[user_type][i][y],end=' | ')
        print('')
        print(f'=============================================\r\n')
        create_new_board=self.bo[user_type]
        return self.bo[user_type]



    def print_board(self,bo,user_type):
        if (user_type==user):
            print('=============================================')
            print(f' W E L C O M E  T O  S E A B A T T L E ! ! ! ')
            print('=============================================\r\n')
            print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ',end='')
            for i in range(self.X):
                print(f'         ', end='\r\n')
                print(f'   {i+1}  | ',end='')
                for y in range(self.Y):
                    print(self.bo[user_type][i][y],end=' | ')
            print('')
            print(f'=============================================\r\n')
            return bo
        elif user_type==comp:
            print('=============================================')
            print(f' W E L C O M E  T O  S E A B A T T L E ! ! ! ')
            print('=============================================\r\n')
            print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ', end='')
            for i in range(self.X):
                print(f'         ', end='\r\n')
                print(f'   {i + 1}  | ', end='')
                for y in range(self.Y):
                    print(self.bo[user_type][i][y], end=' | ')
            print('')
            print(f'=============================================\r\n')
            return bo



class Ship:

    def __init__(self,b,user_type):
        self.current_state=b.bo[user_type]
        chX=0
        chY=0

    def board_reinitialization(self,b,user_type):
        b.empty_board(user_type)
        self.current_state = b.bo[user_type]
        chX = 0
        chY = 0

    def is_cell_empty(self,chY,chX):
            if self.current_state[chY][chX] == emptySign:
                return True
            else:
               return False
    def is_cells_between_one_and_six(self,chY,chX):
            if 6>=chX>0 and 6>=chY>0:
                return True
            else:
                return False
    def surround_cells_gaps_check(self, checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type):
        for val in checkList:
            #print(f'chY:{chY}:chX:{chX}:last{lastCoordinates[0]}:val0:{val[0]}:val1:{val[1]}:{lastCoordinates[0]==val}')

            if (nu_of_po==0):
                if (self.current_state[val[0]][val[1]] != emptySign and self.current_state[val[0]][val[1]] ==assignedSign ):
                    b.print_board(self.current_state,user_type)
                    print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координаты! ')
                    return False

            elif(nu_of_po==1):
                if (self.current_state[val[0]][val[1]] != emptySign and self.current_state[val[0]][val[1]] ==assignedSign ):
                    if  lastCoordinates[0] != val:
                        b.print_board(self.current_state, user_type)
                        print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координаты! ')
                        return False

            elif(nu_of_po==2):
                if (self.current_state[val[0]][val[1]] != emptySign and self.current_state[val[0]][val[1]] ==assignedSign ):
                    if lastCoordinates[0] != val:
                        b.print_board(self.current_state, user_type)
                        print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координаты! ')
                        return False

        return True
    def double_check(self, checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type):
        #print (self.surround_cells_gaps_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type) and self.ships_part_check(checkList, chY, chX,lastCoordinates, number_of_points,nu_of_po, user_type))
        return (self.surround_cells_gaps_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type) and  self.ships_part_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type))
    def ships_part_check(self, checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type):
        if nu_of_po==0: return True
        for val in checkList:
            if (nu_of_po == 1):
                if (self.current_state[val[0]][val[1]] == assignedSign):
                    for lastList in lastCoordinates:
                        if (lastList == val):
                            return True
            elif (nu_of_po == 2):
                if (self.current_state[val[0]][val[1]] == assignedSign):
                    for lastList in lastCoordinates:
                        if (lastList == val):
                            return True


        b.print_board(self.current_state, user_type)
        print('Координаты каждой из частей одного коробля должны находится рядом (в одной из соседних ячеек)! Введите правильные координаты')
        return False






    def is_that_cell_is_allowed_to_allocate(self,chY,chX,number_of_points,nu_of_po,user_type):


           if 0<chY<5:

                if 0<chX<5:

                    checkList.clear()
                    checkList.append([chY - 1,chX])       #1
                    checkList.append([chY - 1, chX + 1])  #2
                    checkList.append([chY,chX + 1])       #3
                    checkList.append([chY + 1, chX + 1])  #4
                    checkList.append([chY + 1, chX])      #5
                    checkList.append([chY + 1, chX - 1])  #6
                    checkList.append([chY, chX - 1])      #7
                    checkList.append([chY - 1, chX - 1])  #8
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type)

                elif chX==5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type)

                elif chX==0:

                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5

                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type)

           elif chY==5:

               if 0 < chX < 5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po, user_type)
               elif chX == 5:
                    checkList.clear()
                    checkList.append([chY - 1, chX])      # 1
                    checkList.append([chY, chX - 1])      # 7
                    checkList.append([chY - 1, chX - 1])  # 8
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type)
               elif chX == 0:
                    checkList.clear()
                    checkList.append([chY - 1, chX])  # 1
                    checkList.append([chY - 1, chX + 1])  # 2
                    checkList.append([chY, chX + 1])  # 3
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type)

           elif chY==0:

               if 0 < chX < 5:
                    checkList.clear()
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type)
               elif chX == 5:
                    checkList.clear()
                    checkList.append([chY + 1, chX])      # 5
                    checkList.append([chY + 1, chX - 1])  # 6
                    checkList.append([chY, chX - 1])      # 7
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type)
               elif chX == 0:
                    checkList.clear()
                    checkList.append([chY, chX + 1])      # 3
                    checkList.append([chY + 1, chX + 1])  # 4
                    checkList.append([chY + 1, chX])      # 5
                    return self.double_check(checkList, chY, chX, lastCoordinates, number_of_points, nu_of_po,user_type)





    def check_coordinates(self,number_of_points,number_of_ships,ship_type,user_type):
        nu_of_po=0
        nu_of_sh=0
        attempts_count=0
        chY=random.randint(1,6-number_of_points)

        try:
            while nu_of_sh < number_of_ships:
                while nu_of_po <number_of_points:
                    if user_type=='user':
                        chX = int(input(f'Пожалуйста введите координату {nu_of_po+1} {ship_type} корабля №{nu_of_sh+1} ({number_of_points} клетки) X=: '))
                        chY = int(input(f'Пожалуйста введите координаты {nu_of_po+1} {ship_type} корабля №{nu_of_sh+1} ({number_of_points} клетки) Y=: '))
                    else:
                        attempts_count+=1






                    if self.is_cells_between_one_and_six(chY,chX):
                        chX -= 1
                        chY -= 1

                        if self.is_cell_empty(chY,chX):

                            if self.is_that_cell_is_allowed_to_allocate(chY,chX,number_of_points, nu_of_po,user_type):
                                lastCoordinates.clear()
                                lastCoordinates.append([chY,chX])
                                self.current_state[chY][chX]=' ■ '
                                b.print_board(self.current_state,user_type)
                            else:
                                nu_of_po -= 1

                        else:
                            b.print_board(self.current_state,user_type)
                            print(f'Данная координата уже занята!')
                            nu_of_po -= 1
                    else:
                       b.print_board(self.current_state,user_type)
                       print(f'Неправильно введены координаты. Пожалуйста введите числа от 1 до 6!')
                       nu_of_po-=1

                    nu_of_po += 1
                nu_of_sh+=1
                nu_of_po=0

        except ValueError:
            self.board_reinitialization(b,user_type)
            b.print_board(self.current_state,user_type)
            print('Пожалуйста вводите заново все координаты. Разрешены только цифры от 1 до 6!')
            self.initiate_user_ships(user_type)



    def initiate_user_ships(self,user_type):
        self.check_coordinates(3,1,'большого',user_type)
        self.check_coordinates(2, 2, 'среднего',user_type)
        self.check_coordinates(1, 4,'малого',user_type)
        print('[Установка координат для кораблей игрока завершена!!!]')





b=Board()
b.create_new_board(user)




c=Ship(b,comp)
c.initiate_user_ships(comp)

print('xxxx=========================================================================================')
u=Ship(b,user)
u.initiate_user_ships(user)














