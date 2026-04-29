# -*- coding: utf-8 -*-
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.key())   #data와 target만 사용

X, y = mnist.data, mnist.target 
print(X)
print(X.shape) #28 x 28개의 픽셀 특징을 가진 이미지 70,00개
print(y)
print(y.shape)

import mat