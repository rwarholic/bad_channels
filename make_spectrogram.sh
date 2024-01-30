#! /usr/bin/bash


for $i in ./${idir}/*.wav; do
	basename=$(basename ${i} .wav)
	ffmpeg -i "${i}" -lavfi showspectrumpic=s=3600x1200 "./${odir}/${basename}_Color-FFMpegHD.png"
done
