import copy
import random

emptySign=' 0 '
assignedSign=' ■ '
exploded=' X '
missed=' T '
checkList=[]
user_names={'user':' [ Игрок ] ','comp':' [ Компьютер ] '}
lastCoordinates=[None,None]
user='user'
comp='comp'
hid=False


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
            print('==============Карта пользователя=============')
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
        elif user_type==comp and hid==False:
            print('=============================================')
            print('===============Карта Компьютера==============')
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
    def print_mearged_board (self, user_set,comp_set):
                print('', end='\r\n')
                print('=============================================      ',end='')
                print('=============================================')
                print('==============Карта пользователя=============      ',end='')
                print('===============Карта компьютера==============')
                print(f'                        W E L C O M E  T O  S E A B A T T L E ! ! !                             ')
                print('=============================================      ',end='')
                print('=============================================\r\n')
                print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  |       ', end='')
                print('   y\X|  1  |  2  |  3  |  4  |  5  |  6  | ')
                for i in range(self.X):

                    print(f'         ', end='\r\n')
                    print(f'   {i + 1}  | ', end='')

                    for y in range(self.Y):
                        print(user_set[i][y], end=' | ')
                    print(f'      ', end='')

                    print(f'   {i + 1}  | ', end='')
                    for y in range(self.Y):
                        print(comp_set[i][y], end=' | ')

                print('',end='\r\n')
                print(f'  ================================================',end='')
                print(f'=============================================\r\n')






class Ship:

    def __init__(self,b,user_type):
        self.current_state=b.bo[user_type]
        self.GameActive={}
        self.GameActive[user_type]= True
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
                    if user_type != 'comp':
                        print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координаты! ')
                    return False

            elif(nu_of_po==1):
                if (self.current_state[val[0]][val[1]] != emptySign and self.current_state[val[0]][val[1]] ==assignedSign ):
                    if  lastCoordinates[0] != val:
                        b.print_board(self.current_state, user_type)
                        if user_type != 'comp':
                            print('Корабли должны находится на расстоянии минимум одна клетка друг от друга. Введите новые координаты! ')
                        return False

            elif(nu_of_po==2):
                if (self.current_state[val[0]][val[1]] != emptySign and self.current_state[val[0]][val[1]] ==assignedSign ):
                    if lastCoordinates[0] != val:
                        b.print_board(self.current_state, user_type)
                        if user_type != 'comp':
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
        if user_type != 'comp':
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


    def generate_random_coordinates(self,number_of_points,nu_of_po,chY,chX,number_of_ships,nu_of_sh):
        X=0
        Y=0
        if number_of_points==3:
            if nu_of_po==0:
                X=1
                Y=random.randint(1,6)
            elif nu_of_po==1:
                X=2
                Y=chY+1
            elif nu_of_po==2:
                X=3
                Y=chY+1

        if (number_of_ships==2):
                if number_of_points==2:
                    if nu_of_po==0:
                        X=2+nu_of_sh
                        Y=random.randint(1,6)
                    elif nu_of_po==1:
                        X=3+nu_of_sh
                        Y=chY+1

        if (number_of_ships==4):
                if number_of_points==1:

                        X=random.randint(1,6)
                        Y=random.randint(1,6)






        return Y, X










    def check_coordinates(self,number_of_points,number_of_ships,ship_type,user_type):
        nu_of_po=0
        nu_of_sh=0
        chX=0
        chY=0
        con=0
        conCycleCount=0

        try:

                while nu_of_sh < number_of_ships and self.GameActive[user_type]:
                    while nu_of_po <number_of_points and self.GameActive[user_type]:
                        #print(self.GameActive)
                        if user_type=='user':

                            chX = int(input(f'Уважаемый {user_names[user_type]}! Пожалуйста введите координату {nu_of_po+1} для {ship_type} корабля №{nu_of_sh+1} состоящего из {number_of_points} координат X=: '))
                            chY = int(input(f'Уважаемый {user_names[user_type]}! Пожалуйста введите координату {nu_of_po+1} для {ship_type} корабля №{nu_of_sh+1} состоящего из {number_of_points} координат Y=: '))
                        else:
                            con+=1
                            #print(f'con:{con}:concycle:{conCycleCount}')
                            if con<=15:

                                if(conCycleCount<15):
                                    chY,chX=self.generate_random_coordinates(number_of_points,nu_of_po,chY,chX,number_of_ships,nu_of_sh)
                                else:
                                    conCycleCount=0
                                    self.board_reinitialization(b, user_type)

                                    self.initiate_user_ships(user_type)

                            else:
                                con=0
                                conCycleCount += 1


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
                                if user_type!='comp':
                                    print(f'Данная координата уже занята!')
                                nu_of_po -= 1
                        else:
                           b.print_board(self.current_state,user_type)
                           if user_type != 'comp':
                                print(f'Неправильно введены координаты. Пожалуйста введите числа от 1 до 6!_')
                           nu_of_po-=1

                        nu_of_po += 1
                    nu_of_sh+=1
                    nu_of_po=0

        except ValueError:
            self.board_reinitialization(b,user_type)
            b.print_board(self.current_state,user_type)
            if user_type != 'comp':
                print('Пожалуйста вводите заново все координаты. Разрешены только цифры от 1 до 6!__')
                self.initiate_user_ships(user_type)






    def initiate_user_ships(self,user_type):
        self.GameActive[user_type] = True
        self.check_coordinates(3,1,'большого',user_type)
        self.check_coordinates(2, 2, 'среднего',user_type)
        self.check_coordinates(1, 4,'малого',user_type)
        print(f'[Установка координат для кораблей {user_names[user_type]} завершена!!!]')
        self.GameActive[user_type]=False




class StartGame():
    def __init__(self,user_set,comp_set):
        self.user_set=user_set
        self.comp_set=comp_set

        self.masked_comp_set=self.commuflage(copy.deepcopy(self.comp_set))

        self.gameController()
        #b.print_mearged_board(self.user_set,self.masked_comp_set)

    def gameController(self):

        self.attack_comp_positions()
    def commuflage(self,inp_set):
        self.tmp_set=inp_set
        for i in range(6):
            for y in range(6):
                if self.tmp_set[y][i]==assignedSign:self.tmp_set[y][i]=emptySign
        return self.tmp_set


    def is_cells_between_one_and_six(self, chY, chX):
        if 5 >= chX >= 0 and 5 >= chY >= 0:
            return True
        else:
            return False
    @property
    def check_user_positions(self):
        if assignedSign in str(self.user_set):
            return True
        else:
            print('')
            print('[-----------------------------------------Внимание-------------------------------------------]')
            print('[-------------------------------------Победил Компьютер!!!-----------------------------------]')
            print('[--------------------------------------------!!!---------------------------------------------]')
            exit(0)
            return False
    @property
    def check_comp_positions(self):
        if assignedSign in str(self.comp_set):
            return True
        else:
            print('')
            print('[-------------------------------------------Внимание------------------------------------------]')
            print('[---------------------------------------- Вы победили!!! -------------------------------------]')
            print('[---------------------------------------------!!!---------------------------------------------]')
            exit(0)
            return False
    def attack_comp_positions(self):
            while(self.check_comp_positions):
                try:
                    chX = int(input(f'Пожалуйста введите координату X для атаки=: '))-1
                    chY = int(input(f'Пожалуйста введите координату Y для атаки=: '))-1

                    if self.is_cells_between_one_and_six( chY, chX):
                        if self.comp_set[chY][chX]==assignedSign:
                            self.comp_set[chY][chX]=exploded
                            self.masked_comp_set[chY][chX] = exploded
                            b.print_mearged_board(self.user_set,self.masked_comp_set)
                            print('Вы подбили корабль или часть корабля Компьютера!!! Выш ход!!!')
                        elif self.comp_set[chY][chX]==emptySign:
                             self.comp_set[chY][chX]=missed
                             self.masked_comp_set[chY][chX] = missed
                             self.attack_user_positions()
                             break
                        elif self.masked_comp_set[chY][chX]==exploded:
                            print("Вы уже делали данный ход! Попробуйте другие координаты!")
                            continue
                        elif self.masked_comp_set[chY][chX]==missed:
                            print("Вы уже делали данный ход! Попробуйте другие координаты!")
                            continue
                    else: print(f'Неправильно введены координаты. Пожалуйста введите числа от 1 до 6!')
                except ValueError:
                    print('Пожалуйста вводите заново все координаты. Разрешены только цифры от 1 до 6!')
            return False




        #emptySign = ' 0 '
        #assignedSign = ' ■ '
        #exploded = ' X '
        #missed = ' T '

    def attack_user_positions(self):
        while (self.check_user_positions):
            chX = random.randint(1,6)-1
            chY = random.randint(1,6)-1
            print('ГЕНЕРАЦИЯ КООРДИНАТ ДЛЯ АТАКИ')
            if self.user_set[chY][chX] == assignedSign:
                self.user_set[chY][chX] = exploded
                b.print_mearged_board(self.user_set, self.masked_comp_set)
                print('Компьютер подбил Ваш корабль или часть вашего корабля!!!')
            elif self.user_set[chY][chX] == emptySign:
                self.user_set[chY][chX] = missed
                b.print_mearged_board(self.user_set,self.masked_comp_set)
                print(f'Вы Промазали. Ход Компьютера!!!')
                print(f'Компьютера: X={chX+1}, Y={chY+1}. Компьютер промазал. Теперь Ваш ход(смотрите карту выше)!!!')
                self.attack_comp_positions()

            elif self.user_set[chY][chX] == exploded:
                continue
            elif self.user_set[chY][chX] == missed:
                continue
            b.print_mearged_board(self.user_set,self.masked_comp_set)
        return False


b=Board()
b.create_new_board(user)

hid=True

c=Ship(b,comp)
c.initiate_user_ships(comp)

u=Ship(b,user)
u.initiate_user_ships(user)


xgame=StartGame(u.current_state,c.current_state)




















