class Teams():

    def __init__(self, team):
        self.team = team
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        elif self.score == other.score:
            return self.team < other.team

    @property
    def mp(self):
        return self.draws + self.losses + self.wins

    @property
    def score(self):
        return self.draws + (self.wins * 3)

def tally(rows):
    team_object = {}
    for row in rows:
        primary_team, secondary_team, result = row.split(";")
        for team in [primary_team, secondary_team]:
            if team not in team_object:
                team_object[team] = Teams(team)

        if result == "win":
            team_object[primary_team].wins += 1
            team_object[secondary_team].losses += 1

        elif result == "loss":
            team_object[primary_team].losses += 1
            team_object[secondary_team].wins += 1

        elif result == "draw":
            team_object[primary_team].draws += 1
            team_object[secondary_team].draws += 1
    
    print_table = [f"{'Team'.ljust(31)}|{'MP'.rjust(3)} |{'W'.rjust(3)} |{'D'.rjust(3)} |{'L'.rjust(3)} |{'P'.rjust(3)}"]
    
    print_order = sorted(team_object.items(), key=lambda x: x[1])

    for team in print_order:
        print_table.append(f"{team[0].ljust(31)}|{str(team[1].mp).rjust(3)} |{str(team[1].wins).rjust(3)} |{str(team[1].draws).rjust(3)} |{str(team[1].losses).rjust(3)} |{str(team[1].score).rjust(3)}")
    return print_table