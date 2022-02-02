# fluffy-chainsaw
scorer_name_1 = 'Ruud Gullit '
scorer_name_1
scorer_name_2 = 'Marco van Basten '
scorer_name_2
goal_0 = 32
goal_0
goal_1 = 54
goal_1
when_gullit_scored = str(32)
print(when_gullit_scored)
when_vanbasten_scored = str(54)
print(when_vanbasten_scored)
scorers = scorer_name_1 + when_gullit_scored, scorer_name_2 + when_vanbasten_scored
scorers
report = scorer_name_1 + 'scored in the ' + when_gullit_scored + 'nd minute' , scorer_name_2 + 'scored in the ' + when_vanbasten_scored + 'th minute' 
report
report = scorer_name_1 + " scored in the {}nd minute\n " + scorer_name_2 + " scored in the {}th minute"
print(report.format(goal_0,goal_1))

#Part 2
player = 'Ruud Gullit'
player
player[0:4]
name = 'Ruud Gullit'
x = name.find('Ruud')
x
x = name.find('Gullit')
x 
player[5:11]
print(len(player[5:11]))
last_name_len = (player[5:11])
last_name_len
first_name = (player[0:4])
first_name
first_name[0] + '. ' + last_name_len
name_short = first_name[0] + '. ' + last_name_len
name_short
chant = (first_name + '! ') * 3 + (first_name + '!')
chant
good_chant = ?
