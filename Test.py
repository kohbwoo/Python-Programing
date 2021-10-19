from sklearn.datasets import load_breast_cancer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib

# matplotlib 설정
matplotlib.rc('font', family='AppleGothic') # 한글 설정
plt.rcParams['axes.unicode_minus'] = False # -표시

# data load
cancer = load_breast_cancer()

# data  분할
x_train, x_test, y_train, y_test = \
  train_test_split( # 데이터 분할을 위해
      cancer.data, cancer.target, # 분할할 데이터
      random_state=0, test_size=0.3 # 랜덤상태, 테스트 비율
      )

# feature visualization
plt.boxplot(x_train, manage_xticks=False) # 데이터, 소눈금 표시 안하기
plt.yscale('symlog') # 축 스케일을 log 로
plt.xlabel('feature list') # x축 이름
plt.ylabel('feature') # y축 이름
plt.show() # 그래프 출력