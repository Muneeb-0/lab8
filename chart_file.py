import matplotlib.pyplot as plt
names = ['onion','ginger','garlic','mango']
no_sold = [10,15,12,9]

plt.bar(names,no_sold, color='red')
plt.title("bar plot for units sold for vegetables and fruits")
plt.show()