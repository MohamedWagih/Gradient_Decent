import matplotlib.pyplot as plt

theta0 = 0
theta1 = 0
alpha = 0.0002

# x = list(range(1, 20))
# y = list(range(1, 20))

x = [18, 20, 21, 25, 26, 27, 30, 33]
y = [10, 15, 25, 30, 31, 35, 44, 50]

# print(x)
# print(y)
print("m = ", len(x))


itr = 0
cost = [0]
cost.clear()
while(1):
    H_theta = [theta0 + theta1 * i for i in x]
    temp_sum0 = 0
    temp_sum1 = 0
    temp_sum2 = 0
    for i in range(len(y)):
        temp_sum0 += H_theta[i] - y[i]
    for i in range(len(y)):
        temp_sum1 += (H_theta[i] - y[i]) * x[i]
    for i in range(len(y)):
        temp_sum2 += (H_theta[i] - y[i]) ** 2

    cost.append((1 / 2 * len(y)) * temp_sum2)
    temp0 = theta0 - alpha * (1 / len(y)) * temp_sum0
    temp1 = theta1 - alpha * (1 / len(y)) * temp_sum1
    if (temp0 - theta0 <= 0.0001) and (temp1 - theta1 <= 0.0001):
        break
    if (temp0 - theta0 <= 0.0001) and (temp1 - theta1 <= 0.0001):
        break

    theta0 = temp0
    theta1 = temp1
    itr += 1


print("theat0 = ", theta0)
print("theat1 = ", theta1)

plt.plot(x, y, 'ro')  # RED POINTS IS THE DATA
plt.plot(x, H_theta, 'b')  # BLUE LINE IS THE H_THETA
plt.ylabel('y , H_theta')
plt.xlabel('x')
plt.show()


# print(J)
print("total itr: ", itr)

plt.plot(range(itr + 1), cost)
plt.ylabel('cost value')
plt.xlabel('Itr num')
plt.show()
