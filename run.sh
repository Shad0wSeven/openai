rm ns.mp4
rm output.mp4
rm input.mp3
rm RTVC/input.txt

ffmpeg -i input.mp4 input.mp3

cp input.txt RTVC/input.txt

cp input.mp3 RTVC/

python3 RTVC/run.py

cp demo_output_00.wav WTL/doc.wav
ffmpeg -i input.mp4 -vf scale=-1:480 output.mp4
ffmpeg -i output.mp4 -c copy -an ns.mp4
cp ns.mp4 WTL/input.mp4

cd WTL

python3 inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face input.mp4 --audio doc.wav

cd ..
cp WTL/results/result_voice.mp4 result.mp4

rm ns.mp4
rm output.mp4
rm input.mp3
rm RTVC/input.txt