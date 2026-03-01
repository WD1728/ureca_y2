import numpy as np
from trajopt import trajopt_2d
from env import CircleObstacle
import matplotlib.pyplot as plt

start = np.array([0, 0])
goal = np.array([10, 0])
subgoal = np.array([5, 3])

T = 20

obs = CircleObstacle(center=[5, 0], radius=1.5)

best_cost = float('inf')
best_traj = None
best_k = None

for k in range(1, T-1):
    traj, cost, success = trajopt_2d(start, goal, T, obs, subgoal, k)
    print(f"k={k}, cost={cost:.3f}")

    if cost < best_cost:
        best_cost = cost
        best_traj = traj
        best_k = k

print("Best k:", best_k)
