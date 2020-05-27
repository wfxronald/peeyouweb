from django.shortcuts import render
from level.models import SongsCleared, User, TitleCard
from statistics import mean
from re import sub, search


def level_detail(request, level):
	if level < 20 or level > 28:
		return render(request, "invalid.html")

	users = User.objects.all()
	song_for_every_user = {}

	for user in users:
		chatid = user.chatid
		songs = SongsCleared.objects.filter(level=level, chatid=chatid)
		for index in range(1, len(songs)+1):
			song = songs[index-1].song
			if song in song_for_every_user:
				song_for_every_user[song].append(index)
			else: 
				song_for_every_user[song] = [index]

	tuple_of_songs = []
	for song in song_for_every_user:
		clean_title = search('\*(.+?)\*', song).group(1)
		clean_cut = search('_\((.+?)\)_', song).group(1)
		image = TitleCard.objects.filter(song=clean_title, cut=clean_cut).first().image
		sanitised_song_string = sub('[*_]', '', song)
		average_song_rank = round(mean(song_for_every_user[song]), 2)
		tuple_of_songs.append((sanitised_song_string, average_song_rank, image))
	tuple_of_songs.sort(key = lambda x : x[1], reverse=True)

	context = {
		"tuple_of_songs": tuple_of_songs,
		"level": level,
	}
	
	return render(request, "level_detail.html", context)
