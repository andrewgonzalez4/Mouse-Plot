import pyautogui
import time
import matplotlib.pyplot as plt

start = time.perf_counter()
def test():
    file = open('test.txt', 'w')
    while time.perf_counter() - start < 1:
        file.write(str(pyautogui.position().x) + ' ')
        file.write(str(pyautogui.position().y) + '\n')
    file.close()

def plot():
     with open('test.txt') as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]
        plt.plot(x,y)
        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.show()
test()
plot()