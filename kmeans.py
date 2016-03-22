#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
import os
import time

best=10000
	
def buildStruct(r_clusters):#build a list of lists, that will act as classification of the points
	clusters=[]
	for i in range(0,r_clusters):
		clusters.append([])
	return clusters	
	
def loadPoints():#return a list containing n-sized vectors 
	f=open("kmeansDb","r")
	lines=f.readlines()	#load data
	points=lines[1:] #get all data,except fist line
	for i in points:
		points[points.index(i)]=i.split() #trim the data, split reduces whitespaces
	points=[[float(j) for j in i] for i in points] #make all points floats
	return points 

def chooseInitCenters(points,r_clusters): #returns initial centers 
	centerIndices=[]
	centers=[]
	index=0
	while True:
		index=random.randint(0,r_clusters-1) #get random int x  0<=x<=r_clusters. What if r_clusters==len(data)? #solution: -1
		if index in centerIndices:
			continue
		centerIndices.append(index)
		centers.append(points[index])
		if len(centerIndices)==r_clusters:
			break
	return sorted(centers)

def cAverage(points): #calculates average of multiple n-dimensional points.
	return [sum(e)/len(e) for e in zip(*points)]

def calcDistance(center,point):#calculates Euclidean distance of n-sized vectors.
	result=0
	count=0
	for dimension in point:
		result+=math.pow(point[point.index(dimension)]-center[point.index(dimension)],2)
		count+=1
	return math.sqrt(result)

def classify(clusters,points,centers): #put all the data in the corresponding clusters
	for item in points:
		index=0
		distance=calcDistance(centers[0],item)
		for center in centers:
			if calcDistance(center,item)<distance:
				index=centers.index(center)
		clusters[index].append(item)
	return clusters
	
def iterate(clusters,centers,points): #main part of the algorithm. calculate centers,then classify based on those.
	index=0
	for cluster in clusters:
		average=cAverage(cluster)
		if cluster and average!=centers[index]:
			centers[index]=average
		index+=1
	newClusters=classify(buildStruct(len(centers)),points,centers) #arg1 must be empty list of lists
	return newClusters,centers
			
def clusterPrint(newClusters,clusters): #pretty print them maybe?
	count=0
	global best
	for i in range(0,len(clusters)):
		for item in clusters[i]:
			try:
				if item != (newClusters[i][clusters[i].index(item)]):
					count+=1
					#print item,"||",newClusters[i][clusters[i].index(item)] #some kind of magic here. An to dei o Giannis ayto 8a pa8ei paniko
			except:
				pass
	os.system("clear")
	if count < best:
		best=count
	print count,"Differences",best,"Best"
	count=0
	#time.sleep(0.1)
def getNumber(x):
	while True:
		number=input("No of clusters? ")
		if number>x:
			print "Too many clusters, try again"
			continue
		return number
 			
def main():
	points=loadPoints()
	r_clusters=getNumber(len(points)) # this must be < number of data, cant have 1 point in 2 categories.
	clusters=buildStruct(r_clusters)
	centers=chooseInitCenters(points,r_clusters)
	clusters=classify(clusters,points,centers)
	for i in range(1,100): #we already have classified our data once
		newClusters,centers=iterate(clusters,centers,points)
		#os.system("clear")
		#print i,"iterations"
		clusterPrint(newClusters,clusters)
		if newClusters==clusters:
			print "Success after",i+1,"iterations"
			return
		clusters=newClusters
	print "Unsuccessful"
	return 0

if __name__ == '__main__':
	main()
