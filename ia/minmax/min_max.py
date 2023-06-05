# Return true for white and false for black
def joueur(etat):
    return etat.turn

def actions(etat):
    return etat.legal_moves

def jouer(etat, coup):
    etat.push(coup)

def is_ended(etat):
    return etat.is_game_over()

# Algorithme sans aucune optimisation, temps infinie pour les échecs
def minmax_infinite(etat, eval):
    if is_ended(etat):
        return eval(etat)
    if joueur(etat):
        valeur = float('-inf')
        for move in actions(etat):
            jouer(etat, move)
            valeur = max(valeur, minmax_infinite(etat, eval))
            etat.pop()
        return valeur
    else:
        valeur = float('inf')
        for move in actions(etat):
            jouer(etat, move)
            valeur = min(valeur, minmax_infinite(etat, eval))
            etat.pop()
        return valeur

def minmax_depth(etat, depth, eval):
    if depth == 0 or is_ended(etat):
        return eval(etat)
    if joueur(etat):
        valeur = float('-inf')
        for move in actions(etat):
            jouer(etat, move)
            valeur = max(valeur, minmax_depth(etat, depth - 1, eval))
            etat.pop()
        return valeur
    else:
        valeur = float('inf')
        for move in actions(etat):
            jouer(etat, move)
            valeur = min(valeur, minmax_depth(etat, depth - 1, eval))
            etat.pop()
        return valeur

# Evalue la position avec une profondeur depth, si le résultat est positif la position est avantageuse pour les blanc, si néative pour les noirs, si 0 équilibrée
def minimax_alpha_beta(board, depth, eval, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return eval(board)
    moves = board.legal_moves
    if board.turn:
        value = -float('inf')
        for move in moves:
            board.push(move)
            value = max(value, minimax_alpha_beta(board, depth - 1, eval, alpha, beta))
            board.pop()
            alpha = max(alpha, value)
            if alpha > beta:
                break  # Élagage beta
        return value
    else:
        value = float('inf')
        for move in moves:
            board.push(move)
            value = min(value, minimax_alpha_beta(board, depth - 1, eval, alpha, beta))
            board.pop()
            beta = min(beta, value)
            if alpha > beta:
                break  # Élagage alpha
        return value


def find_best_move(board, depth, evaluate_board, minimax):
    best_move = None
    max_score = -float('inf')

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth, evaluate_board)
        board.pop()

        if score > max_score:
            max_score = score
            best_move = move

    return best_move
