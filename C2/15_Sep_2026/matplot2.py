import random
import matplotlib.pyplot as plt
d = [random.randint(1, 30) for _ in range(400)]
plt.hist(d, bins=15)
plt.title("random value histogram") 
plt.show()

import matplotlib.pyplot as plt
cate = ['Fashion', 'Electronics', 'Travel', 'Manufacturing']
sale = [200, 450, 600, 1000]
plt.pie(sale, labels=cate, autopct='%1.1f%%', startangle=0)
plt.title("Sector wise sales")
plt.show()

