from enum import Enum
import schedule
import time
import threading
import sys


class ObjectState(Enum):
    """
    This enum contains the state of Objects of the Game (Monsters and Hero) of whether they are dead or alive.
    """
    alive = 'Alive'
    dead = 'Dead'


class GameObject:
    """
    A class that defines characteristics and actions of Object of the Game.
    """
    def __init__(self, health_points: int, damage_points: int):
        """
        Initiates the Game Object with given number of Health Points and Damage points (amount of health damage it does
        to its enemy in a single attack). Also Ascertains whether Object is dead (if healthpoints <= 0 ) or alive
        (healthpoints > 0)
        :param health_points: Health Points of the Game Object
        :param damage_points: Damage Points of the health Object
        """
        self.health_points: int = health_points
        self._damage_points: int = damage_points
        self.state: ObjectState = ObjectState.alive if self._damage_points > 0 else ObjectState.dead

    def __update_state(self):
        """
        After Sustaining an attack from Enemy object, the game object should update its own state of whether its is dead
        or alive based on health points (dead if health points <= 0 else alive).
        to
        :return:
        """
        self.state: ObjectState = ObjectState.alive if self.health_points > 0 else ObjectState.dead
        self.health_points = 0 if self.state == ObjectState.dead else self.health_points

    def attack_enemy(self, enemy_object):
        """
        This method simulates the action of a Game Object Attacking an enemy.
        The Game Object can attack an enemy if:
            1. The attacking object itself is in 'Alive' state
            2. The enemy object getting attacked is in 'Alive' state

        If an object attacks an enemy object, the enemy object's health points will be reduced by the number of damage
        points of the attacking object.
        :param enemy_object:
        :return:
        """
        if self.state == ObjectState.alive:
            if enemy_object.state == ObjectState.alive:
                print(f"\n**{self.__class__.__name__} has attacked the {enemy_object.__class__.__name__}!**")
                enemy_object.health_points -= self._damage_points
                enemy_object.__update_state()
                print(f"=====\nHealth of {enemy_object.__class__.__name__} after attack {enemy_object.health_points}\n=====\n")
            elif enemy_object.state == ObjectState.dead:
                print(f"\n**{self.__class__.__name__} has attacked the {enemy_object.__class__.__name__} "
                      f"but its already dead!**\n")


class Monster(GameObject):
    """
    A Parent Class for Monsters Objects of the Game i.e Orc and Dragon. Inherits from GameObject class.
    """
    def __init__(self, health_points: int, damage_points: int):
        super().__init__(health_points, damage_points)


class Orc(Monster):
    """
    A class for Monster Object of Game 'Orc'
    """
    def __init__(self, health_points: int, damage_points: int):
        super().__init__(health_points, damage_points)


class Dragon(Monster):
    """
    A class for Monster Object of Game 'Dragon'
    """
    def __init__(self, health_points: int, damage_points: int):
        super().__init__(health_points, damage_points)


class Hero(GameObject):
    """
    A class for Hero of the game i.e. Player who user can control.
    """
    def __init__(self, health_points: int, damage_points: int):
        super().__init__(health_points, damage_points)


def start():
    """
    Begins the game by creating objects.
    :return: None
    """
    print("Game Has begun!!!! \n You control the Hero!\nAttack the Orc or Dragon by typing 'attack orc' "
          "or 'attack dragon' ")

    orc_o = Orc(7, 1)
    dragon_o = Dragon(20, 3)
    player_o = Hero(40, 2)

    def take_player_input():
        """
        Function that helps take Player's console input and perform either an attack on orc or dragon or return
        invalid input if the input does not meet the requirement. The input taking functionality is
        :return: None
        """
        while True:
            answer = input("")
            if answer is not "":
                if answer == "attack orc":
                    player_o.attack_enemy(orc_o)
                elif answer == "attack dragon":
                    player_o.attack_enemy(dragon_o)
                else:
                    print("####Invalid input####\n")
            time.sleep(0.1)

    def run_thread():
        """
        This function runs a thread with code of capturing Player's input so that the rest of the code execution
        is not paused to wait for user input. So rest of the code executes without waiting for user input.
        :return:
        """
        t1 = threading.Thread(target=take_player_input)
        t1.daemon = True
        t1.start()

    def orc_attack():
        """
        Used to simulate Orc attacking Hero based on user input
        :return: None
        """
        orc_o.attack_enemy(player_o)

    def dragon_attack():
        """
        Used to simulate Dragon attacking Hero based on user input
        :return: None
        """
        dragon_o.attack_enemy(player_o)

    def check_game_state():
        """
        Checks the state of the game. If Hero is dead, then player loses game, If both monsters are dead then Player
        wins the game. In any case stats such as health points of winners are displayed and program is stopped.
        :return: None
        """
        if player_o.state == ObjectState.dead:
            print(f"\n++++++Hero has died game Over! You Lose!++++++\n")
            print(f"====Stats====\nHealth of Dragon {dragon_o.health_points}\n"
                  f"Health of orc {orc_o.health_points}\n========")
            sys.exit(0)
        elif orc_o.state == ObjectState.dead and dragon_o.state == ObjectState.dead:
            print(f"\n++++++Hero wins the Game!!!!++++++\n")
            print(f"====Stats====\nHealth of Hero {player_o.health_points}\n")
            sys.exit(0)

    # Runs the thread on which user input capturing executes.
    run_thread()
    # Schedule and Orc attack on hero every 1500 ms
    schedule.every(1.5).seconds.do(orc_attack)
    # Schedule and Dragon attack on hero every 1500 ms
    schedule.every(2).seconds.do(dragon_attack)
    # Do a Game state check every 300 ms to check if game is over or not.
    schedule.every(0.3).seconds.do(check_game_state)

    # Start executing the scheduler
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    start()


# attack dragon
#
#
# attack orc