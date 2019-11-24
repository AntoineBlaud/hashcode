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


def test_knapstack():
    size = 200
    val = np.asarray([random.randint(40, size) for i in range(0, size)])
    wt = np.asarray([random.randint(40, size) for i in range(0, size)])
    W = 6000
    n = len(val)
    #print(val)
    #print(wt)
    a = Process.knapSack(W, wt, val, n)
    print(a)