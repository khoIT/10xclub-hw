import pandas as pd
import requests

def loadFile(source, file_name):
    localroot = "/tmp/"
    response = requests.get(source + file_name)
    print("Downloading and Saving " + file_name)
    with open(localroot + file_name, 'wb') as f:
        f.write(response.content)
        dfData = pd.read_csv(localroot + file_name, sep=",")
    return dfData

def join_data(left_data, right_data):
    return left_data.join(right_data)

def filter_data(dataframe, columns, filter):
    """
    Return a new dataframe with all rows filtered by filter and selected_columns.
    Filter should be a string in format "<Column_name> <comparision_operator> <value>". In which, column_name,
    operator and value must be all separated by ONE SPACE.
    Ex: "Insight_Score == 2.5"
    Columns should be a list of column names desired.
    """
    # 0. Check columns list
    if not columns or type(columns) != list:
        dataframe = dataframe
    else:
        dataframe = dataframe[columns]

    # 1. Check and process filter
    column, operand, value_string = filter.split(" ")
    import operator
    switcher = {
        "==": operator.eq,
        ">=": operator.ge,
        "<=": operator.le,
        "<": operator.lt,
        ">": operator.gt,
    }
    compare = switcher.get(operand, "nothing")
    if compare == "nothing":
        return "Invalid syntax in filter"

    return dataframe.loc[compare(dataframe[column], float(value_string))]

if __name__ == "__main__":
    data = loadFile("https://storage.googleapis.com/coderpad/", "data.csv")
    map = loadFile("https://storage.googleapis.com/coderpad/", "maping.csv")
    filtered_df = filter_data(data, ['Period','Insight_Score','Country','Industry','Product_Code'], 'Insight_Score > 2.5')
    joined_df = join_data(filtered_df, map)

    # detect anomalies in Insight_Score using standard deviations
    outliers = joined_df[['Period','Insight_Score']].groupby(['Period']).transform(lambda group: (group - group.mean()).abs().div(group.std())) > 1.0
    new_df = joined_df[outliers.Insight_Score==False]

    min_date = new_df.loc[new_df.groupby(['Industry'])['Insight_Score'].idxmin()]
    max_date = new_df.loc[new_df.groupby(['Industry'])['Insight_Score'].idxmax()]
    final_df = min_date.append(max_date)
    final_df[['Industry','Period','Insight_Score']].sort_values(by=['Industry']).to_csv('datanew.csv')

    # Find correlation
    min_date = min_date[['Industry','Insight_Score']].set_index('Industry')
    min_date = min_date[['Industry','Insight_Score']].set_index('Industry')
