__author__ = 'chance'

import csv
import datetime
import sys

sys.path.append('./modules')
import time
from modules import sqldb, push, requestor
import pandas as pd

SEASON = int((datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y'))
STATS_YEAR = SEASON
fdb = sqldb.DB('Football.db')
# request_instance = espn_request.Request()
request_instance = requestor.Request()
request_instance.year = SEASON
print(request_instance.year)
REFRESH = True
push_instance = push.Push(calling_function="create_matchup_schedule")
SPORT_ID = "ffl"  # mlb: flb, nfl: ffl
API_BASE = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/{SPORT_ID}/seasons"


def get_leagues():
    return fdb.query(f"select leagueId, leagueAbbr, Year from Leagues where Year = {SEASON}")


def get_matchup_schedule(league_id):
    # url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{SEASON}/segments/0/leagues/{league_id}?view=mMatchupScore"
    # matchup_schedule = request_instance.make_request(url=url)
    url = f"{API_BASE}/{SEASON}/segments/0/leagues/{league_id}?view=mMatchupScore"
    matchup_schedule = request_instance.make_request(url=url, sleep_int=0,
                                                     calling_function="fantasy: get_matchup_schedule")
    return matchup_schedule


def get_data(league_id, league_name):
    data = {'matchup_schedule': get_matchup_schedule(league_id), 'league_id': league_id,
            'league_name': league_name, 'year': SEASON}
    return data


def process_data(data):
    file_name = './data/matchup_schedule.csv'
    table_name = "MatchupSchedule"
    schedule = data['matchup_schedule']['schedule']
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file)
        columns = ['LeagueID', 'League', 'Week', 'HomeTeam', 'AwayTeam']
        csv_writer.writerow(columns)
        for matchup in schedule:
            home_team = matchup['home']['teamId']
            away_team = matchup['away']['teamId']
            league = data['league_name']
            league_id = data['league_id']
            week = matchup['matchupPeriodId']
            row = [league_id, league, week, home_team, away_team]
            print(row)
            if len(row) != len(columns):
                raise Exception(f"Number of items in row variable {len(row)} is not equal to number of columns defined "
                                f"in variable columns {len(columns)}")

            csv_writer.writerow([league_id, league, week, home_team, away_team])

    df = pd.read_csv(file_name)
    print(df)
    delcmd = f"delete from {table_name} where league = '{league}'"
    fdb.delete(delcmd, register=True)
    fdb.df_to_sql(df, table_name)


def process_league(league):
    league_id = league['leagueID']
    league_name = league['leagueAbbr']
    data = get_data(league_id, league_name)
    ######################
    process_data(data)
    ######################
    data.clear()
    print("\n")
    time.sleep(4)


def main():
    leagues = get_leagues()
    [process_league(league) for league in leagues]
    fdb.close()
    print("Done")


if __name__ == "__main__":
    main()
