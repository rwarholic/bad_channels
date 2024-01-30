from pedalboard import *
from pedalboard.io import AudioFile
import sys
import os

def make_pedalboard(wav, odir):
    # read in file, resampling as necessary
    sr = 16000
    with AudioFile(wav).resampled_to(sr) as f:
        audio = f.read(f.frames)
        
    # hard-coded for now
    vbr = 9.99
    db = 20
    # make sound pedalboard object
    board = Pedalboard([
        #Compressor(threshold_db=-25, ratio=11),
        MP3Compressor(vbr),
        Distortion(db)
    ])

    # Run audio through pedalboard
    effected = board(audio, sr)

    convo = os.path.splitext(os.path.basename(wav))[0]
    # Write audio back as a mp3 file:
    with AudioFile(f"./{odir}/mp3compressor_dist_{convo}.mp3", "w", sr, effected.shape[0]) as f:
        f.write(effected)

def main(args):
    # check command line for correct arguments
    if len(sys.argv) != 3:
        print("usage: get_output.py <input_directory> <output_directory>")
        exit(1)

    idir = args[1]
    odir = args[2]
    for filename in os.listdir(idir):
        # save output name for convolved file
        audio_file = os.path.join(idir, filename)
        print(os.path.splitext(os.path.basename(audio_file))[0])
        make_pedalboard(audio_file, odir)

if __name__ == '__main__':
    main(sys.argv)