# write a function that given a list of building heights in a row [1,4,2,3,5] wil return visible buildings [1,4,5]

def see_building(start,arr):
    vis_build =[]
    for i in range(len(arr)- 1):
        if len(vis_build) == 0 and arr[i] > start:
            vis_build.append(arr[i])
        if arr[i] > vis_build[len(vis_build)-1]:
            vis_build.append(arr[i])
    return vis_build

print(see_building(0,[1,4,2,3,5]))