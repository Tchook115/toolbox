import matplotlib.pyplot as plt

def joli_scatter(x=None, y=None, color=None, figsize=None):
    if x==None:
        x_ = input('Insert x here: \n')
    if y==None:
        y_ = input('Insert y here: \n')

    if color == None:
        color = input('Choose color here: blue, red, yellow, orange:\n')

    # if figsize == None:
    #     figsize = input('Choose figsize here : format -->(num,num)\n')

    try:
        # plt.figure(figsize=figsize)
        plt.scatter(x=x_, y=y_, color=color)
        plt.show()
    except ValueError:
        print('raté')
