# fluffy-chainsaw
# strings part 1
scorer_name_1 = 'Ruud Gullit '

scorer_name_2 = 'Marco van Basten '

goal_0 = 32

goal_1 = 54

when_gullit_scored = str(32)
print(when_gullit_scored)
when_vanbasten_scored = str(54)
print(when_vanbasten_scored)
scorers = scorer_name_1 + when_gullit_scored, scorer_name_2 + when_vanbasten_scored

report = scorer_name_1 + 'scored in the ' + when_gullit_scored + 'nd minute' , scorer_name_2 + 'scored in the ' + when_vanbasten_scored + 'th minute' 

report = scorer_name_1 + " scored in the {}nd minute\n " + scorer_name_2 + " scored in the {}th minute"
print(report.format(goal_0,goal_1))

#strings part 2
player = 'Ruud Gullit'

player[0:4]
name = 'Ruud Gullit'
x = name.find('Ruud')

x = name.find('Gullit')
 
player[5:11]
print(len(player[5:11]))
last_name_len = (player[5:11])

first_name = (player[0:4])

first_name[0] + '. ' + last_name_len
name_short = first_name[0] + '. ' + last_name_len

chant = (first_name + '! ') * 3 + (first_name + '!')

string_a = 'Ruud! Ruud! Ruud! Ruud! '
string_b = 'Ruud! Ruud! Ruud! Ruud!'
if string_a == 'Ruud! Ruud! Ruud! Ruud! ':
    print('string_b != string_a')
good_chant = string_b
    
