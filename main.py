from AI import AI

PLAYABLE = ["p", "f", "c"]
WIN_CASES = [["p", "f"], ["f", "c"], ["c", "p"]]

points = {"Player": 0, "AI": 0}
current_round = 1

# Results obtained after training AI
ai = AI([[0.39158207658268585, 0.13069492737301114, 0.39158207658268585, 0.011012860920175616],
         [0.009369458570809064, 0.7809103669914822, 0.7809103669914822]])


def determine_winner(player, ai):
    if player == ai:
        return None
    elif [ai, player] in WIN_CASES:
        return "Player"
    return "AI"


while True:
    print(f"Round {current_round}!")
    player_input = input("Pierre, feuille ou ciseau ? [p/f/c] : ").lower()

    if not player_input in PLAYABLE:
        print("Veuillez entrer une réponse valide!\n")
        continue

    ai_input = ai.act()

    print("Ce round ont été joué :", " et ".join([player_input, ai_input]))
    ai.last_player_action = player_input

    winner = determine_winner(player_input, ai_input)
    if not winner:
        print("Egalité!")
    else:
        print(f"{winner} a remporté le tour!")
        points[winner] += 1
    print(f"Points -> Pl: {points['Player']} || AI: {points['AI']}", end="\n" * 2)

    current_round += 1
