import pandas as pd
import matplotlib.pyplot as plt

# Zad1
print("Zad1")
miasta = pd.read_csv (r'./miasta.csv')

print(miasta.values)

# Zad2
print("Zad2")
new_row = pd.DataFrame([[2010, 460, 555, 405]],
                   columns=['Rok', 'Gdansk', 'Poznan', 'Szczecin'])

miasta = pd.concat([miasta, new_row], ignore_index=True)

print(miasta)

# Zad3
xpoints = miasta['Rok'].values
ypoints = miasta['Gdansk'].values
plt.plot(xpoints, ypoints, color='r', marker="o")
plt.ylabel('Liczba ludności (w tys)')
plt.xlabel('Lata')
plt.suptitle('Ludność w Gdańsku')
plt.show()


# Zad4
xpoints = miasta['Rok'].values
gdansk = miasta['Gdansk'].values
poznan = miasta['Poznan'].values
szczecin = miasta['Szczecin'].values
plt.plot(xpoints, gdansk, color='r', marker="o", label="Gdansk")
plt.plot(xpoints, poznan, color='b', marker="o", label="Poznan")
plt.plot(xpoints, szczecin, color='y', marker="o", label="Szczecin")
plt.ylabel('Liczba ludności (w tys)')
plt.xlabel('Lata')
plt.suptitle('Ludność w miastach Polski')
plt.legend()
plt.show()
