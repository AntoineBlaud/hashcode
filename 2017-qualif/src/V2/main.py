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
import numpy as np
import random
import matplotlib.pyplot as plt
import datetime
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
    print("ok")
    # {cache 3: 4000, cache 1: 3500, ....}
    cacheRequests = dict(sorted(cacheRequests.items(), key=lambda t: t[1], reverse=True))
    return cacheRequests


def endpoint_connected_to_cache(endpointsLatencyCache, cache, endpoint):
    return cache in endpointsLatencyCache[endpoint]


def evaluateVideosPoints(endpointsLatencyCache, endpointsVideosRequest, endpointsLatencyDataCenter,endpointVideoLatency, videosN,cache):
    videosPoints = {i: 0 for i in range(videosN)}
    for video in range(videosN):
        for endpoint in range(len(endpointsVideosRequest)):
            videosRequest = endpointsVideosRequest[endpoint]
            if(video in videosRequest):
                if(endpoint_connected_to_cache(endpointsLatencyCache, cache, endpoint)):
                    latency = endpointsLatencyDataCenter[endpoint]-endpointsLatencyCache[endpoint][cache]
                    if()
                    videosPoints[video]+= (latency)*videosRequest[video]
    return videosPoints


def solve(endpointsLatencyCache, endpointsVideosRequest, endpointsLatencyDataCenter, videosN,endpointN,cacheN):



if __name__ == '__main__':

    DEFAULT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2017-qualif\\qualification_round_2017.in\\exemple.in"
    OUTPUT_F = "C:\\Users\\antoi\\Documents\\GitHub\\hashcode\\2017-qualif\\out\\exemple.out"

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

    print("Finished getting input")

    cacheSortedByRequests = sort_server_per_request_number(
        endpointsLatencyCache, endpointsVideosRequest, cacheN)

    evaluateVideosPoints(endpointsLatencyCache,endpointsVideosRequest,endpointsLatencyDataCenter,videosN,0)
    print("OK")
