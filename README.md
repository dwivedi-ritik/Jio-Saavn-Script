# Jio-Saavn-Script

Try just installing axios and
node saavn.js {permalink} album/song

eg - 
https://www.jiosaavn.com/song/afsana/EyoaVTZqAGU
and command will be like this
node saavn.js EyoaVTZqAGU song
This is faster than the python one

Require- Perma link of a song or album 

Make sure you pass the right link to right class //This is album , you can see in original url

eg - normal link ="https://www.jiosaavn.com/album/dil-bechara/OV26eogqCTQ_"
     perma_link = "OV26eogqCTQ_" //Last characters of URL

https://www.jiosaavn.com/song/taare-ginn/GTA0dzkdWEQ - This is song url and its perma_link is = "GTA0dzkdWEQ"

Feautures 

SONG CLASS-

1- Get the details of song in dictionary format(including all the details such as album/artists/img url/song id/etc...)

2- Get the download link of Song

3- Get lyrics of song if available

AlBUM CLASS -

1- Get the details of all the songs in album in json format(including all the details such as album/artists/img url/song id/etc...)

2- Get download links of all the songs

3- Download all the songs of album into desired path

4- Downloading done using multithreading(Faster than normal process)

I will include more features in futures and unofficial api too <3
