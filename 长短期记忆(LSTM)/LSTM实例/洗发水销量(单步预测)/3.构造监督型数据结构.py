from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from pandas import concat

# ����ලѧϰ���ݽṹ
def timeseries_to_supervised(data, lag=1):
    df = DataFrame(data)
    print(df)
    # ���д�������һ�����飬��df�����ƶ�һλ��Ϊ��һ��Ԫ��
    # ����������Ĵ���д����Ϊ������һ�������б�����ݽṹ��������һ������
    # columns = df.shift(1)���ɵ���һ�����У��������б�
    columns = [df.shift(i) for i in range(1, lag+1)]
    print(columns)
    print(df)
    # df��Ϊ�ڶ���Ԫ��
    columns.append(df)
    # ��df.shift(1)��df���кϲ������ɼල������
    df = concat(columns, axis=1)
    print(df)
    # ��NaNλ�ò���
    df.fillna(0, inplace=True)
    return df


# ���ݸ�ʽ����
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')


series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# transform to supervised learning
X = series.values
print(X)
supervised = timeseries_to_supervised(X, 1)
print(supervised)