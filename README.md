# Descent Clock

Countdown timer for the Gradient hackathon, staged as a gradient descent run.

Live: https://gradientvc.github.io/hackathon-timer/

- Space or tap the numerals: start / pause. R: reset. Up / down arrows: add or remove a minute. F: fullscreen. M: sound.
- Duration via URL: `?m=3` (minutes) or `?s=90` (seconds). Default is five minutes.

`timer.html` is the source (no document skeleton, it doubles as the Claude artifact). `python3 build.py` wraps it into `index.html`, which is what Pages serves.
