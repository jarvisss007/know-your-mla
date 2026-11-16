# studio3d (pilot)

Script-to-video in 3D. A scene is real 3D (three.js: lights, shadows, bloom, rain, camera moves, animated characters),
rendered frame by frame in headless Chrome on the Mac's GPU, with word-by-word captions drawn on top.

    npm install                       # three.js
    python audio.py build             # voice + original score + timing (build/mix.wav, build/timeline.json)
    python render.py pilot.html out/pothole_3d_pilot.mp4 build/mix.wav

`render.py --q=every=56` renders only every 56th frame, for a quick look. A 31-second Short renders in about 30 seconds.
Python: /opt/anaconda3/bin/python (needs numpy, Pillow, ffmpeg). Voices: macOS `say`; the chorus is a recorded voice.

Status: one pilot (Episode 12, potholes, Kannada). The scene is hand-written in pilot.html; the next step is to drive
scenes from a script file the way ../talk.py does.
