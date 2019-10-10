from pandas import read_csv
from pandas import datetime
from pandas import Series

"""
������о�����һ�������У����������������
ֻ���������еı仯�ʣ��ų������������е���������
"""
# ����һ���������
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return Series(diff)

# ��ԭ�������
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

# ���ݸ�ʽ����
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series)
# ��ֺ�������ֲ���Ϊ1
differenced = difference(series, 1)
print(differenced)
# invert transform
inverted = list()
for i in range(len(differenced)):
	value = inverse_difference(series, differenced[i], len(series)-i)
	inverted.append(value)

inverted = Series(inverted)
print(inverted)