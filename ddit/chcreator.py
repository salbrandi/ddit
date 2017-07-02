#!/usr/bin/python
import numpy



Game_Version = 'Dungeon & Dragons: 5th edition'
attrs = ['race', 'class', 'background', 'deity', 'level', 'saving throws',
 'armor class', 'proficieny', 'equipment', 'inventory', 'skills', 'name',
 'maximum health', 'item proficiencies', 'currency']

abbrevs = ['rc', 'cls', 'bg', 'dty', 'lv', 'sth', 'ac', 'pro', 'eqp', 'inv',
 'name', 'hp', 'i_pro', 'gp']

race_list = [
'Tiefling,0,0,0,1,0,2', 'Forest_Gnome,0,0,1,2,0,0',
 'Rock_Gnome,0,1,0,2,0,0', 'Lightfoot_Halfling,0,0,2,0,0,1',
 'Stout_Halfling,0,1,2,0,0,0', 'Hill_Dwarf,0,2,0,0,1,0',
 'Mountain_Dwarf,2,2,0,0,0,0', 'Human,1,1,1,1,1,1',
 'High_Elf,0,0,2,1,0,0', 'Wood_elf,0,0,2,0,1,0', 'Drow,0,0,2,0,0,1',
 'Half-Elf,0,0,0,0,0,2', 'Dragonborn,2,0,0,0,0,1', 'Half-Orc,2,1,0,0,0,0']

stats = ['str', 'con', 'dex', 'int', 'wis', 'cha']

skill_list = [
'Athletics,str',
'Sleight of Hand,dex',
'Acrobatics,dex',
'Stealth,dex',
'Arcana,int',
'History,int',
'Investigation,int',
'Nature,int',
'Religion,int',
'Animal,Handling, wis',
'Insight,wis',
'Medicine,wis',
'Perception,wis',
'Survival,wis',
'Deception,cha',
'Intimidation,cha'
'Performance,cha',
'Persuasion,cha'
]

class_list = [
'Barbarian,12',
'Bard,8',
'Cleric,8',
'Druid,8',
'Fighter,10',
'Monk,8',
'Paladin,10',
'Ranger,10',
'Rogue,8',
'Sorcerer,6',
'Warlock,8',
'Wizard,6',
]

def calc_sign(a):
    return (a>0) - (a<0)

def calc_mod(s_value):
    mod = int(numpy.floor(0.5*s_value)-5)
    return mod


class pacter():
    def set_info(self, atr, arg):
      setattr(self, atr, args)


pc = pacter()
proficiency = 2

def calc_stats(strength, dex, con, intel, wis, cha, race, cliss, skill1, skill2, level):
    stat_list = [strength, dex, con, intel, wis, cha]
    print(Game_Version)
    print('Race: ' + race)
    print('Class: ' + cliss)
    print('-----------------------')
    print('Character Stats')
    print('-----------------------')

    # Race Based Stat Bonuses
    for idx, i in enumerate(stat_list):
        rcname_list = []
        name_and_stats = []
        for item in race_list:
            name_and_stats = item.split(',')
            rcname_list.append(name_and_stats[0])
            if name_and_stats[0] == race:
                fl_list = name_and_stats
        rc = rcname_list[rcname_list.index(race)]
        rc_stats = list(map(int, fl_list[1:]))
        stat_list = list(map(int, stat_list))
        stat_list[idx] = stat_list[idx] + rc_stats[idx]
        if calc_mod(stat_list[idx]) < 0:
            print(str(stats[idx]) + ': ' + str(stat_list[idx])
            + ' (' + str(calc_mod(stat_list[idx])) + ')')
        else:
            print(str(stats[idx]) + ': ' + str(stat_list[idx])
            + ' (+' + str(calc_mod(stat_list[idx])) + ')')


    # Class Based Max Hp

    clname_list = []
    fl_list = []
    for item in class_list:
        statandname = item.split(',')
        clname_list.append(statandname[0])
        if statandname[0] == cliss:
            fl_list =  statandname
    cl_stats = fl_list[1]
    cl = clname_list[clname_list.index(cliss)]
    maxhp = int(cl_stats) + calc_mod(stat_list[1])


    print('Max HP: ' + str(maxhp) + ' (' + str(level) + 'd' + cl_stats + " + "
    + str(calc_mod(stat_list[1])) + ")")

    print('----------------------')
    print('Skills')
    print('-----------------------')

    # Selection and Stat Based Skill Bonusus

    fls_list = []
    for skl in skill_list:
        sklname = skl.split(',')[0]
        if sklname == skill1 or sklname == skill2:
            sklname_list = []
            for item in skill_list:
                skill_stat = item.split(',')
                sklname_list.append(skill_stat[0])
                if sklname == skill_stat[0]:
                    fls_list = skill_stat
            skl_stat_name = fls_list[1]
            skill_number = calc_mod(stat_list[stats.index(skl_stat_name)])
            skill_bonus = skill_number + proficiency
            print(sklname + ': +' + str(skill_bonus))
        else:
            print(sklname + ': +' + str(proficiency))

    print('-----------------------')
    print('Proficiency: ' + str(proficiency))
    print('-----------------------')
