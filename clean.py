import pandas as pd

def clean_data(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df1 = df1.rename(columns={'respondent_id': 'id'})
    merge_df = pd.merge(df1, df2, on='id')
    cleaned_df = merge_df.dropna()
    s_df = cleaned_df[~cleaned_df['job'].str.contains('Insurance')]
    ss_df = s_df[~cleaned_df['job'].str.contains('insurance')]
    return ss_df


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Path to respondent_contact.csv file')
    parser.add_argument('input2', help='Path to respondent_other.csv file')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean_data(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)
