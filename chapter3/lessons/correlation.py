import matplotlib.pyplot as plt
import csv

def find_corr_x_y(x,y):
    n = len(x)
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)
    y_square=[]
    for yi in y:
        y_square.append(yi**2)
    y_square_sum = sum(y_square)
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    return correlation

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
    return summer, highest_correlated

summer, highest_correlated = read_csv('correlate-summer.csv')
corr = find_corr_x_y(summer, highest_correlated)
print('Highest correlation: {0}'.format(corr))
scatter_plot(summer, highest_correlated)

# high_school_math = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
# college_admission = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
# corr = find_corr_x_y(high_school_math, college_admission)
# print('Correlation coefficient: {0}'.format(corr))
