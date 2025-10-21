import requests
import pandas as pd
from datetime import datetime
from metrics.conf import HEADERS, REPO_URL

def get_all(url):
    results = []

    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

        results.extend(response.json())

        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    return results

def get_commits():
    url = f"{REPO_URL}/commits"
    return get_all(url)


def get_commits_per_day():
    commits = get_commits()
    commit_dates = [commit['commit']['author']['date'] for commit in commits]
    commit_dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') for date in commit_dates]

    df_commits = pd.DataFrame({'date': commit_dates})
    df_commits['day'] = df_commits['date'].dt.date
    commits_per_day = df_commits.groupby('day').size().reset_index(name='commits')
    return commits_per_day
