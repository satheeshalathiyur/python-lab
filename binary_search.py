'''
Binary search to findout a element is present in a sorted list
complexity is o(logn)

'''
l = raw_input('enter values seperated by commas')
f = int(raw_input('Element to findout'))
l = map(int,l.split(','))
start = 0
end = len(l)
def cal(start, end):
    print start,end
    m = (start+end)/2
    if l[m] == f:
        print ('element is in index: ',m)
        return
    elif f<l[m]:
        end = m
    else:
        start = m
    cal(start,end)

if f>l[end-1] or f<l[start]:
    print ('Value is not found....')
else:
    cal(start, end)
