#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def distance(center,point):#calculates Euclidean distance of n-sized vectors. OK
	result=0
	count=0
	for dimension in point:
		result+=math.pow(point[count]-center[count],2)
		count+=1
	return math.sqrt(result)
	
def loadPoints():#return a list containing n-sized vectors #OK
	f=open("kmeans.txt","r")
	lines=f.readlines()	#load data
	points=lines[1:] #get all data,except fist line
	for i in points:
		points[points.index(i)]=i.split() #trim the data, split reduces whitespaces
	points=[[float(j) for j in i] for i in points] #make all points floats
	return points 

def cAverage(points): #calculates average of multiple n-dimensional points. works as intended
	result=[]
	count=0 #initialize a dynamic array that will be the result
	total_points=len(points)
	for count in range(0,total_points):
		result.append((1.0/total_points)*sum([item[count] for item in points]))
	return result

def chooseCenters(points,clusters): #returns indices that split the data into clusters. #is this what we want?
	centerIndices=[]
	index=int(math.ceil(float(len(points)/float(clusters))))
	for i in range(0,len(points),index):
		centerIndices.append(i)
	return centerIndices

def main():
	clusters=3
	points=loadPoints()
	centerIndices=chooseCenters(points,clusters)
	
	return 0

if __name__ == '__main__':
	main()

