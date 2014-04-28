#!/usr/bin/env python2

import sys
from math import log

def information(p): return -log(p, 2)

def entropy(probabilities):
    total = 0
    for p in probabilities:
        total += p * information(p)
    return total

def compute_information_sources(ips):
    sources = []
    for ip in ips.keys():
        sample_size    = len(ips[ip])
        unique_symbols = set(ips[ip])
        probabilities  = [float(ips[ip].count(s)) / sample_size for s in unique_symbols]
        sources.append([ip, entropy(probabilities), sample_size, sorted(ips[ip])])
    return sorted(sources, key = lambda x: x[1])

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ["source", "destination"]:
        sys.exit("Usage: %s [source | destination] < [data]" % sys.argv[0])
        exit(-1)

    file = open("/dev/stdin")
    lines = file.readlines()
    file.close()

    src_ips = {}
    dst_ips = {}

    for line in lines[1:]:
        fields = line.split(", ")
        src_ip = fields[3]
        dst_ip = fields[4]

        if src_ip not in src_ips: src_ips[src_ip] = []
        src_ips[src_ip].append(dst_ip)

        if dst_ip not in dst_ips: dst_ips[dst_ip] = []
        dst_ips[dst_ip].append(src_ip)

    information_sources = compute_information_sources(src_ips if(sys.argv[1] == "source") else dst_ips)

    # Print everything as CSV
    for source in information_sources:
        line = "%s, %f, %d" % (source[0], source[1], source[2])
        for ip in source[3]:
            line += ", " + ip
        print line

    # Print just the information sources' IP and entropy
    # for source in information_sources:
    #     print "%s %f" % (source[0], source[1])