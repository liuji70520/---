# 编程实现肽序列的AA531(531 properties of Amino Acids)特征表征/数值化
## 一、将AA531properties.txt做成字典  


```python3
df = pd.read_csv("../data/AA531properties.txt", delimiter='\t', header=None, skiprows=1)
AA531Dict = df.set_index(0).T.to_dict('list')
```
## 二、肽序列表征         
### 1、得到行数即三肽数目150行，         
