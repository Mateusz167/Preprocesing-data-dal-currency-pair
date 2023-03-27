import pandas
import random
import numpy
import json

#Part 1
data = pandas.read_csv('EURUSD_H4.csv')  # Data loading
data_to_use = pandas.DataFrame((data.head(2500)))

# counting empty values and averaging them for the close column
data_to_use.drop(columns=['SMA14IND', 'SMA50IND'], axis=1, inplace=True)
nullVal_close_column = data_to_use["Close"].isnull().sum()
print(nullVal_close_column)
data_to_use["Close"] = data_to_use["Close"].interpolate()

# Fixing blank values for SMA14 AND SMA50 columns - AVERAGE
nullVal_sma14_column = data_to_use["SMA14"].isnull().sum()
print(nullVal_sma14_column)
data_to_use["SMA14"] = data_to_use["SMA14"].interpolate()

nullVal_sma50_column = data_to_use["SMA50"].isnull().sum()
print(nullVal_sma50_column)
data_to_use["SMA50"] = data_to_use["SMA50"].interpolate()

# Filling in empty values in other attributes with zeros
data_to_use["Bulls"] = data_to_use["Bulls"].fillna(0)
data_to_use["CCI"] = data_to_use["CCI"].fillna(0)
data_to_use["DM"] = data_to_use["DM"].fillna(0)
data_to_use["OSMA"] = data_to_use["OSMA"].fillna(0)
data_to_use["RSI"] = data_to_use["RSI"].fillna(0)
data_to_use["Stoch"] = data_to_use["Stoch"].fillna(0)
# #you can go faster
# data_to_use = data_to_use.fillna(0)

# Correlation between SMA14 and SMA50
correllation = data_to_use["SMA14"].corr(data_to_use["SMA50"])
print(correllation)

# Collation between SMA14 and Close and SMA50 and Close
correllation_SMA14 = data_to_use["SMA14"].corr(data_to_use["Close"])
correllation_SMA50 = data_to_use["SMA50"].corr(data_to_use["Close"])
print(correllation_SMA14)
print(correllation_SMA50)

# Remove the column (SMA14 or SMA50) for which the correlation value with the Close column was greater
if correllation_SMA14 > correllation_SMA50:
    data_to_use.drop(columns=["SMA14"], axis=1, inplace=True)
else:
    data_to_use.drop(columns=["SMA50"], axis=1, inplace=True)

# The number of negative elements for the CCI attribute
CCI_negative_values = (data_to_use["CCI"] < 0).sum().sum()
print(f"Negative valuse for CCI atribute is {CCI_negative_values}")

# Minimum and maximum values for each attribute
min_val = []
max_val = []

for i in data_to_use:
    min_val.append(data_to_use[i].min())
    max_val.append(data_to_use[i].max())

print(f"Max values for each attribute is {max_val} and min values for each attribute is {min_val}")

# Normalization for Bulls and CCI attributes
atributes = ["Bulls", "CCI"]

for atribute in atributes:
    max = data_to_use[atribute].max()
    min = data_to_use[atribute].min()
    data_to_use[atribute] = (data_to_use[atribute] - min) / (max - min)

# Discretization of 2 selected attributes
lable = ["Down", "Up"]
series = pandas.Series(numpy.array(data_to_use["Bulls"]))
result = pandas.cut(series, 2, labels=lable)

lable = ["[0:0.25]", "[0.25:0.50]", "[0.50:0.75]", "[0.75: 1.00]"]
series = pandas.Series(numpy.array(data_to_use["CCI"]))
result = pandas.cut(series, 4, labels=lable)

# Pie chart for the distribution of decision values
data_to_use["Decision"].value_counts().plot.pie()

data_to_use["Close"].plot()
data_to_use.to_json()

# Part 2
import random

help_list = ['Close', 'SMA50', 'Bulls', 'CCI', 'DM', 'OSMA', 'RSI', 'Stoch', 'Decision']

data_frame = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

Decision_possibilities = ["BUY", "STRONGBUY", "SELL", "STRONGSELL", "WAIT"]
first_row = []


def choice_sign():
    """Function draws the number by which the next value is to be changed (+- 1%)"""
    sign = [0.01, -0.01]
    return random.choice(sign)


def generate_new_value():
    new_value = round(data_frame[column][i - 1] + data_frame[column][i - 1] * choice_sign(), 5)
    return new_value


def put_values(column, min, max):
    """Function fills a column of 2500 rows from the minimum and maximum range for the given attribute."""
    for i in range(2499):
        new_value = round(data_frame[column][i - 1] + data_frame[column][i - 1] * choice_sign(), 5)
        # new_value = round((1 + choice_sign()) * data_frame[column][(i - 1)], 5)
        if new_value >= max:
            data_frame[column].append(max)
        elif new_value <= min:
            data_frame[column].append(min)
        elif min < new_value < max:
            data_frame[column].append(new_value)


# Drawing of the first value in each column within the range of minimum and maximum values from the previous programme
for i in range(0, 8):
    first_row.append(round(random.uniform(min_val[i], max_val[i]), 5))

# Column completion of up to 2500 values
for i in range(0, len(first_row)):
    data_frame[i].append(first_row[i])
for atribute in range(0, 8):
    put_values(atribute, min_val[atribute], max_val[atribute])

for decision_number in range(2500):
    data_frame[8].append(random.choice(Decision_possibilities))
print(data_frame)
print(first_row)
# Create a data frame
list_data = []

data = pandas.DataFrame()
data['Close'] = data_frame[0]
data['SMA50'] = data_frame[1]
data['Bulls'] = data_frame[2]
data['CCI'] = data_frame[3]
data['DM'] = data_frame[4]
data['OSMA'] = data_frame[5]
data['RSI'] = data_frame[6]
data['Stoch'] = data_frame[7]
data['Decision'] = data_frame[8]
print(data)

# Calculation of the correlation between each of the columns from the two sets
corelation_list = []
cor_value = data.corrwith(data_to_use, axis = 0)
corelation_list.append(cor_value)

print(f"correlation for specific column is: {corelation_list}")
print(2)


