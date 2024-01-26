from tkinter import *
from tkinter import ttk

solution = [(b, y, p) for b in range(1,6) for y in range(1,6) for p in range(1,6) ]
solutionFilter = { }
for b in range(1,6):
    for y in range(1,6):
        for p in range(1,6):
            solutionFilter[(b, y, p)] = True

def refresh():
    msg = ''
    count = 0
    prevBlue = -1
    prevYellow = 1
    for i in range(len(solution)):
        blue = solution[i][0]
        yellow = solution[i][1]
        purple = solution[i][2]
        if yellow != prevYellow:
            if blue != prevBlue:
                msg += '\n'
            else:
                msg += ' | '
        elif blue == prevBlue:
            msg += ' '
        if solutionFilter[(blue, yellow, purple)] == False:
            msg += '...'
        else:
            msg += str(blue) + str(yellow) + str(purple)
            count += 1
        prevBlue = blue
        prevYellow = yellow
    msg += f"\ntotal: {count}\n"
    msgVar.set(msg)

def filter(name, condition):
    #show(f'filtering on whether {name}')
    for b, y, p in solution:
        if not eval(condition):
            solutionFilter[(b, y, p)] = False

#filter('blue is equal to 1', 'b == 1')
#filter('blue is greater than 1', 'b > 1')
#filter('there are more evens than odds', '(b % 2 + y % 2 + p % 2) <= 1')
#filter('there are more odds than evens', '(b % 2 + y % 2 + p % 2) > 1')
#filter('there is a double number', 'b == y or y == p or b == p')
#filter('there is no repetition', 'b != y and b != p and y != p')
#filter('there are no 3s', 'b != 3 and y != 3 and p != 3')
#filter('there is exactly one 3', '(b == 3 and y != 3 and p != 3) or (b != 3 and y == 3 and p != 3) or (b != 3 and y != 3 and p == 3)')
#filter('there are exactly two 3s', '(b == 3 and y == 3 and p != 3) or (b == 3 and y != 3 and p == 3) or (b != 3 and y == 3 and p == 3)')

#filter('numbers are ascending', 'b < y and y < p')
#filter('numbers are descending', 'b > y and y > p')

#refresh()

root = Tk()
root.title("turing completer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

msgVar = StringVar()
ttk.Label(mainframe, textvariable=msgVar).grid(column=2, row=2, sticky=(W, E))

def blueEqualsOne():
    filter('blue is equal to 1', 'b == 1')

def blueDoesNotEqualOne():
    filter('blue does not equal 1', 'b != 1')

blueIsOne = StringVar()
check = ttk.Checkbutton(mainframe, text='blue == 1', 
	    command=blueEqualsOne, variable=blueIsOne,
	    onvalue='metric', offvalue='imperial')

ttk.Button(mainframe, text="refresh", command=refresh).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()