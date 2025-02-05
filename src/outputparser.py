import statistics


def create_output_line(parameter_dict, print_parameters, runtimes):
    result = ""
    for print_parameter in print_parameters:
        result += parameter_dict[print_parameter]
        result += ","
    if len(result) >= 1:  # remove last comma if it exists
        result = result[:-1]
    result += ";" + str(statistics.median(runtimes)) + ";" + str(statistics.mean(runtimes)) \
              + ";" + str(min(runtimes)) + ";" + str(max(runtimes)) + "\n"
    return result


def create_raw_output(parameter_dict, print_parameters, runtimes):
    result = ""
    for printParameter in print_parameters:
        result += parameter_dict[printParameter]
        result += ","
    if len(result) >= 1:  # remove last comma if it exists
        result = result[:-1]
    result += ";"
    for runtime in runtimes:
        result += str(runtime) + ";"
    result = result[:-1] + "\n"
    return result
