from django.shortcuts import render, redirect
from .models import Player, Team
from .forms import PlayerForm


#---------------------------------------- PAGES -----------------------------------------------------
def home(request):
    return render(request, 'home.html')

def feed(request):
    return render(request, 'feed.html')

def squad(request):
    players = Player.objects.all()
    return render(request,'squad.html', {'players': players})

#---------------------------------------------------------------
def add_player(request):                
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            # Save the new player
            form.save()
            # Redirect to the squad page or wherever you want
            return redirect('squad')
    else:
        # Initialize the form with an empty instance
        form = PlayerForm()

    return render(request, 'add_player.html', {'form': form})

