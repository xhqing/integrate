import pandas as pd
import numpy as np
from scipy.integrate import cumulative_trapezoid

# 创建一个包含时间序列数据的 DataFrame
data = {'时间': pd.date_range(start='2022-01-01', end='2022-01-30', freq='D'),
        '数值': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 
                 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 
                 54, 56, 58, 60, 62, 64, 66, 68]}
df = pd.DataFrame(data)

# 计算序列的数值积分
integral = cumulative_trapezoid(y=df['数值'])

print(integral)

