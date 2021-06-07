import pandas as pd
import plotly.express as px
import csv 
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")

math_list = df["math score"].tolist()
reading_list = df["reading score"].tolist()
writing_list = df["writing score"].tolist()


#Mean , median and mode for math
math_mean = statistics.mean(math_list)
math_median = statistics.median(math_list)
math_mode = statistics.mode(math_list)

#Mean median mode for reading
reading_mean = statistics.mean(reading_list)
reading_median = statistics.median(reading_list)
reading_mode = statistics.mode(reading_list)

#Mean , median and mode for writing
writing_mean = statistics.mean(writing_list)
writing_median = statistics.median(writing_list)
writing_mode = statistics.mode(writing_list)


print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
#print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_mean, writing _median, writing _mode))


#std deviation
math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation = statistics.stdev(writing_list)

print("Std deviation for math is {}".format(math_std_deviation))
print("Std deviation for reading is {}".format(reading_std_deviation))
print("Std deviation for writing is {}".format(writing_std_deviation))



math_first_std_deviation_start,math_first_std_deviation_end = math_mean -math_std_deviation ,math_mean+math_std_deviation
math_second_std_deviation_start,math_second_std_deviation_end = math_mean - 2* math_std_deviation ,math_mean + 2* math_std_deviation
math_third_std_deviation_start,math_third_std_deviation_end = math_mean - 3* math_std_deviation ,math_mean + 3* math_std_deviation


reading_first_std_deviation_start,reading_first_std_deviation_end = reading_mean -reading_std_deviation ,reading_mean+reading_std_deviation
reading_second_std_deviation_start,reading_second_std_deviation_end = reading_mean - 2* reading_std_deviation ,reading_mean + 2* reading_std_deviation
reading_third_std_deviation_start,reading_third_std_deviation_end = reading_mean - 3* reading_std_deviation ,reading_mean + 3* reading_std_deviation


writing_first_std_deviation_start,writing_first_std_deviation_end = writing_mean -writing_std_deviation ,writing_mean+writing_std_deviation
writing_second_std_deviation_start,writing_second_std_deviation_end = writing_mean - 2* writing_std_deviation ,writing_mean + 2* writing_std_deviation
writing_third_std_deviation_start,writing_third_std_deviation_end = writing_mean - 3* writing_std_deviation ,writing_mean + 3* writing_std_deviation


#Percentage of data within 1, 2 and 3 Standard Deviations for math
math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]


#Percentage of data within 1, 2 and 3 Standard Deviations for reading
reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]


#Percentage of data within 1, 2 and 3 Standard Deviations for writing
writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]


print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))


print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))


print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))
