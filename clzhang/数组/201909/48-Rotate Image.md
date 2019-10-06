## 48 Rotate Image（旋转图像）

给定一个 *n* × *n* 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。原地旋转。

## A

### 顺时针旋转 90 度：相当于 先副对角线转，再上下翻转

![1569409929494](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1569409929494.png)

```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int wide = matrix.size();
        for (int i = 0; i < wide; ++i) {
            for (int j = 0; j < wide - i; ++j) {
                swap(matrix[wide - 1 - j][wide - 1 - i], matrix[i][j]);
            }
        }
        for (int i = 0; i < wide/2; ++i) {
            for (int j = 0; j < wide; ++j) {
                swap(matrix[wide - 1 - i][j], matrix[i][j]);
            }
        }
    }
};
```



### 逆时针旋转 90 度：相当于 先主对角线转，再上下翻转



```C++
//逆时针旋转图像90度
class Solution {
public:
	void rotate_2(vector<vector<int>>& matrix) {
		int wide = matrix.size();
		for (int i = 0; i < wide; ++i) {
			for (int j = 0; j < wide - i; ++j) {
				swap(matrix[j][wide - 1 - i], matrix[wide - 1 - i][j]);
			}
		}
		for (int i = 0; i < wide / 2; ++i) {
			for (int j = 0; j < wide; ++j) {
				swap(matrix[wide - 1 - i][j], matrix[i][j]);
			}
		}
	}
};
```

