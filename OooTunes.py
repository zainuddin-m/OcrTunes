myfile = open("SongsFile.txt","r")
Songs = []
Artist = []
Genre = []
SongLength = []
fullsonglist = []

for line in myfile:
    line=line.strip("\n")
    line=line.split(",")
    line[3]=int(line[3])
    Songs.append(line[0])
    Artist.append(line[1])
    Genre.append(line[2])
    SongLength.append(line[3])
    fullsonglist.append(line)
    
    

def artist():
    #print(Artist)
    print("Song Artists: \n1.Ed Sheeran \n2.Justin Bieber \n3.Mozarty \n4.Logic \n5.KSL")
    condition3 = True
    while condition3 == True:
        Userartist = input("Please enter your favourite artist:")
        if Userartist.isdigit():
            Userartist = int(Userartist)
            if 0<Userartist<=5:
                print(" ")
                condition3 = False
            else:
                print("Please enter a number from 1-5")
        else:
            print("Please enter a number from 1-5")

    

def genre():
    print("Song Genres: \n1.Pop \n2.Jazz \n3.Rap \n4.Hip-hop \n5.Reggae")
    condition1 = True
    while condition1 == True:
        Usergenre = input("Please enter your favourite genre:")
        if Usergenre.isdigit():
            Usergenre = int(Usergenre)
            if 0<Usergenre<=5:
                print(" ")
                condition1 = False
            else:
                print("Please enter a number from 1-5")
        else:
            print("Please enter a number from 1-5")
    
print("1:User")
print("2:Creator")
condition0 = True
while condition0 ==True:
    creatororuser = input("Are you a user or creator. Please enter 1 or 2")
    if creatororuser == "1":
        Name = input("What is your name?")
        DoB = input("What is your date of birth?")
        print(" ")
        artist()
        genre()

        condition1 = True
        while condition1 ==True:
            print("1:Edit Artist")
            print("2:Edit Genre")
            print("3:View Profile")
            print("4:Display Alphabetically sorted song list")
            print("5:Create,View or Save Playlists")
            print("6:Automatically generate a playlist")
            print("7:Exit")
            choice2 = input("Please enter 1,2,3,4,5,6 or 7:")
            if choice2 =="1":
                artist()
                condition1 = True
            elif choice2=="2":
                genre() 
                condition1 = True
            elif choice2 =="3":
                print("Your name is:",Name)
                print("Your Date Of Birth is:",DoB)
                print(" ")
                condition1 = True
            elif choice2 =="4":
                print("The Alphabetically sorted songs:")
                fullsonglist.sort()
                print(fullsonglist)
                '''
                Playlist_of_timelimit = []
                Timelimit = int(input("Please enter a time limit:")
                Playlist_of_timelimit.append(SongsLength<Timelimit)
                print(Playlist_of_timelimit)

                Playlist_of_genre = []
                Genre2 = input("Please enter a genre:")
                Playlist_of_genre.append(Songs,in,Genre2)
                print(Playlist_of_genre)

                Playlist_of_artist = []
                Artist2 = input("Please enter an artist:")
                Playlist_of_artist.append(Songs, in,Artist2)
                print(Playlist_of_artist)
                artist_playlist.write(Playlist_of_artist)'''
                condition1 = True
            elif choice2 =="5":
                print("1.Create Playlist")
                print("2.View Playlist")
                print("3.Save Playlists")
                choice3 = input("Please enter what you would like to do:")
                if choice3 =="1":
                    print("Create Mode")
                elif choice3 =="2":
                    print("Playlist 1:",fullsonglist)
                elif choice3 =="3":
                    print("Writing to a file:")
                else:
                    print("Please enter a number from 1-3")
            elif choice2 =="6":
                condition5 = True
                while condition5 == True:
                    timelimit = input("Please enter a timelimit:")
                    if timelimit.isdigit():
                        condition5 = False
                    else:
                        print("Please enter a number only")
                timelimit = int(timelimit)
                timelimit = timelimit * 60
                condition6 = True
                position = 0
                position = int(position)
                playlist1=[]
                totaltime = 0
                totaltime = int(totaltime)
                position1 = 0
                #position1 = int(position1)
                while condition6 ==True:
                    position1 = fullsonglist[position][3]
                    playlist1 = playlist1.append(fullsonglist[position][3])
                    print(playlist1)
                    #position1 = (playlist1[position][3])
                    totaltime = (fullsonglist[position][3])
                    if totaltime >timelimit:
                        #totaltime = (totaltime) - (position)                        
                        condition6 = False
                    else:
                        position = position + 1
                        

            elif choice2 =="7":
                quit()
            else:
                print("Please enter only 1,2,3,4,5 or 6")

        #Rearrange songs[ ] in alphabetical order	
        #Rearrange songlength[] according to songs[]

        condition0 = False       

    elif creatororuser == "2":
        print("CREATOR MODE")
        '''print("All the genres are:", Genre)
        SongLength.split(",")
        Mean = (SongLength) + (SongLength.index)
        Mean = Mean/len(SongLength)'''
        condition0 = False
    else:
        print("Please enter only 1 or 2")

myfile.close()
