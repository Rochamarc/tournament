HOST=0.0.0.0
PORT=5503
DATABASE=TournamentAnalysis
USER=MainUser
PASSWORD=MainPassword
DATABASE=TournamentAnalysis

mysql -h $HOST -P $PORT -u $USER --password=$PASSWORD $DATABASE < ./database/tournament_analysis/main.sql