import csv
import math
import matplotlib.pyplot as plt

def main():
    
    input_list = [];
    output_list = [];
    variation_list = [];
    
    with open('task_1.tsv') as input_file:
        for line in input_file:
            num = float(input_file.readline())
            input_list.append(num)
        print("read")

    output_list = sorted(input_list)
    print("sorted")


    # Получаем вариационный ряд для НСВ
    
    min_val = output_list[0]
    max_val = output_list[-1]
    
    variation_range = max_val - min_val
    variances_num = len(output_list)
    
    # Формула Стёрджесса
    number_of_intervals = 1 + math.floor(math.log2(variances_num))
    
    interval_length = variation_range / number_of_intervals
    rounded_interval_length = math.ceil(interval_length)
    # enumeration здесь это перебор
    enumeration = (rounded_interval_length - interval_length ) *  number_of_intervals

    # Создаём список интервалов и листы с минимальными и максимальными значениями
    intervals = [ [] for x in range(number_of_intervals)]
    min_values = []
    max_values = []
    
    interval_min_value = min_val - enumeration / 2
    interval_max_value = interval_min_value + rounded_interval_length
    
    for x in range(number_of_intervals):
        interval_min_value += rounded_interval_length
        min_values.append(interval_min_value)

    for x in range(number_of_intervals):
        interval_max_value += rounded_interval_length
        max_values.append(interval_max_value)

    for count, el in enumerate(intervals):
        for variation in output_list:
            if variation > min_values[count] and variation < max_values[count]:
                el.append(variation)


    frequencies = [len(el) for el in intervals]
    relative_freq = [el / sum(frequencies) for el in frequencies]
    density = [ el / rounded_interval_length for el in relative_freq]

    # Сам вариационный ряд для НСВ
    variation_list = []
    for count, el in enumerate(intervals):
        variation_list.append((min_values[count] + max_values[count]) / 2)

    # Относительные накопленные частоты
    cumulative_relative_freq = []
    for index, el in enumerate(relative_freq):
        if index == 0:
            cumulative_relative_freq.append(relative_freq[index])
        else:
            cumulative_relative_freq.append(cumulative_relative_freq[index - 1] + relative_freq[index]) 

            
    print(variation_list)
    print(density)
    print(cumulative_relative_freq[-1])
    
    # Вариационный ряд для ДСВ
    #
    # variation_list = enumerate(output_list)
    # print("enumerated")

    # Create data for emperical func
    data_for_emperical_func = []
    data_for_emperical_func.append((-math.inf, 0))
    data_for_emperical_func.append((min_values[0], 0))
    for el in zip(max_values, cumulative_relative_freq):
        data_for_emperical_func.append(el)
    data_for_emperical_func.append((math.inf, 1))
    print(data_for_emperical_func)

    # separating data in two columns
    xvalues = [ el[0] for el in data_for_emperical_func ]
    yvalues = [ el[1] for el in data_for_emperical_func ]

    # Равноинтервальным способом
    plt.hist(yvalues, label='Диаграмма построенная равноинтервальным способом')
    plt.show()
    # Равновероятностным спосбом
    values_for_hist = [ y / rounded_interval_length for y in yvalues ]
    plt.hist(values_for_hist)
    plt.show()
    plt.plot(xvalues, yvalues, label='Эмпирическая функция распределения')
    plt.show()

    pp_variation_list = enumerate([ round(x, 2)  for x in variation_list ], start=1)
    with open('output_1_nsv.csv' , 'w', newline = '') as csvfile:
        variationwriter = csv.writer(csvfile, delimiter=',',  dialect='excel')
        variationwriter.writerows(pp_variation_list)
        print('wrote')
        
main()
