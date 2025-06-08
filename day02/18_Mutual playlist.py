your_playlist = {
    "All I Want for Christmas is You",
    "Silent Night, Holy Night",
    "Star ng Pasko",
    "Pasko na Sinta Ko",
}

friend_playlist = {
    "Baby, It's Cold Outside",
    "All I Want for Christmas is You",
    "Kampana ng Simbahan",
    "Christmas Bonus",
}

print(your_playlist.union(friend_playlist))
print(your_playlist.intersection(friend_playlist))
print(your_playlist & friend_playlist)
print((your_playlist.symmetric_difference(friend_playlist)))


# Create a new playlist that combines all the songs