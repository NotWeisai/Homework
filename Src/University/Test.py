from repository import get_user_results

for result in get_user_results('Алиса'):
    print(result['score'], result['played_at'])