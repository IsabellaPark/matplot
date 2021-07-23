import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4]
# y1 = [1, 4, 9, 14]
# y2 = [9, 8, 2, 10]
# y3 = [7, 4, 3, 8]

# plt.plot(x,y1, color = "green", marker = "o")
# plt.plot(x,y2, color = "purple", marker = "o")
# plt.plot(x,y3, color = "pink", marker = "o")

# plt.xlabel("distance")
# plt.ylabel("time")

# plt.title("Swimming")
# plt.legend(["Y1", "Y2", "Y3"])

# plt.show()
weight_values =[72,87,64,63,71,31,62,65]
height_values =[30,70,100,56,10,23,15,54]
sizes = []

for i in height_values:
  sizes.append(i * 2)


plt.scatter(height_values, weight_values, sizes)
plt.xlabel("amount")
plt.ylabel("days")

plt.title("sugar graph")


plt.show()

