# Welcome to one of my first begginers projects, this is called "Madlibs" and here you can create
# your own story using different words up to your choice, have fun!


adj1 = input('Add an adjective: ')
adj2 = input('How do you think a developer is? Add an adjective: ')
adj3 = input('What do you think people think about us? Add an adjective: ')
adj4 = input('How do you think the reality is about a developer? Add an adjective: ')
verb1 = input('What verb best suits for what a dev does? : ')
noun1 = input('Who do you think we collaborate with? Type a noun: ')
noun2 = input('We create a better what? Add a noun: ')
noun3 = input('What else do you think we use in our job? Add a noun: ')
prep1 = input('Please add a preposition: ')
noun4 = input('Add a noun: ')
action = input('What do you think we are lack of? Add an action: ')
action2 = input('How do you think we spend our night? Add an action: ')
noun5 = input('Add a noun: ')
description = input('Add a description: ')
action3 = input('Add a verb: ')
years = int(input('How many years in the future?'))
action4 = input('Add a verb: ')
concept = input("In the future, which machine do you think you can make friends with?: ")
action5 = input('What action do you think you could get from a machine? Add a verb: ')
job = input('Type a job or occupation: ')
tech = input('What kind of futuristic machine you think could help you keep you warm?: ')
adj5 = input('Please choose an adjective: ')
verb2 = input('What do you think developers are here for? Type a verb: ')


madlib = (
    f'The path of a developer is sometimes {adj1} , since many of us are usually {adj2}. People think we are {adj3}, but the reality is way too {adj4}. \n'
    f'We create, {verb1}, improve and collaborate with other {noun1} around the world. \n'
    f'Our task is to make a better {noun2}. Using Internet and {noun3} to make things {prep1} easier for the rest of the population. \n'
    f'Some of us do not have {noun4} to {action}, or maybe we spend the night {action2} to make your {noun5} better. From Web Developers, Data Scientists, AI engineers and app developers, \n'
    f'there is a very {description} range of areas in which we can {action3} with the future of technology. \n'
    f'Imagine a world {years} years from now. Do you think we are going to {action4} among robots?\n'
    f'Someday your best friend could be a {concept}. When you are old, you could get {action5} from a {job} robot or maybe, \n'
    f'if you are cold, you could get warm thanks to the {tech} we develop to make your future {adj5}. \n'
    f'\n'
    f'We are like that. We are here to {verb2} the future of technology.'
    f''
    f'')


print(madlib)