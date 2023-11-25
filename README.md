# 编程实现肽序列的AA531(531 properties of Amino Acids)特征表征/数值化
最终目的是将每一个三肽相关的特征转换为数值矩阵，所以得先将每一个氨基酸对应的生理生化指标提取出来。其中用数字标签来表示对应的多肽
## 一、将AA531properties.txt做成字典  
这里每一个氨基酸有着531生理生化指标，即AA531properties.txt第一行
```python3
df = pd.read_csv("../data/AA531properties.txt", delimiter='\t', header=None, skiprows=1)
AA531Dict = df.set_index(0).T.to_dict('list')
```
## 二、肽序列表征           
### 1、得到行数即三肽数目150行，一个三肽有着三个氨基酸，一个氨基酸有着531个生理生化，故而一个三肽有着3*531个特征数值 
```python3

```
