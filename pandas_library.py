import pandas as pd
import numpy as np
# import sys
# print(sys.executable)

                                                #  Different data structures in Pandas  #
                                                    ## Series & DataFrame & Index  ##
                                                            ##  Series  ##

# dic = {'Alex': 400, "David": 500, "Sara": 450}   ----> Dic
# list_1 = ["A", "B", "C", "D"]   ----> List

# print(pd.Series(list_1))

# print(pd.Series([400,500,450],["Alex","David","Sara"]))

# sr = pd.Series([400,500,450],["Alex","David","Sara"])
# print(sr["David"]) ----> index
# print(sr[0]) ----> value

# dic_1 = pd.Series([400,500,450],["Alex","David","Sara"])
# dic_2 = pd.Series([600,800,250],["David","Alex","Sara"])

# sum_value = dic_1 + dic_2
# print(sum_value)
# sum_value = dic_1 * dic_2
# print(sum_value)
# sum_value = dic_1 / dic_2
# print(sum_value)

# dic_3 = pd.Series([400,500,450,100],["Alex","David","Sara", "Ali"])
# dic_4 = pd.Series([600,800,250,40],["David","Alex","Sara", "Samira"])
# sum_value_nan = dic_3 + dic_4
# sum_value_nan
                                                            ## DataFrame ##
# df = np.random.randint(0, 100, 25).reshape(5, 5)
# print(df)
# data_frame = pd.DataFrame(df, ["a", "b", "c", "d", "e"], ["A", "B", "C", "D", "E"]) # سطر و ستون = جدول
# print(data_frame)
# print(data_frame["A"]) # برای نشون دادن یک ستون
# print(data_frame[["A", "D"]]) # برای نشون دادن دو یا چند ستون دلخواه
                                                        ## loc % iloc ##
# print(data_frame.loc["a"]) # برای نشون دادن سطر
# print(data_frame.iloc[1]) #نشون دادن index  اون سطر مورد نظر

                                                ## creating new column ##

# per = pd.DataFrame([[400,500,450,100], [500, 600, 430, 900],[200, 300, 120, 780], [210, 880, 640, 90]], ["Baran","Sahar","Kamiar", "Habib"], ["Mehre","Aban","Azar", "Dey"])
# print(per)
# creating_new_column = per["Bahman"]=[100,200,300,400]
# print(creating_new_column)

                                                ## drop / delete ##
# print(per.drop("Mehre", axis = 1)) # حذف ستون
# print(per.drop("Baran", axis = 0)) # حذف سطر

                ##  ----------------------------------------------------------------------------------------------------  ##
# df_1402 = pd.Series([67 , 1999 , 299, 300,123, 34 ,12] , ["Iran" , "Japan" , "usa" , "turk" , "France", "Arbic" , " Afghanestan"])
# print(df_1402)

# born = pd.Series([0.5 , 2 ,3 , 4 ,0.9, 0.2 ,0.1] , ["Iran" , "Japan" , "usa" , "turk" , "France", "Arbic" , " Afghanestan"])
# print(born)

# df_1403 = born + df_1402
# print(df_1403)

# death = pd.Series([0.2 , 1.5 ,5  , 2 ,1.5, 0.5 ,2] , ["Iran" , "Japan" , "usa" , "turk" , "France", "Arbic" , " Afghanestan"])
# print(df_1402 / 2)