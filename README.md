import random

import sys

import time
  

class soccerShootout
    
    player_team = 0
    
    virtual_player_team = 0
    
    player_shootout_blocks = 0
    
    player_shootout_goals = 0
    
    count_player = 0
    
    virtual_player_shootout_goals = 0
    
    virtual_player_shootout_blocks = 0
    
    count_virtual_player = 0
    
    event_count = 0
 
    def increaseEventCount() 
    
        soccerShootout.event_count += 1
    
    def increaseCountPlayer() 
    
        soccerShootout.count_player += 1
        
    def increasePlayerShootoutGoals() 
    
        soccerShootout.player_shootout_goals += 1
 
    def increasePlayerShootoutBlocks() 
    
        soccerShootout.player_shootout_blocks += 1
 
    def increaseCountVirutalPlayer() 
    
        soccerShootout.count_virtual_player += 1
        
    def increaseVirutalPlayerShootoutGoals() 
    
        soccerShootout.virtual_player_shootout_goals += 1
 
    def increaseVirtualPlayerShootoutBlocks() 
    
        soccerShootout.virtual_player_shootout_blocks += 1

def club_or_country()

    club_or_country = input(nDo you want to choose clubs or countries )
    
    if club_or_country == club or Club
    
        playerTeamRandomClub()
        
    elif club_or_country == Countries or countries
    
        playerTeamRandomCountry()
        
    else
        print(nInvalid input.)
        

def playerTeamRandomClub()

    player_team = [Rangers F.C., Inter Milan,D.C. United, Chelsea F.C.,
                    Portland Timbers, Real Salt Lake, FCB Bacelona]

    for name in random.sample(player_team, 1)
    
        player_team = name
        
        player_team = player_team.upper()

    soccerShootout.player_team = player_team
 
def virtualPlayerTeamRandomClub()

    virtual_player_team = [Sporting Kansas City, LA Galaxy,Arsenal F.C.,
                           Manchester United F.C., Liverpool F.C., Real Madrid]
 
    for name in random.sample(virtual_player_team, 1)
    
        virtual_player_team = name
        
        virtual_player_team = virtual_player_team.upper()
        
 
    soccerShootout.virtual_player_team = virtual_player_team

def playerTeamRandomCountry()
    player_team = [Poland, Croatia, England, Korea, Brazil, Russia, Italy, Swiss]


    for name in random.sample(player_team, 1)
    
        player_team = name
        
        player_team = player_team.upper()
    
    soccerShootout.player = player_team

def virtuealPlayerTeamRandomCountry()

    virtual_player_team = [Norway, France, Germany, Netherlands, Japan]
    for name in random.sample(virtual_player_team, 1)
    
        virtual_player_team = name
        
        virtual_player_team = virtual_player_team.upper()

    soccerShootout.virtual_player_team = virtual_player_team


def soccerEvent()

    soccerShootout.increaseEventCount()
  
    pt = soccerShootout.player_team
    
    vpt = soccerShootout.virtual_player_team
    
    ec = soccerShootout.event_count
    
    print(fEvent Soccer Shootout - {ec} )
    
    print(Location Los Angeles, California)
    
    print(fn{pt} vs. {vpt} )
    
    print(fYou will represent {pt} and the opponent is {vpt}.)
    
    print(Let the soccer shootout begin!)
    
def playerKicker()

    pt = soccerShootout.player_team
    
    print(fnYou will be representing {pt} in the shootout as a kicker.)
 
def playerGoalie()

    pt = soccerShootout.player_team
    
    print(fnYou will be representing {pt} in the shootout as a goalie.)
    
    print(goalie)
   
def playerShootoutKicks()

    soccerShootout.increaseCountPlayer()
    
    cp = soccerShootout.count_player
    
    pt = soccerShootout.player_team
    
    while (cp = 1 and cp = 5)
    
        time.sleep(1)
        
        print(fnSetting up for shootout kick {cp}. Where will you kick the ball )
        
        ball_kick = input(Please enter left, center, or right )
        
        ball_direction = ball_kick.upper()
        
        time.sleep(1)
        
        while (ball_direction != LEFT and ball_direction != CENTER and ball_direction != RIGHT)
        
            print(nInvalid input.)
            
            ball_kick = input(Please enter left, center, or right )
            
            ball_direction = ball_kick.upper()
            
        directions = [LEFT, CENTER, RIGHT]
        
        for i in random.sample(directions, 1)
        
            kicker_location = i
            
        if ball_direction == kicker_location
        
            soccerShootout.increasePlayerShootoutGoals()
            
            ipsg = soccerShootout.player_shootout_goals
            
            
            time.sleep(1)
            
            print(fnYou scored a goal at the {kicker_location} location.)
            
            print(f{pt} has scored {ipsg} goal(s).)
            
            playerShootoutKicks()
            
        else
        
            soccerShootout.increaseVirtualPlayerShootoutBlocks()
            
            time.sleep(1)
            
            print(fnThe goalie blocked the kick at the {kicker_location} location.)
            
            playerShootoutKicks()
            
    else
   
        playerGoalie()
        
        virtualPlayerShootoutKicks()
 
def virtualPlayerShootoutKicks()

    directions = [LEFT, CENTER, RIGHT]
    
    
    soccerShootout.increaseCountVirutalPlayer()
    
    cvp = soccerShootout.count_virtual_player
    
    vpt = soccerShootout.virtual_player_team
    
    while (cvp = 1 and cvp = 5)
    
        time.sleep(1)
        
        print(fnSetting up for shootout kick {cvp} for {vpt}. Where will you try to block the ball )
        
        ball_kick = input(Please enter left, center, or right )
        
        
        ball_direction = ball_kick.upper()
        
        time.sleep(1)
        
        while (ball_direction != LEFT and ball_direction != CENTER and ball_direction != RIGHT)
        
            print(nInvalid input.)
            
            ball_kick = input(Please enter left, center, or right )
            
            ball_direction = ball_kick.upper()
            
        for i in random.sample(directions, 1)
        
            kicker_location = i
            
        if ball_direction == kicker_location
        
            soccerShootout.increaseVirutalPlayerShootoutGoals()
            
            ivpsg = soccerShootout.virtual_player_shootout_goals
            
            time.sleep(1)
            
            print(fn{vpt} scored a goal at the {kicker_location} location.)
            
            print(f{vpt} has scored {ivpsg} goal(s).)
            
            virtualPlayerShootoutKicks()
            
        else
        
            pt = soccerShootout.player_team
            
            soccerShootout.increasePlayerShootoutBlocks()
            
            time.sleep(1)
            
            print(fn{pt} goalie blocked the kick at the {kicker_location} location.)
            
            virtualPlayerShootoutKicks()
            
    else
    
        shootoutScore()
 
def shootoutScore()

    vpt = soccerShootout.virtual_player_team
    
    pt = soccerShootout.player_team
    
    psg = soccerShootout.player_shootout_goals
    
    vpsg = soccerShootout.virtual_player_shootout_goals
    
    print(fn{pt} {psg} - {vpt} {vpsg} )
    
    if psg == vpsg
    
        print(fnThe shootout resulted in a tie.)
        
    elif psg  vpsg
    
        print(fn{pt} Wins!!!)
        
    elif psg  vpsg
    
        print(fn{vpt} Wins!!!)
        
    confirmPlay()

def confirmPlay()

    time.sleep(3)
    
    choice = int(input(nEnter 1 to keep playing or 2 to quit ))
    
    while choice  1 or choice  2
    
        choice = int(input(nInvalid Input, please enter 1 to keep playing or 2 to quit ))
        
    if choice == 1
    
        reset()
        
        
        playSoccerShooutoutAgain()
        
    else
    
        sys.exit()
        
 
def reset()

    soccerShootout.player_shootout_blocks = 0
    
    soccerShootout.player_shootout_goals = 0
    
    soccerShootout.count_player = 0
    
    soccerShootout.virtual_player_shootout_goals = 0
    
    soccerShootout.virtual_player_shootout_blocks = 0
    
    soccerShootout.count_virtual_player = 0
    
 
def playSoccerShooutoutAgain()

    playerTeamRandomClub()
    
    virtualPlayerTeamRandomClub()
    
    soccerEvent()
    
    playerKicker()
    
    playerShootoutKicks()
 
club_or_country()

playerTeamRandomClub()

playerTeamRandomCountry()

virtualPlayerTeamRandomClub()

virtuealPlayerTeamRandomCountry()

soccerEvent()

playerKicker()

playerShootoutKicks()
