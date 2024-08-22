import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,25,5)
data = [
    [],
    []]
dataval = input("Input your values in the form x y, enter -1 to terminate and display statistics: ").split()
i=1
while len(dataval)>1:
    i+=1
    data[0].append(float(dataval[0]))
    data[1].append(float((dataval[1])))
    dataval = input("Data pair "+str(i)+": ").split()

def correlation_coefficient():
    avgx = 0
    stdx = 0
    for i in range(0, len(data[0])):
        avgx = avgx + (data[0][i])
    avgx = avgx/(len(data[0]))
    for i in range(0, len(data[0])):
        stdx = stdx + ((data[0][i]-avgx)**2)
    stdx = (stdx/(len(data[0])-1))**0.5
    avgy = 0
    stdy = 0
    for i in range(0, len(data[0])):
        avgy = avgy + (data[1][i])
    avgy = avgy / (len(data[1]))
    for i in range(0, len(data[1])):
        stdy = stdy + ((data[1][i]-avgy)**2)
    stdy = (stdy/(len(data[1])-1))**0.5
    r = 0
    for i in range(0, len(data[0])):
        r = r + (data[0][i]-avgx)*(data[1][i]-avgy)/(stdx*stdy)
    r = r/(len(data[0])-1)
    m = r*stdy/stdx
    b = avgy-(m*avgx)
    y = (m*x)+b
    print("\n\nMETHOD 1:")
    print(f"mean of x: {round(avgx,2)}\nmean of y: {round(avgy,2)}\nstandard deviation of x: {round(stdx,2)}\nstandard deviation of y: {round(stdy,2)}\ncoefficient of determination (r): {round(r,2)}\ngradient of line: {round(m,2)}\ny-intercept: {round(b,2)}")
    plt.plot(x, y, color='grey')
    plt.xlim(min(data[0])-5, max(data[0])+5)
    plt.ylim(min(data[1])-5, max(data[1])+5)
    plt.scatter(data[0], data[1],s=25, color='purple')
    plt.grid(color='#00B2EE', linestyle=':', linewidth=1.0)
    plt.show()


def regression_line():
    avgx = 0
    for i in range(0, len(data[0])):
        avgx = avgx + (data[0][i])
    avgx = avgx / (len(data[0]))
    avgy = 0
    for i in range(0, len(data[0])):
        avgy = avgy + (data[1][i])
    avgy = avgy / (len(data[1]))
    avgxy = 0
    for i in range(0, len(data[0])):
        avgxy += data[0][i]*data[1][i]
    avgxy=avgxy/len(data[0])
    avgx2 = 0
    for i in range(0, len(data[0])):
        avgx2 += data[0][i]**2
    avgx2 = avgx2/len(data[0])
    avgy2=0
    for i in range(0, len(data[1])):
        avgy2 += data[1][i]**2
    avgy2 = avgy2/len(data[1])
    m = (avgxy-(avgx*avgy))/(avgx2-(avgx**2))
    r=m*((avgx2-(avgx**2))**0.5)/((avgy2-(avgy**2))**0.5)
    b = avgy-(avgx*m)
    y = m*x+b
    print("\n\nMETHOD 2:")
    print(f"mean of x: {round(avgx,2)}\nmean of y: {round(avgy,2)}\ncoefficient of determination (r): {round(r,2)}\ngradient of line: {round(m,2)}\ny-intercept: {round(b,2)}")
    plt.plot(x, y, color='blue')
    plt.xlim(min(data[0])-5, max(data[0])+5)
    plt.ylim(min(data[1])-5, max(data[1])+5)
    plt.scatter(data[0], data[1],s=25, color='brown')
    plt.grid(color='#00B2EE', linestyle=':', linewidth=1.0)
    plt.show()

correlation_coefficient()
regression_line()
