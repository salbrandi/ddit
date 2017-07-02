import numpy
import click
import random
from chcreator import calc_stats

class dice():
    def __init__(self):
        self.total = 0

dc = dice()

fumble_list = [
'Slipped - You must make a successful DC 10 DEX Save or immediately fall prone.',
'Something in your eye - Your accuracy is halved for your next attack',
'Wicked backswing - You strike yourself slightly on your backswing and take 1d8 damage',
'Wind knocked out of you - You become exhausted to level 1 of that condition',
'Loss of confidence - You gain disadvantage for your attacks against this opponent for the remainder of the encounter',
'Shook yourself up - You are stunned for 1 rd',
'Give them hope - Your target’s allies within 30 feet gain a d6 inspiration die that can be used during this encounter',
'Panic attack - You must make a successful DC 10 WIS Save or become frightened for the remainder of the encounter.',
'Dropped weapon - Your drop your weapon and it falls 10’ from your location in a random direction',
'You’ve fallen and you can’t get up - You immediately fall prone and lose all movement this round.',
'Bad timing - You drop to last in the imitative order for the combat but do not act again this turn.',
'Broken bone -  You break a bone in your hand. You suffer disadvantage for the rest of the encounter and take 1d6 damage every rd. until healed.',
'Easy prey -  Allies of the target within 20’ will attack you with their next turn, unless they would suffer an Attack of Opportunity to do so.',
'Exposed defenses - Your swing unbalances you so much that your target may take one melee attack against you as a reaction',
'Your own worst enemy - You suffer the effects of a bane spell for the remainder of the encounter',
'Unguarded - All adjacent allies of your target may immediately take an attack of opportunity against you',
'Costly mistake - Your target may reroll all 1s and 2s on the damage roll for his next successful melee attack vs. you',
'Revealed intentions - You and your allies all suffer disadvantage for your next attack',
'Wrong target - You mistakenly strike an ally adjacent to you with your attack',
'Devastating error - As a free action your opponent may immediately make one melee attack with advantage against you as a reaction',
'Shattered,  Your weapon breaks if it is non-magical. Enchanted weapons must make a DC 8 Save and get a +1 to their roll for every + of the weapon',
'Thrown weapon - You lose your grip and throw your weapon. It lands 30’ from your location in a random direction',
'Horrible aftermath - Roll twice on this chart and apply both effects to yourself',
'Self-inflicted wound - Your attack ricochets back and you hit yourself. Roll your damage as if you had hit your target and apply it to yourself',
'Did you see that? - Your attack ricochets back and you hit yourself. Apply the maximum damage to yourself as if you had hit your target']


@click.group()
def roll():
    pass


@click.command()
@click.argument('number', required=False, default=1)
def roll_d12(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 12)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")


@click.command()
@click.argument('number', required=False, default=1)
def roll_d10(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 10)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")


@click.command()
@click.argument('number', required=False, default=1)
def roll_d8(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 8)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")


@click.command()
@click.argument('number', required=False, default=1)
def roll_d6(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 6)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")


@click.command()
@click.argument('number', required=False, default=1)
def roll_d4(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 4)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")


@click.command()
@click.argument('number', required=False, default=1)
def roll_d20(number):
    dc.total = 0
    for i in range(number):
        result = random.randint(0, 20)
        dc.total += result
    click.echo('your roll: ' + str(dc.total) + "!")
    if dc.total == 1:
        fumble = input("Critical Failure! would you like to fumble? y/n")
        if fumble == "yes" or "y":
            percentile = random.randint(0, 100)
            click.echo(fumble_list[percentile%25])
    if dc.total == 20:
        click.echo('Critical Success! On an attack roll, your attack crits!')


@click.command()
def p_fumble():
    percentile = random.randint(0, 100)
    click.echo(fumble_list[percentile%25])


@click.command()
@click.argument('strength')
@click.argument('con')
@click.argument('dex')
@click.argument('intelligence')
@click.argument('wis')
@click.argument('cha')
@click.argument('race')
@click.argument('cliss')
@click.argument('skill1')
@click.argument('skill2')
@click.argument('level', required=False, default=1)
def create_character(strength, con, dex, intelligence, wis, cha, race, cliss, skill1, skill2, level):
    calc_stats(strength, con, dex, intelligence, wis, cha, race, cliss, skill1, skill2, level)



roll.add_command(create_character, name='setup')
roll.add_command(roll_d20, name='d20')
roll.add_command(roll_d12, name='d12')
roll.add_command(roll_d10, name='d10')
roll.add_command(roll_d8, name='d8')
roll.add_command(roll_d6, name='d6')
roll.add_command(roll_d4, name='d4')
