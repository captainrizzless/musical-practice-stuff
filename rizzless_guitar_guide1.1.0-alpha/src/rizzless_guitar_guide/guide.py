import scalestuff
import modestuff
import intervalstuff

selected_topics = {}

main_menu_prompt = ('Main Menu\n'
                    'Program options:\n'
                    '  (Show) Displays concepts.\n'
                    '  (Hide) Removes concept from final review.\n'
                    'Good to do for accidental searches.\n'
                    '  (Print) Prints list that documents what the user\n'
                    'has searched to review areas of focus for practice.\n'
                    '  (Quit) Terminates program.\n'
                    '\n'
                    'Enter input: ')
main_menu_options = ['Show', 'Hide', 'Print', 'Quit']

table_of_contents_prompt = ('Concept options:\n'
                            '  (Scales) Displays Scales.\n'
                            '  (Modes) Displays Modes.\n'
                            '  (Intervals) Displays basic Interval information.\n'
                            '  (More Intervals) Displays information about Circle of Fifths/Fourths, Order of\n'
                            'Sharps/Flats, etc.\n'
                            '\n'
                            'Enter concept: ')
table_of_contents = ['Scales', 'Modes', 'Intervals', 'More Intervals']

vocab = []
for i in main_menu_options, table_of_contents:
    vocab.append(i)
for i in scalestuff.scale_list, modestuff.mode_list, intervalstuff.interval_list1, intervalstuff.interval_list2:
    vocab.append(i)
# todo fix valid() to correctly check items of 'vocab' container


def valid(command):
    if len(command) == 0:
        print('Enter command or type \'quit\' to terminate.')
        return
    elif command not in vocab:
        print('Try again')
        return


def hide():
    global user_input
    topic = input('Enter topic you wish to remove from topic review:\n').strip().lower().title()
    if topic in selected_topics:
        selected_topics.__delitem__(topic)
        user_input = input(main_menu_prompt[26:]).strip().lower().title()
        return
    else:
        print("Topic already removed OR wrong input was entered")
        return


def print_check():
    if not selected_topics:
        print('Nothin\' here')


def format_print():
    global user_input
    for user_input in selected_topics:
        topic_location()


def topic_location():
    global user_input
    topic = user_input
    if topic in scalestuff.scale_list:
        print('{} found within {}'.format(user_input.title(), table_of_contents[0]))
        print()
        return
    elif topic in modestuff.mode_list:
        print('{} found within {}'.format(user_input.title(), table_of_contents[1]))
        print()
        return
    elif topic in intervalstuff.interval_list1:
        print('{} found within {}'.format(user_input.title(), table_of_contents[2]))
        print()
        return
    elif topic in intervalstuff.interval_list2:
        print('{} found within {}'.format(user_input.title(), table_of_contents[3]))
        print()
        return


print("Welcome to Michael's Music Theory Program!\n")
user_input = input(main_menu_prompt).strip().lower().title()

while user_input != 'Quit':
    if user_input == 'Show':
        user_input = input(table_of_contents_prompt).strip().lower().title()
        continue
    elif user_input == 'Scales':
        user_input = input(scalestuff.scales_prompt).strip().lower().title()
        continue
    elif user_input == 'Major':
        print(scalestuff.major_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Major Pentatonic':
        print(scalestuff.major_penta_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Minor':
        print(scalestuff.minor_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Melodic Minor':
        print(scalestuff.melminor_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Harmonic Minor':
        print(scalestuff.harminor_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Minor Pentatonic':
        print(scalestuff.minor_penta_scale_prompt)
        selected_topics[user_input] = 'Scale'
        user_input = ''
        continue
    elif user_input == 'Modes':
        user_input = input(modestuff.modes_prompt).strip().lower().title()
        valid('Modes')
        continue
    elif user_input == 'Ionian':
        print(modestuff.ionian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Dorian':
        print(modestuff.dorian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Phrygian':
        print(modestuff.phrygian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Lydian':
        print(modestuff.lydian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Mixolydian':
        print(modestuff.mixolydian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Aeolian':
        print(modestuff.aeolian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Locrian':
        print(modestuff.locrian_mode_prompt)
        selected_topics[user_input] = 'Mode'
        user_input = ''
        continue
    elif user_input == 'Intervals':
        user_input = input(intervalstuff.interval_menu).strip().lower().title()
        valid('Intervals')
        continue
    elif user_input == 'Interval Basics':
        print(intervalstuff.interval_basics)
        selected_topics[user_input] = 'Interval'
        user_input = ''
        continue
    elif user_input == 'Chord Basics':
        print(intervalstuff.chord_basics)
        selected_topics[user_input] = 'Interval'
        user_input = ''
        continue
    elif user_input == 'Chord Progressions':
        print(intervalstuff.chord_progs)
        selected_topics[user_input] = 'Interval'
        user_input = ''
        continue
    elif user_input == 'Arpeggio Basics':
        print(intervalstuff.arpeggio_basics)
        selected_topics[user_input] = 'Interval'
        user_input = ''
        continue
    elif user_input == 'More Intervals':
        user_input = input(intervalstuff.more_intervals_menu).strip().lower().title()
        valid('More Intervals')
        continue
    elif user_input == 'Circles':
        print(intervalstuff.circles_prompt)
        selected_topics[user_input] = 'More Intervals'
        user_input = ''
        continue
    elif user_input == 'Orders':
        print(intervalstuff.orders_prompt)
        selected_topics[user_input] = 'More Intervals'
        user_input = ''
        continue

    elif user_input == 'Hide':
        hide()
        continue

    elif user_input == 'Print':
        print_check()
        format_print()
        user_input = ''
        continue

    valid(user_input)
    user_input = input(main_menu_prompt[26:]).strip().lower().title()
