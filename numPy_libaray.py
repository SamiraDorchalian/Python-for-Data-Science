import numpy as np
                                                        ## vectore ##
# list_1 = [1, 2, 3, 4]
# print(list_1)

# conversion_list_to_array_One_dimensional = np.array(list_1)
# print(conversion_list_to_array_One_dimensional)

                                                        ## Matrix ##

# list_2 = [[1,2,3], [4,5,6]]
# print(list_2)

# conversion_list_to_array_Two_dimensional = np.array(list_2)
# print(conversion_list_to_array_Two_dimensional)

                                                        ## arange ##
# arange_vslue = np.arange(0, 10)
# print(arange_vslue)

# arange_vslue = np.arange(0, 20, 5)
# print(arange_vslue)

                                                        ## zeros Matrix
# make_matrix_zeros = np.zeros(5)
# print(make_matrix_zeros)

# make_matrix_zeros = np.zeros((5, 5))
# print(make_matrix_zeros)

                                                        ## linspace ##
# linspace_number = np.linspace(0, 100, 6)
# print(linspace_number)

                                                        ## eye - Diagonal matrix ##
# diagonal_matrix = np.eye(5)
# print(diagonal_matrix)

                                                        ## random and rand ##
# random_number = np.random.rand(2)
# print(random_number)

# random_number = np.random.rand(2, 2)
# print(random_number)

                                                        ## random and randint ##
# random_int = np.random.randint(0, 100)
# print(random_int)

# random_int = np.random.randint(0, 100, 5)
# print(random_int)

                                                        ## math.inf - بینهایت " ∞ "

# print(np.math.inf)

                                                        ## math.nan - تهی " ∅ " 

# print(np.math.nan)

                                                ##      array method        ##


                                                        ## shape ##
# arr = np.array([1,2,3,4,5,])
# print(arr.shape)
                                                        ## reshape ##
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr.shape)
# reshap_arr = arr.reshape(5,2)
# print(reshap_arr)

# arr = np.random.randint(0, 100, 25)
# print(arr)
# print(arr.shape)
# reshap_arr = arr.reshape(5,5)
# print(reshap_arr)
                                                        ## max & min ##
# print(reshap_arr.max())
# print(reshap_arr.min())
                                                        ## argmax & argmin ##
# print(reshap_arr.argmax())
# print(reshap_arr.argmin())
                                                        ## flatten ##
# print(reshap_arr.flatten())

                                                        ## vstack & hstack & concatenate ##
day1= np.array([[1,2],[3,4]])
day2= np.array([[11,2],[6,5]])
# vstack_arr = np.vstack((day1, day2))
# vstack_arr = np.hstack((day1, day2))
# vstack_arr = np.concatenate((day1, day2), axis=0)
# vstack_arr = np.concatenate((day1, day2), axis=1)
# print(vstack_arr)
                                                        ## dtype ##
# print(day1.dtype)
# print(day2.dtype)


                                                 ##      indexing        ##
# for i in day1:
#     print(i)

# print(day1[0])
# print(day1[1])
                                                        ## update_with_index ##
# update_with_index = np.arange(0, 20, 2)
# print(update_with_index)
# update_with_index[0:4] = 1
# print(update_with_index)
                                                        ## copy ##
# update_with_index = np.arange(0, 20, 2)
# print(update_with_index)
# update_with_copy= update_with_index.copy()[0:6]
# print(update_with_copy)

                                                        ## transpose ##
# mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(mat)
# print(mat.transpose())

                                                        ## triu & tril ##
# matrix_triu_and_tril = np.random.randint(0,100,25).reshape(5, 5)
# print(matrix_triu_and_tril)
# print(np.triu(matrix_triu_and_tril))
# print(np.tril(matrix_triu_and_tril))



