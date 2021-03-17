# michaelpeterswa
# espnstats.py

class Team:
    opp_ppg_mult = 1

    def __init__(self, name):
        self.name = name

    def set_espn_stats(self, opp_ppg, vs_t25, bpi_rank, vs_conference, ppg, vs_overall):
        # ESPN TC Stats
        self.opp_ppg = opp_ppg
        self.vs_t25 = vs_t25
        self.bpi_rank = bpi_rank
        self.vs_conference = vs_conference
        self.ppg = ppg
        self.vs_overall = vs_overall

    def set_team_rankings(self, decision_tree, seed_comparison, power_rating, similar_games):
        # TeamRankings Game Predictor
        self.decision_tree = decision_tree
        self.seed_comparison = seed_comparison
        self.power_rating = power_rating
        self.similar_games = similar_games

    def set_raw_score(self, val):
        self.raw_score = val

    def pretty_print(self):
        print(f'Team name:\t\t\t{self.name}')
        print("--------------------------------------")
        print(f'Points per Game:\t\t{self.ppg} pts.')
        print(f'Opponent Points per Game:\t{self.opp_ppg} pts.')
        print(f'Versus Overall:\t\t\t{self.vs_overall}')
        print(f'Versus Top-25:\t\t\t{self.vs_t25}')
        print(f'Versus Conference:\t\t{self.vs_conference}')
        print(f'Basketball Power Index:\t\t{self.bpi_rank}')
        print(f'Decison Tree Win %:\t\t{self.decision_tree}%')
        print(f'Seed Comparison Win %:\t\t{self.seed_comparison}%')
        print(f'Power Rating Win %:\t\t{self.power_rating}%')
        print(f'Similar Games Win %:\t\t{self.similar_games}%')
        print()

    def calculate_raw_score(self):
        
        # multipliers
        ppg_mult = 1
        opp_ppg_mult = 1
        vs_overall_mult = 1
        vs_t25_mult = 1
        vs_conference_mult = 1
        bpi_rank_mult = 1
        decision_tree_mult = 1
        seed_comparison_mult = 1
        power_rating_mult = 1
        similar_games_mult = 1

        # flip weighting to favor lower scores
        self.opp_ppg = 100 - self.opp_ppg
        
        self.vs_overall = vs_calc(self.vs_overall)
        self.vs_t25 = vs_calc(self.vs_t25)
        self.vs_conference = vs_calc(self.vs_conference)
        
        # flip weighting to favor lower scores
        self.bpi_rank = 100 - self.bpi_rank
        
        score = ((self.ppg * ppg_mult) + 
                (self.opp_ppg * opp_ppg_mult) +
                (self.vs_overall * vs_overall_mult) +
                (self.vs_t25 * vs_t25_mult) +
                (self.vs_conference * vs_conference_mult) +
                (self.bpi_rank * bpi_rank_mult) +
                (self.decision_tree * decision_tree_mult) +
                (self.seed_comparison * seed_comparison_mult) +
                (self.power_rating * power_rating_mult) +
                (self.similar_games * similar_games_mult))

        return score


def vs_calc(vs):
        vs = vs.split('-')
        vs = [int(i) for i in vs] 
        vs = (int(vs[0]) / (sum(vs))) * 100
        return vs

def calculate_winner(team1, team2):
    print(f"\nCalculating winner between {team1.name} and {team2.name}...\n")
    team1.pretty_print()
    team2.pretty_print()

    team1.set_raw_score(team1.calculate_raw_score())
    team2.set_raw_score(team2.calculate_raw_score())
    print(f"{team1.name} raw score: {team1.raw_score}")
    print(f"{team2.name} raw score: {team2.raw_score}\n")

    if team2.raw_score < team1.raw_score:
        print(f"{team1.name} is the Winner!")
    else:
        print(f"{team2.name} is the Winner!")
    print()

if __name__ == "__main__":

    team_one = Team("OU")
    team_two = Team("MIZ")

    # opp_ppg, vs_t25, bpi_rank, vs_conference, ppg
    team_one.set_espn_stats(69.2, "5-7", 30, "9-8", 74.8, "15-10")
    # decision_tree, seed_comparison, power_rating, similar_games
    team_one.set_team_rankings(66, 51, 53, 38)

    # opp_ppg, vs_t25, bpi_rank, vs_conference, ppg
    team_two.set_espn_stats(69.2, "4-2", 50, "8-8", 73.6, "16-9")
    # decision_tree, seed_comparison, power_rating, similar_games
    team_two.set_team_rankings(34, 49, 47, 62)

    calculate_winner(team_one, team_two)