# Projectile Calculator

Beginner Python project — built by Steven (with Cursor as coach, not code author).

## Goal

A command-line tool for basic aerospace / physics math:

1. Horizontal range and time of flight for a projectile
2. (Later) max height, impact speed, unit conversions

## Formulas (Challenge 1)

Launch speed `v`, angle `θ` (degrees), gravity `g = 9.81 m/s²`:

- time of flight: `t = 2 * v * sin(θ) / g`
- range: `R = v² * sin(2θ) / g`

Assumes flat ground, no air resistance.

## How to run

```bash
python main.py
```

## What I'm practicing

- loops
- math / trigonometry
- matplotlib plots
- input validation

## Status

Finished
