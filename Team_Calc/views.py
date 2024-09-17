import itertools
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

MAX_LINEUP = 5  # Max number of players in a lineup
MAX_SL_SUM = 23  # Maximum SL sum for the lineup

def generate_team_combos(team, x_ball_SL):
    possible_lineups = []
    
    # Generate all possible combinations of the team
    for comb in itertools.combinations(team, MAX_LINEUP):
        possible_lineups.append(comb)
    
    sl_restricted_lineups = []
    
    # Filter combinations by maximum SL sum
    for lineup in possible_lineups:
        total_sl = 0
        for player in lineup:
            total_sl += x_ball_SL[player]
        if total_sl <= MAX_SL_SUM:
            sl_restricted_lineups.append(lineup)
    
    # Sort lineups by the highest individual SL in descending order
    sorted_lineups = sorted(
        sl_restricted_lineups, 
        key=lambda lineup: max(x_ball_SL[player] for player in lineup),
        reverse=True
    )
    
    return sorted_lineups

def team_member_form(request):
    return render(request, 'player_form.html', {'player_range': range(1, 9)})

@csrf_exempt
def submit_team_members(request):
    if request.method == 'POST':
        # Store player data in session
        players = []
        eight_ball_SL = {}
        nine_ball_SL = {}
        
        for i in range(1, 9):
            name = request.POST.get(f'player{i}_name', '')
            eight_ball_sl = request.POST.get(f'player{i}_8ball', '')
            nine_ball_sl = request.POST.get(f'player{i}_9ball', '')

            if not name or not eight_ball_sl.isdigit() or not nine_ball_sl.isdigit():
                return JsonResponse({'success': False, 'message': 'Invalid input.'}, status=400)

            players.append(name)
            eight_ball_SL[name] = int(eight_ball_sl)
            nine_ball_SL[name] = int(nine_ball_sl)

        # Save to session
        request.session['players'] = players
        request.session['eight_ball_SL'] = eight_ball_SL
        request.session['nine_ball_SL'] = nine_ball_SL

        # Redirect to game type selection
        return redirect('game_selection')

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def game_selection(request):
    return render(request, 'game_selection.html')

@csrf_exempt
def generate_lineups(request):
    if request.method == 'POST':
        game_type = request.POST.get('game_type', '')
        
        # Retrieve data from session
        players = request.session.get('players', [])
        eight_ball_SL = request.session.get('eight_ball_SL', {})
        nine_ball_SL = request.session.get('nine_ball_SL', {})

        # Choose the appropriate SL dictionary
        if game_type == '8ball':
            lineups = generate_team_combos(players, eight_ball_SL)
            sl_dict = eight_ball_SL
        elif game_type == '9ball':
            lineups = generate_team_combos(players, nine_ball_SL)
            sl_dict = nine_ball_SL
        else:
            return JsonResponse({'success': False, 'message': 'Invalid game type.'}, status=400)

        # Add SL to the players in the lineup
        lineup_with_sl = []
        for lineup in lineups:
            lineup_with_sl.append([(player, sl_dict[player]) for player in lineup])

        # Display the results
        return render(request, 'lineup_results.html', {
            'lineups': lineup_with_sl,
            'game_type': game_type
        })

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)