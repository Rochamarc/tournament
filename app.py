import tkinter as tk

import locale

from controllers.players_controller import PlayersController
from controllers.clubs_controller import ClubsController

cc = ClubsController()
pc = PlayersController()

# Define a season variables
season = '2022'

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 

def format_value(value):
    return locale.format_string("%.2f", value, grouping=True)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Brazilian Football Clubs")

        # Label and listbox for clubs
        self.label = tk.Label(root, text="Select a Club:")
        self.label.pack(pady=10)

        self.club_listbox = tk.Listbox(root, width=90, height=40)
        self.club_listbox.pack(pady=10)

        self.players_listbox = None # tk.Listbox(root, width=90, height=40)
        # self.players_listbox.pack(pady=10)

        # Populate clubs
        self.populate_clubs()

        # Button to show players
        self.show_players_button = tk.Button(
            root, text="Squad Details", command=self.show_players
        )
        self.show_players_button.pack(pady=10)

        # Button to show Club details
        self.show_players_button = tk.Button(
            root, text="Club Details", command=self.show_club_details
        )
        self.show_players_button.pack(pady=10)


        self.players_details = None

    def show_club_details(self) -> None:
        return None
    
    def populate_clubs(self):
        """Show all the clubs names
        """

        serie_a, serie_b, serie_c = cc.select_serie_a_clubs(season), cc.select_serie_b_clubs(season), cc.select_serie_c_clubs(season)

        clubs = [ a[1] for a in serie_a ] + [ b[1] for b in serie_b ] + [ c[1] for c in serie_c ]

        for club in clubs:
            self.club_listbox.insert(tk.END, club)

    def show_players(self):
        """Show all players from a selected club
        """

        selected_index = self.club_listbox.curselection()

        if not selected_index:
            tk.messagebox.showinfo("Info", "Please select a club first!")
            return

        selected_club = self.club_listbox.get(selected_index)

        # select clubs players
        players = pc.select_players_by_club(selected_club, season)
        
        # add a copy of the total of club's players
        self.players_details = players.copy()

        # Open a new window for players
        players_window = tk.Toplevel(self.root)
        players_window.title(f"{selected_club} Squad")

        label = tk.Label(players_window, text=f"{selected_club} Squad:")
        label.pack(pady=10)

        self.players_listbox = tk.Listbox(players_window, width=90, height=40)
        self.players_listbox.pack(pady=10)


        for player in players:
            self.players_listbox.insert(tk.END, f"{player[2]} :: {player[0]}") 

        close_button = tk.Button(players_window, text="Show Player Details", command=self.show_player_details)
        close_button.pack(pady=10)

    def show_player_details(self):
        """Show details of a selected player
        """
        select_player = self.players_listbox.get(self.players_listbox.curselection()).split(' :: ')[-1]
        
        for player in self.players_details:
            if select_player == player[0]:
                select_player = player
        
        player_attributes = [
            "Name", "Nationality", "Position", "Birth Year", 
            "Height (m)", "Weight (kg)", "Foot", "Salary (R$)", 
            "Positioning", "Reflexes", "Diving", "Standing tackle", 
            "Physical", "Passing", "Dribbling", "Long shot", "Finishing", 
            "Current Club"
        ]                                                

        details_window = tk.Toplevel()
        details_window.title("Player Details")

        # Cria uma grade para os detalhes
        for i, attribute in enumerate(player_attributes):
            player_att = select_player[i]

            if attribute == "Salary (R$)":
                player_att = format_value(player_att)

            # Label para o campo (Key)
            tk.Label(details_window, text=f"{attribute}:", font=("Arial", 12, "bold"), anchor="w").grid(
                row=i, column=0, sticky="w", padx=10, pady=5
            )
            # Label para o valor (Value)
            tk.Label(details_window, text=str(player_att), font=("Arial", 12), anchor="w").grid(
                row=i, column=1, sticky="w", padx=10, pady=5
            )

        # Botão para fechar a janela
        tk.Button(
            details_window, text="Close", command=details_window.destroy, font=("Arial", 12)
        ).grid(row=len(player_attributes), column=0, columnspan=2, pady=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()