a,b,c,d,e,f=map(int,input().split())
det=a*e-b*d
det_1=c*e-b*f
det_2=a*f-c*d
print(int(det_1/det),int(det_2/det))