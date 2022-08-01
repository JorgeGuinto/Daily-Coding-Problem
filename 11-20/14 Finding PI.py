"The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method."
"Hint: The basic equation of a circle is x2 + y2 = r2."
import matplotlib.pyplot as plt
import random

def pi(n):
    points = []
    for i in range(n):
        points.append([random.randrange(-25, 25), random.randrange(-25,25)])
    
    plt.xlim(-35, 35)
    plt.ylim(-35, 35)
    plt.grid()
    count = 0
    for p in points:
        if (p[0]**2 + p[1]**2) <= (25**2):
            #plt.plot(p[0], p[1], marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
            count += 1
        else:
            #plt.plot(p[0], p[1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
            "Nada"    
    area = (50*50) * count/n #Area del cuadrado con puntos aleatorios * porcentaje de puntos dentro del círculo
    #PI = area / 25**2
    PI = 4 * count/n
    print(f"Pi equivale a:\n{PI}")
    #plt.show()

pi(1000000)