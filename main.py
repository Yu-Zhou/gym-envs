import gym
import numpy as np

# Assuming gym_envs is a module that includes your custom gym environment
import gym_envs

def td(pi, env, gamma=1.0, alpha=0.01, n_episodes=10000):
    """ Temporal Difference Learning Algorithm """
    V = np.zeros(env.observation_space.n)
    for t in range(n_episodes):
        state, terminated = env.reset(), False
        truncated = False
        while not terminated:
            action = pi(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            td_target = reward + gamma * V[next_state] * (not terminated)
            td_error = td_target - V[state]
            V[state] = V[state] + alpha * td_error
            state = next_state
    return V

def main():
    env = gym.make('WalkFive-v0')
    pi = lambda x: np.random.randint(2)
    V = td(pi, env)
    print("Value Function:", V)

if __name__ == "__main__":
    main()
