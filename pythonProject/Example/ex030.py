# Ex28,29는 없음. 미니 프로젝트는 크롤링. 숫자, 수치, value, 숫자(문자열), matplotlib 참고. ppt 준비. 크롤링할 사이트 선택.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()