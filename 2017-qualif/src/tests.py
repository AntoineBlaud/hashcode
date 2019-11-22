from Objects import *
from Process import *

def test_server_score(io):
    server = io.cacheServers[0]
    video0 = io.videos[0]
    video1 = io.videos[1]
    video2 = io.videos[2]
    video3 = io.videos[3]
    video4 = io.videos[4]
    server.addVideo(video0)
    #server.addVideo(video3)
    server.addVideo(video4)

    server2 = io.cacheServers[1]
    server2.addVideo(video3)


    data = Data(io)
    process = Process(data)
    print(process.evalueServerScore(server))
    print(process.evalueServerScore(server2))

