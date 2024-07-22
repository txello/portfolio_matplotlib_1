import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

legend = plt.legend()

def animate(i):
    global legend
    graph_data = pd.read_csv('example.csv',names=['ID','attention','meditation','theta','delta','lowAlpha','highAlpha','lowBeta','highBeta',
                                                  'lowGamma','highGamma','poorSignalLevel','status','time'])
    ax1.clear()
    ax1.plot(graph_data['ID'], graph_data['theta'], label="theta")
    ax1.plot(graph_data['ID'], graph_data['delta'], label="delta")
    ax1.plot(graph_data['ID'], graph_data['lowAlpha'], label="lowAlpha")
    ax1.plot(graph_data['ID'], graph_data['highAlpha'], label="highAlpha")
    ax1.plot(graph_data['ID'], graph_data['lowBeta'], label="lowBeta")
    ax1.plot(graph_data['ID'], graph_data['highBeta'], label="highBeta")
    ax1.plot(graph_data['ID'], graph_data['lowGamma'], label="lowGamma")
    ax1.plot(graph_data['ID'], graph_data['highGamma'], label="highGamma")
    legend.remove()
    legend = plt.legend()
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()