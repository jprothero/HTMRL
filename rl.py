from utils import *
from params import *

def main():
    episodicRewards = []

    env = setupGym(envName, print=False)
    
    for episode in range(numEpisodes):
        accumReward = 0
        observation = env.reset()
        for t in range(numTimesteps):
            # env.render()
            # print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            
            accumReward += reward
            if done:
                # print("Episode finished after {} \
                #     timesteps".format(t+1))
                # print("Cumulative Reward: {} \
                #     ".format(accumReward))                
                episodicRewards.append(accumReward)
                accumReward = 0
                break

    episodicRewards = np.array(episodicRewards)
    print("""Cumulative reward mean: %0.2f\nCumulative reward std: %0.2f""" % \
    (episodicRewards.mean(), episodicRewards.std()))

if __name__ == "__main__":
    main()