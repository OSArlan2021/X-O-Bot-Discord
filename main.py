#By _Arlan-Programmist™_#7777

вносить  разлад
от  разлада . команды импорта ext  
бот  =  команды . Бот ( command_prefix = "." )
@ бот . событие
async  def  on_ready ():
    print ( «Бот онлайн» )

@ бот . событие
async  def  on_command_error ( ошибка ):
    если  isinstance ( ошибка , команды . CommandNotFound ):
        ждите  ctx . send ( "Ошибка: Команда Не Найдена" )
    если  isinstance ( ошибка , команды . MissingRequiredArgument ):
        ждите  ctx . send ( 'Ошибка: Не Правильно Написали' )
    если  isinstance ( ошибка , команды . MissingPermissions ):
        ждите  ctx . send ( "Ошибка: Вы не Аданы управления" )

game_map  = [ ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square:" , ": white_large_square: , ": white_large_square:" ]
@ бот . команда ()
async  def  place ( ctx , control ):
    если  control  ==  "1r" :
        game_map [ 0 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "1b" :
        game_map [ 0 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "2r" :
        game_map [ 1 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "2b" :
        game_map [ 1 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "3r" :
        game_map [ 2 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "3b" :
        game_map [ 2 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "4r" :
        game_map [ 3 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "4b" :
        game_map [ 3 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "5r" :
        game_map [ 4 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "5b" :
        game_map [ 4 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "6r" :
        game_map [ 5 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "6b" :
        game_map [ 5 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "7r" :
        game_map [ 6 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "7b" :
        game_map [ 6 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "8r" :
        game_map [ 7 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "8b" :
        game_map [ 7 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "9r" :
        game_map [ 8 ] =  ": o2:"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")
    если  control  ==  "9b" :
        game_map [ 8 ] =  ": Regional_indicator_x :"
        ждите  ctx . send ( f " { ( game_map [ 0 ]) } { ( game_map [ 1 ]) } { ( game_map [ 2 ]) } \ n { ( game_map [ 3 ]) } { ( game_map [ 4 ]) } { ( game_map [ 5 ]) } \ n { ( game_map [ 6 ])} { ( game_map [ 7 ]) } { ( game_map [ 8 ]) } ")

@ бот . команда ()
async  def  перезапуск ( ctx ):
    game_map [ 0 ] =  ": white_large_square:"
    game_map [ 1 ] =  ": white_large_square:"
    game_map [ 2 ] =  ": white_large_square:"
    game_map [ 3 ] =  ": white_large_square:"
    game_map [ 4 ] =  ": white_large_square:"
    game_map [ 5 ] =  ": white_large_square:"
    game_map [ 6 ] =  ": white_large_square:"
    game_map [ 7 ] =  ": white_large_square:"
    game_map [ 8 ] =  ": white_large_square:"

бот . запустить ( "Token Bot")
