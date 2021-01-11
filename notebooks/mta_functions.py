# Create filtered list of top x ranked stations during timeframe
def topStations(input_dataframe, top_x):
    top_stations = set()

    for idx, row in input_dataframe.iterrows():
        top_stations |= set(row[row > 0].sort_values(ascending=False).head(top_x).index)

    return list(top_stations)