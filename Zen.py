import time


t1 = time.time()

x = "𓃟 = 𓃟   𓂻 = -"
x1 = "𓃠 = 𓃠   𓂻 = -"
x2 = "𓃠 = 𓃟 = 𓆣"
x3 = "𓆉 = 𓆉"
x4 = "𓅥 = 𓅥    𓂻 = -"
x5 = "𓃠 = 𓃠   𓂻 = -"
x6 = "𓅥 = 𓃠 = 𓆣"
x7 = "𓁟 = 𓊝 = 人"

print(bool(x))
print(bool(x1))
print(bool(x2))
print("1")
print(bool(x4))
print(bool(x5))
print(bool(x6))
print("人")


t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
