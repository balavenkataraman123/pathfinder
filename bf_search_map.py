stations = [1,2,3,4,5,6,7,8,9,10]
edges = [(1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(4,5),(5,4),(2,6),(6,2),(6,7),(7,6),(7,8),(8,7),(8,9),(9,8),(8,10),(10,8)]
import copy
def paths(station,end,parentnodelist):
    nodelist = []
    parentnodelist1 = copy.deepcopy(parentnodelist)
    parentnodelist1.append(station)
    for i in edges:
        if i[0] == station:
            nodelist.append(i[1])
    if end in nodelist:
        return [parentnodelist1, 1]
    for i in nodelist:
        if not i in parentnodelist1:
            a = paths(i,end,parentnodelist1)

            if a[1] == 1:
                return a
    return [11, 0]
if __name__ == "__main__":
    start = int(input(''))
    end = int(input(''))
    print(paths(start,end,[])[0])