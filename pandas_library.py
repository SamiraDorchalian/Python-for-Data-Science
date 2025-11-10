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
