import pandas as pd
import quandl
import pickle
api_key = open('apiKey.txt', 'r').read()


def state_list():
    fiddy_states = pd.read_html(
        'https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        print(query)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    return df


def mortgage30():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.columns = ['m30']
    df = df.resample('1D')
    df = df.resample('M').mean()
    return df


def stocks():
    df = quandl.get("WFE/INDEXES_BSEINDIALIMITEDSPBSE", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.columns = ['stocks']
    return df


def sp500():
    df = pd.read_csv('AS-SP500.csv')
    df.index = pd.to_datetime(df.date, format='%Y-%m-%d')
    df.resample('M').mean()
    df["close"] = (df["close"] - df["close"][0]) / df["close"][0] * 100.0
    df.rename(columns={'close': 'sp500'}, inplace=True)
    df = df['sp500']
    return df


def gdp():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M').mean()
    df.rename(columns={'Value': 'GDP'}, inplace=True)
    df = df['GDP']
    return df


def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (
        df["Unemployment Rate"] -
        df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df = df.resample('1D').mean()
    df = df.resample('M').mean()
    return df

def women_emp():
    df = quandl.get("BLSE/CEU0500000010", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.columns = ['women_emp']
    return df