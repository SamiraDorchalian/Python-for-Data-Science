import numpy as np
import pandas as pd

arr_1 = np.random.rand(20)
# print(arr_1)
condition_arr_1 = np.where(arr_1 > 0.5, 1, 0)
# print(condition_arr_1)
# print(arr_1 * 10)
#---------------------------------------------------
mat_1 = np.random.randint(1, 20, 9).reshape(3, 3)
mat_2 = np.random.randint(1, 100, 9).reshape(3, 3)
# print(mat_1)
# print(mat_2)
# print(mat_1 * mat_2)
# print(mat_1 + mat_2)
                                                                    ## linalg ##
dat_1 = np.linalg.det(mat_1)
# print(dat_1)
dat_2 = np.linalg.det(mat_2)
# print(dat_2)
                                                                    ## eig ##
eig_1 = np.linalg.eig(mat_1)
# print(eig_1)
eig_2 = np.linalg.eig(mat_2)
# print(eig_2)
#---------------------------------------------------
arr_2 = np.random.randint(0, 100, 16).reshape(4, 4)
# print(arr_2)
ones_arr_2 = np.ones((4, 4)) + arr_2
# print(ones_arr_2)
number_smaller_than_50 = arr_2[arr_2 > 50]
# print(number_smaller_than_50)

condition_arr_2 = np.where(arr_2 >50, 50, arr_2)
# print(condition_arr_2)
#---------------------------------------------------
arr_3 = np.random.randint(0, 10, 9).reshape(3,3)
# print(arr_3)
arr_4 = np.random.randint(0 , 10, 3)
# print(arr_4)
print(arr_3 + arr_4)
#---------------------------------------------------
