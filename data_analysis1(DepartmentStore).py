import numpy as np
import pandas as pd

sal = pd.read_csv("C:\\Users\\ziggurat\\Desktop\python for data science\\train.csv")
# print(sal)
# print(sal.head()) # 5 سطر اول رو میده
# print(sal.info()) # اطلاعات عنوان ستون ها و تایپ داده رو میده
# print(sal.shape) # تعداد سطر و ستون ها رو میده
# print(sal.columns) # عنوان تمام ستون ها رو میده
                                    # درمورد مفهوم هرکدام از داده ها گفتگو کنید
# print(sal.describe())
                                    # کمترین ، بیشترین و میانگین فروش را محاسبه کنید
# print(sal['Sales'].min())
# print(sal['Sales'].max())
# print(sal['Sales'].mean())
                                    # این فروشگاه از چند شهر متنوع سفارش گرفته است؟
# print(sal['City'].unique())       # مقادیر تکراری رو نشون نمیده
# print(sal['City'].nunique())        # تعداد کل شهر ها
                                    # پنج تاریخی که این فروشگاه بیشترین سفارش رو گرفته

                                    # سفارشاتی که مبلغ فروش انها بیشتر از 800 دلار است را فیلتر کنید
# print(sal['Sales'] > 800)
# print(sal[sal['Sales'] > 800])
                                    # بیشترین و کمترین فروش مربوط به کدام کشور است
# print(sal[sal['Sales'] == sal['Sales'].max()])
# print(sal[sal['Sales'] == sal['Sales'].max()]['City'])

# print(sal[sal['Sales'] == sal['Sales'].min()])
# print(sal[sal['Sales'] == sal['Sales'].min()]['City'])

# print(sal[sal['Sales'] == sal['Sales'].max()]['Country'])
# print(sal[sal['Sales'] == sal['Sales'].min()]['Country'])

# print(sal['City'].value_counts())  # بیشترین تعداد سفارشات هر شهر
# print(sal['City'].value_counts().head())
                        # سفارشاتی که در شهر لس انجلس انجام شده را فیلتر کنید و بگویید در مجموع این فروشگاه چقدر فروش در این شهر داشته؟
# print(sal[sal['City'] == "Los Angeles"])                
# print(sal[sal['City'] == "Los Angeles"].sum())                
                    #ارسال شده اند را فیلتر کنید"California"در ایالت  "San Francisco"تمام سفارش هایی که به شهر  
# print(sal[(sal['City'] == 'San Francisco') & (sal['State'] == 'California')])
                                    # تمام سفارشاتی که در سال 2017 ثبت شده اند را فیلتر کنید
# print(sal['Order Date'] == pd.to_datetime(sal["Order Date"], format= "%d/%m/%Y"))
                                                # group by #
                                    # تعداد کل سفارشات برای هر دسته محصول را پیدا کنید
# print(sal.groupby('Category')['Sales'].agg(min))
                                    # تعداد کل سفارشات برای هر دسته محصول را محاسبه کنید
# print(sal.groupby("Category")["Order ID"].count())
                                    #  مجموع فروش برای هر دسته محصول را محاسبه کنید
# print(sal.groupby("Category")["Sales"].sum())
                                    # بیشترین و کمترین فروش برای هر دسته از محصول رو محاسبه کنید
# print(sal.groupby("Category")["Sales"].agg(min))

