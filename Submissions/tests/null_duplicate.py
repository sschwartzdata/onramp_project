
def null_count(df_list):
    for df, name in df_list:
        print(name + "table NULLS : ")
        print(df.isna().sum())


def duplicate_count(df_list):
    for df, name in df_list:
        print(name + "table duplicates : ")
        print(df.duplicated().sum())
