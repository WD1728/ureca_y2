plt.plot(best_traj[:,0], best_traj[:,1], '-o')
plt.scatter(start[0], start[1], label='start')
plt.scatter(goal[0], goal[1], label='goal')
plt.scatter(subgoal[0], subgoal[1], label='subgoal')

circle = plt.Circle((5,0), 1.5, color='r', alpha=0.3)
plt.gca().add_patch(circle)

plt.legend()
plt.axis('equal')
plt.show()