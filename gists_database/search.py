from .models import Gist

def search_gists(db_connection, **kwargs):
    if not kwargs:
        query = 'SELECT * FROM gists'
    if 'github_id' in kwargs:
        query = 'SELECT * FROM gists WHERE github_id = :github_id'
    if 'created_at' in kwargs:
        query = 'SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)'
        
    gists = db_connection.execute(query, kwargs)
    results = []
    for gist in gists:
        results.append(Gist(gist))
    return results
