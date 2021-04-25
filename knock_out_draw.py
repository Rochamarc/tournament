from random import choice 

def define_knock_out_stage(teams, phase):
    """ Receive a dict and a string return a dict"""

    output = {}

    if phase == 'Round of 16':
        for confront in range(len(teams['first'])):
            first = choice(teams['first'])
            teams['first'].remove(first) # remove
            second = choice(teams['second'])
            teams['second'].remove(second) # remove
        
            output[f'confrontation {confront}'] = [first, second]

        return output 

    for confront in range(len(teams['classified'])):
        first = choice(teams['classified'])
        teams['classified'].remove(first) # remove
        second = choice(team['classified'])
        teams['classified'].remove(second) # remove
        
        output[f'confrontation {confront}'] = [first, second]

    return output 


