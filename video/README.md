# Shorts pipeline

`make.py` renders 1080x1920 scenes with headless Chrome and writes an MP4 (OpenCV, mp4v, 15 fps).

    py make.py ../brand/mark.svg scenes/scenes_wealth.py

Each `scenes/*.py` file defines `SCENES` (seconds, HTML, source line) and `OUT`.
Finished videos are in `out/`. `-kn` files are Kannada-first, `-en` English-first.
`districts.py` maps the 224 MLAs to 31 districts (`mlas_dist.json`).

Rule: every figure on screen carries its public-record source. If one is wrong, open an issue.
