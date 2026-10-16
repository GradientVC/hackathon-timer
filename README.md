# Descent Clock

Countdown timer for the Gradient hackathon, staged as a gradient descent run. Its twin, the Ascent Clock, is a count-up stopwatch with laps.

- Countdown: https://gradientvc.github.io/hackathon-timer/
- Stopwatch: https://gradientvc.github.io/hackathon-timer/stopwatch/

## Countdown

- Space or tap the numerals: start / pause. R: reset. Up / down arrows: add or remove a minute. F: fullscreen. M: sound.
- Duration via URL: `?m=3` (minutes) or `?s=90` (seconds). Default is five minutes.
- The ground heats to red through the final minute and goes solid red at zero.

## Stopwatch

- Space or tap the numerals: start / pause. L: lap. R: reset (clears laps). F: fullscreen. M: sound.
- Optional limit via URL: `?limit=5` (minutes). The last minute before the limit reads UNSTABLE, past it the ground goes red and the status reads DIVERGED with the overrun. Up / down arrows move the limit by a minute. Without a limit the top rule shows twelve five-minute segments per hour.
- Switches to `H:MM:SS` past an hour.

## Files

`timer.html` and `stopwatch.html` are the sources (no document skeleton; they double as the Claude artifacts). `python3 build.py` wraps them into `index.html` and `stopwatch/index.html`, which is what Pages serves.
