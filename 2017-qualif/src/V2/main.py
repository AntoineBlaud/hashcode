import sys
import os
import time
import argparse
import re
from copy import copy
import pulp
from functools import reduce
import pickle
import multiprocessing
import random
import datetime
import tqdm
import warnings
warnings.filterwarnings("ignore")
######################################################################################
# import line_profiler
# import atexit
# profile = line_profiler.LineProfiler()
# atexit.register(profile.print_stats)
######################################################################################


def count_requested_video(endpoint):
    request = 0
    for k, v in endpoint.items():
        request += v
    return request


def sort_server_per_request_number(endpointsLatencyCache, endpointsVideosRequest, cacheN):

    endpointN = len(endpointsLatencyCache)
    endpointsRequestN = {}
    cacheRequests = {i: 0 for i in range(cacheN)}
    for i in range(len(endpointsVideosRequest)):
        endpoint = endpointsVideosRequest[i]
        endpointsRequestN[i] = count_requested_video(endpoint)

    for i in range(endpointN):
        endpoint = endpointsLatencyCache[i]
        for k in endpoint.keys():
            cacheRequests[k] += endpointsRequestN[i]

    # {cache 3: 4000, cache 1: 3500, ....}
    cacheRequests = sorted(cacheRequests.items(),key=lambda t: t[1], reverse=True)
    return cacheRequests


def endpoint_connected_to_cache(endpointsLatencyCache, cache, endpoint):
    return cache in endpointsLatencyCache[endpoint]


def evaluateVideosPoints(endpointsLatencyCache, endpointsVideosRequest, endpointsLatencyDataCenter, endpointsVideoLatency, videosN, cache):
    videosPoints = {i: 0 for i in range(videosN)}
    tempEndpointsVideoLatency = {i:{} for i in range(endpointsN)}
    for video in range(videosN):
        for endpoint in range(len(endpointsVideosRequest)):
            videosRequest = endpointsVideosRequest[endpoint]
            if(video in videosRequest):
                if(endpoint_connected_to_cache(endpointsLatencyCache, cache, endpoint)):
                    points = endpointsLatencyDataCenter[endpoint] - endpointsLatencyCache[endpoint][cache]
                    if(endpoint in endpointsVideoLatency and video in endpointsVideoLatency[endpoint]):
                        if(points > endpointsVideoLatency[endpoint][video]):
                            videosPoints[video] += (points) * videosRequest[video]
                            tempEndpointsVideoLatency[endpoint][video] = points
                    else:
                        videosPoints[video] += (points)*videosRequest[video]
                        tempEndpointsVideoLatency[endpoint][video] = points

    return videosPoints, tempEndpointsVideoLatency


def knapstack(value,size,cacheSize):
    prob = pulp.LpProblem("Server", pulp.LpMaximize)
    videos = pulp.LpVariable.dicts("videos", [i for i in range(len(value))], lowBound=0, upBound=1, cat=pulp.LpInteger)
    prob += pulp.lpSum(videos[i]*value[i] for i in range(len(value)))
    prob += pulp.lpSum(videos[i]*value[i] for i in range(len(value)))
    prob += pulp.lpSum(videos[i]*size[i] for i in range(len(value))) <= cacheSize
    prob.solve()
    results = []
    for k, v in videos.items():
        if(pulp.value(v) == 1):
            results.append(k)
    return results
        





def solve(videosSize,endpointsLatencyCache, endpointsVideosRequest, endpointsLatencyDataCenter,  cachesSortedByRequestsNumber,videosN, endpointsN, cacheN,cacheSize):
    endpointsVideoLatency = {i:{} for i in range(endpointsN)}
    caches = {i:[] for i in range(cacheN)}
    for (cache,r) in tqdm.tqdm(cachesSortedByRequestsNumber):
        videoPoints,tempEndpointsVideoLatency = evaluateVideosPoints(endpointsLatencyCache,endpointsVideosRequest,endpointsLatencyDataCenter,endpointsVideoLatency,videosN,cache)
        videosToPutIn = knapstack(videoPoints,videosSize,cacheSize)
        if(len(videosToPutIn)>0):
            caches[cache] = videosToPutIn

            for endpoint,dictio in tempEndpointsVideoLatency.items():
                for video,points in dictio.items():
                    if(video in caches[cache]):
                        endpointsVideoLatency[endpoint][video] = points
        else:
            del caches[cache] 
    return caches

        



if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2017-qualif\\qualification_round_2017.in\\videos_worth_spreading.in"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2017-qualif\\out\\videos_worth_spreading.out"

    parser = argparse.ArgumentParser(
        description='Compute hashcode pizza regina')
    parser.add_argument('-i', '--filein', help='Input file',
                        default=DEFAULT_F, type=str)
    parser.add_argument('-o', '--fileout', help='Ouput file',
                        default=OUTPUT_F, type=str)
    parser.add_argument('-v', '--verbose', default=-1,
                        help='verbose mode', type=int)
    args = parser.parse_args()

    with open(args.filein) as f:
        videosN, endpointsN, requestsN, cacheN, cacheSize = map(
            int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
        videosSize = [int(x)
                      for x in re.sub("\n", "", f.readline()).split(" ")]
        # Here endpoint treatement
        # All endpoints
        endpointsLatencyCache = []
        endpointsLatencyDataCenter = {}
        for i in range(endpointsN):
            datacenterLatency, cacheConnectedN = map(
                int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
            endpointsLatencyDataCenter[i] = datacenterLatency
            # One endpoints
            endpointLatencyCache = {}
            for i in range(cacheConnectedN):
                cache, latency = map(
                    int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
                endpointLatencyCache[cache] = latency
            endpointsLatencyCache.append(endpointLatencyCache)

        # Here videos treatment
        endpointsVideosRequest = [{} for i in range(endpointsN)]
        for i in range(requestsN):
            video, endpoint, number = map(
                int, [int(x) for x in re.sub("\n", "", f.readline()).split(" ")])
            endpointVideosRequest = endpointsVideosRequest[endpoint]
            endpointVideosRequest[video] = number

        # endpointsLatencyDataCenter  {0:1000,1:500,.......}
        # endpointsLatencyCache [endpoint 0: {cache 0:latency 5,cache 1:latency:1000}
        #                        endpoint 1:  {} ]
        # endpointsVideosRequest[endpoint 0: {video 0:request 15000,video 1:request :1000}
        #                       endpoint 1:  {video 1: request 2000} ]
        # videosSize [50,10,30,80,100]


    cachesSortedByRequestsNumber = sort_server_per_request_number(endpointsLatencyCache, endpointsVideosRequest, cacheN)
    solution = solve(videosSize, endpointsLatencyCache, endpointsVideosRequest, endpointsLatencyDataCenter,  cachesSortedByRequestsNumber,videosN, endpointsN, cacheN,cacheSize)

    cachesOutN = len(solution)
    f = open(args.fileout,"w")
    f.write(str(cachesOutN)+"\n")
    for k,videos in solution.items():
        f.write(str(k) + " ")
        f.write(' '.join(str(videos[i]) for i in range(len(videos))))
        f.write("\n")
    
    
