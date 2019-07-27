import matplotlib.pyplot as plt
import numpy as np
welcome=""
wel=welcome.center(100,'*')
print(wel)
print('Welcome to Graph Go! \n')
print("Graph Go is a non-graphical program that helps its users creating beautiful and stunning graphs with just a few clicks \n")
print('1: Line Graph \n2: Bar Graph \n3: Pie Chart \n4: Scatter Graph\n')
choice=input('Choose your desired graph option from the menu above: ')
if choice=='1':
    x = []
    y = []
    numberx=int(input('How many values of x do you want to plot? '))
    for i in range(0, numberx): 
	    number = int(input('Enter the value of x-axis: '))
	    x.append(number) 
    
    number2=int(input('How many values of y do you want to plot? '))
    for i in range(0, number2): 
	    numbery = int(input('Enter the value of y-axis: '))
	    y.append(numbery)
    title=input("Enter the title for your graph: ")
    a=input('Choose the color of your graph: ')
    xlabel=input('Enter the x-axis label: ')
    ylabel=input('Enter the y-axis label: ')

    plt.plot(x,y, color=a)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    print('Do you want to save the figure')
    print('Choose: \n1: Yes \n2: No')
    save=input('Choice: ')
    if save=='1':
        name=input('Enter the file name: ')
        plt.savefig(name+".png")
    elif save=='2':
        print('Thankyou for using GraphGo!')

if choice=='2':
    print('For a Bar Graph, you need to load data from an external source.\n')
    filename=input("Enter File Name: ")
    Year, Profit=np.loadtxt(filename, unpack=True)
    barcolor=input('Choose bar color: ')
    cfill=input('Do you want it to be colour filled: ')
    chatch=input('Choose your hatch? ')
    bartitle=input("Enter the title for your graph: ")
    barxlabel=input('Enter the x-axis label: ')
    barylabel=input('Enter the y-axis label: ')

    plt.bar(Year, Profit, color=barcolor, fill=cfill, hatch=chatch)
    plt.title(bartitle)
    plt.xlabel(barxlabel)
    plt.ylabel(barylabel)
    plt.show()
    print('Do you want to save the figure')
    print('Choose: \n1: Yes \n2: No')
    save=input('Choice: ')
    if save=='1':
        name=input('Enter the file name: ')
        plt.savefig(name+".png")
    elif save=='2':
        print('Thankyou for using GraphGo!')

if choice=='3':
    print('For a Pie Chart, you need to load data from an external source.\n')
    filename=input("Enter File Name: ")
    Year, Profit=np.loadtxt(filename, unpack=True)
    bartitle=input("Enter the title for your graph: ")
    barxlabel=input('Enter the x-axis label: ')
    barylabel=input('Enter the y-axis label: ')

    plt.pie(Profit,labels=Year) 
    plt.title(bartitle)
    plt.xlabel(barxlabel)
    plt.ylabel(barylabel)
    plt.show()
    print('Do you want to save the figure')
    print('Choose: \n1: Yes \n2: No')
    save=input('Choice: ')
    if save=='1':
        name=input('Enter the file name: ')
        plt.savefig(name+".png")
    elif save=='2':
        print('Thankyou for using GraphGo!')
      
if choice=='4':
    print('For a Scatter Graph, you need to load data from an external source.\n')
    filename=input("Enter File Name: ")
    Year, Profit=np.loadtxt(filename, unpack=True)
    bartitle=input("Enter the title for your graph: ")
    barxlabel=input('Enter the x-axis label: ')
    barylabel=input('Enter the y-axis label: ')
    scolor=input('Choose the graph color: ')
    smarker=input('Choose the graph marker: ')

    plt.scatter(Year,Profit,color=scolor ,marker=smarker) 
    plt.title(bartitle)
    plt.xlabel(barxlabel)
    plt.ylabel(barylabel)
    plt.show()
    print('Do you want to save the figure')
    print('Choose: \n1: Yes \n2: No')
    save=input('Choice: ')
    if save=='1':
        name=input('Enter the file name: ')
        plt.savefig(name+".png")
    elif save=='2':
        print('Thankyou for using GraphGo!')

else:
        print('Invalid Selection. Program Ended!')