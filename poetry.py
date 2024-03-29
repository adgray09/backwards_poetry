from random import shuffle, random, randint

poem = '''If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!
'''
lines = poem.split("\n")
def lines_printed_backwards(lines):
    '''This function takes in a list of strings 
    containing the lines of your poem as arguments and will 
    print the poem lines out in reverse with the line numbers reversed'''
    lines.reverse()
    line_count = len(lines)

    for i in range(len(lines)):
        line = lines[i]
        print(line)
        print(line_count)
        line_count -= 1
    

def lines_printed_random(lines):
    '''will randomly select lines from a list of strings
    and print them out in random order'''
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
# shuffle(lines)
# print(" \n".join(lines)) 
# lines = poem.split("\n")

    i = 0 
    while i < len(lines):
        random_index = randint(1, len(lines) - 1)
        item = lines[random_index]
        print(item)
        i += 1

# def user_choice():
#     question = input("enter in your own poem ")
#     lines = question.split("\n")
    
#     for i in range(len(lines)):
#         line = lines[i]
#         print(line)

def sort_by_length_of_line(lines):
    '''Takes in list of strings and sorts by length of characters. '''
    line_size = sorted(lines, key=len)
    print(line_size)
        
        
    
    
    
    
    
    



#TODO: 
#print(poem)
#testing code
sort_by_length_of_line(lines)

