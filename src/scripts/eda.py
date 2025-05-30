def headline_stats(df):
    df['headline_len'] = df['headline'].apply(len)
    return df['headline_len'].describe()

def publisher_frequency(df):
    return df['publisher'].value_counts()

def time_distribution(df):
    df['hour'] = df['date'].dt.hour
    return df['hour'].value_counts().sort_index()

def plot_headline_length(df, save_path='outputs/figures/headline_length.png'):
    import matplotlib.pyplot as plt
    df['headline'].str.len().hist(bins=20)
    plt.title('Headline Length Distribution')
    plt.savefig(save_path)
