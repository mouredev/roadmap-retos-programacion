import pandas as pd


def filter_active(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.status == 'active']


def choose_three_random_users(df: pd.DataFrame) -> pd.DataFrame:
    return df[['id', 'email']].sample(n=3)


if __name__ == "__main__":
    df = pd.read_csv('users.csv')
    active_users = filter_active(df)
    winners = choose_three_random_users(active_users)
    print(winners)
