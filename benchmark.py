#!/usr/bin/env python3

import time

import numpy as np

import gym
import gym_duckietown
from gym_duckietown.envs import SimpleSimEnv

st = time.time()
env = SimpleSimEnv(max_steps = 20000)
env.seed(0)
env.reset()
load_time = 1000 * (time.time() - st)

num_frames = 0
st = time.time()

while True:
    dt = time.time() - st

    if dt > 5:
        break

    # Slow speed to minimize resets
    action = np.array([0.05, 0.05])
    obs, reward, done, info = env.step(action)

    if done:
        env.reset()

    num_frames += 1

fps = num_frames / dt
frame_time = 1000 * dt / num_frames

print()
print('load time: %d ms' % int(load_time))
print('frame time: %.1f ms' % frame_time)
print('frame rate: %.1f fps' % fps)

env.close()
