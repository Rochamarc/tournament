#include <sqlite3.h>
#include <stdio.h>

int main(void) {
	sqlite3 *db;
    char *err_msg = 0;
    
    int rc = sqlite3_open("database.db", &db);

	if (rc != SQLITE_OK) {
		// Catch an error opening
        	
		fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        	sqlite3_close(db);

        	return 1;
    	}

	char *sql = "DROP TABLE IF EXISTS Players;"
                "CREATE TABLE Players(id INTEGER PRIMARY KEY, name TEXT, nationality TEXT, age INT, overall INT, current_club TEXT, position TEXT, market_value INT, salary INT, height TEXT, weight TEXT, foot TEXT);"
                "DROP TABLE IF EXISTS Clubs;"
                "CREATE TABLE Clubs(id INTEGER PRIMARY KEY, name TEXT, country TEXT, state TEXT, coeff INT, clubclass TEXT, total_budget INT, salary_budget INT);"
                "DROP TABLE IF EXISTS Coaches;"
                "CREATE TABLE Coaches(id INTEGER PRIMARY KEY, name TEXT, nationality TEXT, age INT, formation TEXT, play_mode TEXT, current_club TEXT);"
                "DROP TABLE IF EXISTS Stadiums;"
                "CREATE TABLE Stadiums(id INTEGER PRIMARY KEY, name TEXT, location TEXT, capacity INT, club_owner TEXT);"
                "DROP TABLE IF EXISTS Games;"
                "CREATE TABLE Games(id INTEGER PRIMARY KEY, competition TEXT, season TEXT, hour TEXT, home_team TEXT, away_team TEXT, score TEXT, stadium TEXT, home_shots INT, home_shots_on_target INT, home_fouls INT, home_tackles INT, home_saves INT, home_ball_possession INT, home_offsides INT, home_freekicks INT, away_shots INT, away_shots_on_target INT, away_fouls INT, away_tackles INT, away_saves INT, away_ball_possession INT, away_offsides INT, away_freekicks INT);"
                "DROP TABLE IF EXISTS Champions;"
                "CREATE TABLE Champions(id INTEGER PRIMARY KEY, competetition TEXT, club TEXT, season TEXT);";
    
    
    rc = sqlite3_exec(db, sql, 0, 0, &err_msg);

    if (rc != SQLITE_OK ) {
		// Catch a error on insertion
		//
        	fprintf(stderr, "SQL error: %s\n", err_msg);

        	sqlite3_free(err_msg);
        	sqlite3_close(db);

        	return 1;
    }

    sqlite3_close(db);

    return 0;
}

