import pandas as pd

# 创建一个示例DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': [5, 1, 3, 3, 2, 5, 4, 1],
    'C': ['apple', 'orange', 'banana', 'strawberry', 'blueberry', 'blackberry', 'pineapple', 'raspberry']
})
print(df)
# 使用groupby找到每组B列的最大值
idx = df.groupby('A')['B'].transform(max)== df['B']
filtered_df = df[idx]

print(filtered_df)
