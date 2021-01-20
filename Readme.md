# Rasa Demo

This repo contains example chatbot program written using RASA framework.

## Usage

Training: `rasa train`

Running Rasa Core Server:`rasa run --debug --enable-api -p 5005`

Running Rasa Action Server: `rasa run actions --debug`

Validate Training Data: `rasa data validate stories`

## Debug



Prevent GPU blocking by setting environment variable TF_FORCE_GPU_ALLOW_GROWTH to "true"

