def data_type(df):
    try:
        df["followers"] = df["followers"].astype('int')
        df['popularity'] = df['popularity'].astype('int')
    except Exception:
        pass

    try:
        df['release_date'] = df['release_date'].astype('datetime64')
        df['total_tracks'] = df['total_tracks'].astype('int')
    except Exception:
        pass

    try:
        df['duration_ms'] = df['duration_ms'].astype('datetime64')
        df['explicit'] = df['explicit'].astype('int')
        df['disc_number'] = df['disc_number'].astype('int')
    except Exception:
        pass

    try:
        df['danceability'] = df['danceability'].astype('datetime64')
        df['energy'] = df['energy'].astype('int')
        df['instrumentalness'] = df['instrumentalness'].astype('int')
        df['liveness'] = df['liveness'].astype('datetime64')
        df['loudness'] = df['loudness'].astype('int')
        df['speechiness'] = df['speechiness'].astype('int')
        df['tempo'] = df['tempo'].astype('int')
        df['valence'] = df['valence'].astype('int')
    except Exception:
        pass
