import random

import sys

import time


# Class

class PeanaltyShootout:

    player_team = ""

    Opponent_player_team = ""

    player_shootout_blocks = 0

    player_shootout_goals = 0

    count_player = 0

    Opponent_player_shootout_goals = 0

    Opponent_player_shootout_blocks = 0

    count_Opponent_player = 0

    event_count = 0
 
    def increaseEventCount(): 

        PeanaltyShootout.event_count += 1
    
    def increaseCountPlayer(): 

        PeanaltyShootout.count_player += 1
        
    def increasePlayerShootoutGoals(): 

        PeanaltyShootout.player_shootout_goals += 1
 
    def increasePlayerShootoutBlocks(): 

        PeanaltyShootout.player_shootout_blocks += 1
 
    def increaseCountVirutalPlayer(): 
        PeanaltyShootout.count_Opponent_player += 1
        
    def increaseVirutalPlayerShootoutGoals(): 

        PeanaltyShootout.Opponent_player_shootout_goals += 1
 
    def increaseOpponentPlayerShootoutBlocks(): 

        PeanaltyShootout.Opponent_player_shootout_blocks += 1

# Timer or Countdown(Not Working)

# def countdown(t):

#     while t:

#         mins, secs = divmod(t, 60)

#         timer = '{:02d}:{:02d}'.format(mins, secs)

#         print(timer, end="\r")

#         time.sleep(1)

#         t -= 1

#     print('Fire in the hole!!')

# input time in seconds

# t = input("Enter the time in seconds: ")

# function call

# countdown(int(t))

# Club or Country

def club_or_country():

    a = input("\nDo you want to choose club or country: ")

    if a == "Country" or "country" or "COUNTRY":

        playerTeamRandomCountry()

        OpponentPlayerTeamRandomCountry() 

    elif a == "club" or "Club" or "CLUB":

        playerTeamRandomClub()

        OpponentPlayerTeamRandomClub()

    else:

        print("\nInvalid input.")


def playerTeamRandomClub():

    player_team = ["Inter Milan","D.C. United", "Chelsea F.C.","Portland Timbers", "Real Salt Lake", "FCB Bacelona"]

    for name in random.sample(player_team, 1):

        player_team = name

        player_team = player_team.upper()

    PeanaltyShootout.player_team = player_team
 
def OpponentPlayerTeamRandomClub():

    Opponent_player_team = ["Sporting Kansas City", "LA Galaxy","Arsenal F.C.","Manchester United F.C.", "Liverpool F.C.", "Real Madrid"]
 
    for name in random.sample(Opponent_player_team, 1):

        Opponent_player_team = name

        Opponent_player_team = Opponent_player_team.upper()
 
    PeanaltyShootout.Opponent_player_team = Opponent_player_team

def playerTeamRandomCountry():

    player_team = ["Croatia", "England", "Korea", "Brazil", "Russia", "Italy"]

    for name in random.sample(player_team, 1):

        player_team = name

        player_team = player_team.upper()
    
    PeanaltyShootout.player = player_team

def OpponentPlayerTeamRandomCountry():

    Opponent_player_team = ["Norway", "France", "Germany", "Netherlands", "Japan"]

    for name in random.sample(Opponent_player_team, 1):

        Opponent_player_team = name

        Opponent_player_team = Opponent_player_team.upper()

    PeanaltyShootout.Opponent_player_team = Opponent_player_team

# Event Started

def soccerEvent():

    PeanaltyShootout.increaseEventCount()

    p_t = PeanaltyShootout.player_team

    v_p_t = PeanaltyShootout.Opponent_player_team

    ec = PeanaltyShootout.event_count

    print(f"Event: Soccer Shootout - ({ec}(Event Count)) ")

    print("Location: Los Angeles, California")

    print(f"\n{p_t} (You) vs. {v_p_t} ")

    print(f"You will represent {p_t} (You) and the opponent is {v_p_t}.")

    print("Let the soccer shootout begin!")

    
def playerKicker():

    p_t = PeanaltyShootout.player_team

    print(f"\nYou will be representing {p_t} in the shootout as a kicker.")
 
def playerGoalKepper():

    p_t = PeanaltyShootout.player_team

    print(f"\nYou will be representing {p_t} in the shootout as a GoalKepper.")

    print("GoalKepper")
    
# Choices

def playerShootoutKicks():

    PeanaltyShootout.increaseCountPlayer()

    c_p = PeanaltyShootout.count_player

    p_t = PeanaltyShootout.player_team

    while (c_p >= 1 and c_p <= 5):

        time.sleep(1)

        print(f"\nSetting up for shootout kick {c_p}. Where will you try to kick the ball? ")

        ball_kick = input("Please enter left, center, or right: ")

        ball_direction = ball_kick.upper()

        time.sleep(1)

        while (ball_direction != "LEFT" and ball_direction != "CENTER" and ball_direction != "RIGHT"):

            print("\nInvalid input.")

            ball_kick = input("Please enter left, center, or right: ")

            ball_direction = ball_kick.upper()

        directions = ["LEFT", "CENTER", "RIGHT"]

        for i in random.sample(directions, 1):

            kicker_location = i

        if ball_direction == kicker_location:

            PeanaltyShootout.increasePlayerShootoutGoals()

            ipsg = PeanaltyShootout.player_shootout_goals

            time.sleep(1)

            print(f"\nYou scored a goal at the {kicker_location} (RIGHT) location.")

            print(f"{p_t}(You) has scored {ipsg} goal(s).")

            playerShootoutKicks()

        else:

            PeanaltyShootout.increaseOpponentPlayerShootoutBlocks()

            time.sleep(1)

            print(f"\nThe GoalKepper blocked the kick at the {kicker_location} (RIGHT) location.")

            playerShootoutKicks()

    else:

        playerGoalKepper()

        OpponentPlayerShootoutKicks()

 
def OpponentPlayerShootoutKicks():

    directions = ["LEFT", "CENTER", "RIGHT"]

    PeanaltyShootout.increaseCountVirutalPlayer()

    cvp = PeanaltyShootout.count_Opponent_player

    v_p_t = PeanaltyShootout.Opponent_player_team

    while (cvp >= 1 and cvp <= 5):

        time.sleep(1)

        print(f"\nSetting up for shootout kick {cvp} for {v_p_t}. Where will you try to block the ball? ")

        ball_kick = input("Please enter left, center, or right: ")

        ball_direction = ball_kick.upper()

        time.sleep(1)

        while (ball_direction != "LEFT" and ball_direction != "CENTER" and ball_direction != "RIGHT"):

            print("\nInvalid input.")

            ball_kick = input("Please enter left, center, or right: ")

            ball_direction = ball_kick.upper()

        for i in random.sample(directions, 1):

            kicker_location = i

        if ball_direction == kicker_location:

            PeanaltyShootout.increaseVirutalPlayerShootoutGoals()

            ivpsg = PeanaltyShootout.Opponent_player_shootout_goals

            time.sleep(1)

            print(f"\n{v_p_t} scored a goal at the {kicker_location} (RIGHT) location.")

            print(f"{v_p_t} has scored {ivpsg} goal(s).")

            OpponentPlayerShootoutKicks()
        else:

            p_t = PeanaltyShootout.player_team

            PeanaltyShootout.increasePlayerShootoutBlocks()

            time.sleep(1)

            print(f"\n{p_t} (You) GoalKepper blocked the kick at the {kicker_location} (RIGHT) location.")

            OpponentPlayerShootoutKicks()

    else:

        shootoutScore()

 
# Score

def shootoutScore():

    v_p_t = PeanaltyShootout.Opponent_player_team

    p_t = PeanaltyShootout.player_team

    psg = PeanaltyShootout.player_shootout_goals

    vpsg = PeanaltyShootout.Opponent_player_shootout_goals

    print(f"\n{p_t} {psg} - {v_p_t} {vpsg} ")

    if psg == vpsg:

        print(f"\nThe shootout resulted in a tie.")

    elif psg > vpsg:

        print(f"\n{p_t} (You) Wins!!!")

    elif psg < vpsg:

        print(f"\n{v_p_t} Wins!!!")

        print(f"\n{p_t} (You) Lost")

    confirmPlay()

def confirmPlay():

    time.sleep(3)

    choice = int(input("\nEnter 1 to keep playing or 2 to quit: "))

    while choice < 1 or choice > 2:

        choice = int(input("\nInvalid Input, please enter 1 to keep playing or 2 to quit: "))

    if choice == 1:

        reset()

        playSoccerShooutoutAgain()

    else:

        sys.exit()
 
# Another Round

def reset():

    PeanaltyShootout.player_shootout_blocks = 0

    PeanaltyShootout.player_shootout_goals = 0

    PeanaltyShootout.count_player = 0

    PeanaltyShootout.Opponent_player_shootout_goals = 0

    PeanaltyShootout.Opponent_player_shootout_blocks = 0

    PeanaltyShootout.count_Opponent_player = 0
 

def playSoccerShooutoutAgain():

    club_or_country()

    playerTeamRandomClub()

    OpponentPlayerTeamRandomClub()

    soccerEvent()

    playerKicker()    

    playerShootoutKicks()
 
club_or_country()

playerTeamRandomClub()

playerTeamRandomCountry()

OpponentPlayerTeamRandomClub()

OpponentPlayerTeamRandomCountry()

soccerEvent()

playerKicker()

playerShootoutKicks()
