#! /usr/bin/bash

# Put all audio files in a directory through a bandpass filter, mimicking frequency range of telephone audio. 

# Sox and ffmpeg citation: cloudacm.com/?p=3132

echo $1
echo $2

filepath=$1
outputdir=$2
for i in ${filepath}/*.wav; do
	basename=$(basename ${i} .wav)
	# if i wanted to just get conversation number, i'd uncomment below and use that as output name
	#arr=(${basename//-/ })
	#conv_id=${arr[1]}
	sox "${i}" "./${outputdir}/${basename}_bandpass.wav" sinc 300-3k
done
