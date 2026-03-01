import numpy as np
from scipy.optimize import minimize

def trajopt_2d(start, goal, T, obstacle, subgoal=None, subgoal_t=None):

    dim = 2

    # initial trajectory
    traj_init = np.linspace(start, goal, T)

    # optimization variables: q1 ~ q_{T-2}
    x0 = traj_init[1:-1].flatten()

    def unpack(x):
        traj = np.zeros((T, dim))
        traj[0] = start
        traj[-1] = goal
        traj[1:-1] = x.reshape(T-2, dim)
        return traj

    def objective(x):
        traj = unpack(x)

        smooth_cost = 0.0
        obs_cost = 0.0

        # smoothness
        for t in range(T-1):
            smooth_cost += np.sum((traj[t+1] - traj[t])**2)

        # obstacle
        for t in range(T):
            obs_cost += obstacle.cost(traj[t])

        return smooth_cost + 10.0 * obs_cost

    constraints = []

    # subgoal constraint
    if subgoal is not None and subgoal_t is not None:
        def subgoal_constraint(x):
            traj = unpack(x)
            return traj[subgoal_t] - subgoal

        constraints.append({
            'type': 'eq',
            'fun': subgoal_constraint
        })

    res = minimize(
        objective,
        x0,
        method='SLSQP',
        constraints=constraints,
        options={'maxiter': 200}
    )

    traj = unpack(res.x)

    return traj, res.fun, res.success