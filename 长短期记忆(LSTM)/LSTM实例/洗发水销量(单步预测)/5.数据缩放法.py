from pandas import read_csv
from pandas import datetime
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
"""
ͨ������MinMaxScaler��feature_range���������Խ��������������ⷶΧ��
"""

# ���ݸ�ʽ����
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series)

# transform scale
X = series.values
X = X.reshape(len(X), 1)
# feature_range�����������ŷ�Χ
scaler = MinMaxScaler(feature_range=(-1, 1))
# �����ݽ������䣬�ҵ������Сֵ�����������ں���ת��
scaler = scaler.fit(X)
# ��ʼת������,���һ����ά����
scaled_X = scaler.transform(X)
print(scaled_X)
# ����ά����ת��������
scaled_series = Series(scaled_X[:, 0])
print(scaled_series)

# �����ź�����ݷ���ת����ԭֵ
inverted_X = scaler.inverse_transform(scaled_X)
inverted_series = Series(inverted_X[:, 0])
print(inverted_series)