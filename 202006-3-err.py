
import sys
import re
import math
from pprint import pprint

def run():
    w = int(input())
    data = sys.stdin.read().split("\n")
    len_data = len(data)

    graph = ''

    lines = 0
    pg = 0 # paragraph
    l = 0  
    while l < len_data:
        graph = ''
        while l < len_data:
            line = data[l]
            line = line.strip(' ')

            if line != '':
                break

            l += 1

        if l < len_data and data[l].startswith("* "):
            graph += "* " + line[2:].strip(" ") + " "
            l += 1
            
            while l < len_data:
                line = data[l]

                if not line.startswith("  "):
                    graph = graph[:-1]
                    if not line.startswith("* "):
                        pg += 1

                    break

                line = line.strip(' ')

                graph += line + " "
                l += 1
        else:
            while l < len_data:
                line = data[l]
                line = line.strip(' ')

                if line == '' or line.startswith("* "):
                    graph = graph[:-1]
                    pg += 1
                    break

                graph += (line + " ")
                l += 1

        if graph != '':
            print(graph, lines)
            i = 0
            append = 0

            if graph.startswith("* "):
                append = 3
                if graph == "*  ":
                    lines += 1

                graph = graph[2:-1]


            while i < len(graph):
                while graph[i] == ' ':
                    i += 1

                i += (w - append)
                lines += 1

            print("=",graph, lines)

    print(lines + pg - 1)

if __name__ == "__main__":
    run()
