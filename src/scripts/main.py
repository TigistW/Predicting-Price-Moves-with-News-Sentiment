from src.scripts.load_data import load_headlines, load_stock_data
from src.scripts.eda import headline_stats, publisher_frequency
from src.scripts.indicators import add_technical_indicators
from src.scripts.sentiment import apply_sentiment, average_daily_sentiment

if __name__ == "__main__":
    news_df = load_headlines()
    stock_df = load_stock_data("AAPL")

    print("Headline Stats:\n", headline_stats(news_df))
    print("Top Publishers:\n", publisher_frequency(news_df).head())

    stock_df = add_technical_indicators(stock_df)

    news_df = apply_sentiment(news_df)
    avg_sent = average_daily_sentiment(news_df)
    stock_df['Return'] = stock_df['Close'].pct_change()

    daily = stock_df.copy()
    daily['date'] = daily.index.date
    combined = daily.merge(avg_sent, left_on='date', right_index=True, how='inner')

    correlation = combined['Return'].corr(combined['sentiment'])
    print("Correlation between sentiment and returns:", correlation)
