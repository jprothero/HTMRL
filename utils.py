import gym
from gym import envs
import numpy as np

def printEnvs(): print(envs.registry.all())

def printEnvInfo(env):
    print(env.action_space)
    print(env.observation_space)
    print(env.observation_space.high)
    print(env.observation_space.low)

def setupGym(envName, print=True):
    env = gym.make(envName)
    if print: printEnvInfo(env)
    return env