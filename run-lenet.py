#! /usr/bin/env python

from subprocess import call
import sys
#from os import listdir
#from os.path import isfile, join

pipes_to_run = [ 0, 1]

for x in range(0,len(pipes_to_run)):

  # Copy in the new data
  call("cp /datasets/cifar-10/v"+str(pipes_to_run[x])+"/* data/cifar10/", shell=True)

  # Recalculate image mean and create database
  call("./examples/cifar10/create_cifar10.sh", shell=True)

  # Let the user know what run is currently being processed
  call("echo Now running with data from pipeline V"+str(pipes_to_run[x]), shell=True)

  # Run the training and pipe output to a log file
  call("./examples/cifar10/train_full.sh 2> log_"+str(pipes_to_run[x])+".txt", shell=True)
