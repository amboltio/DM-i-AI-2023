import gymnasium as gym


class LunarLanderEnvHandler():
    def __init__(self, render_mode=None) -> None:
        self.env = gym.make(
            "LunarLander-v2", render_mode=render_mode)

        self._game_ticks = 0
        self._total_reward = 0
        
    def step(self, action: list):
        observation, reward, terminated, truncated, _ = self.env.step(action)
        self._game_ticks += 1
        self._total_reward += reward
        return observation, reward, (terminated or truncated), self._total_reward, self._game_ticks

    def reset(self, seed=None):
        self._game_ticks = 0
        self._total_reward = 0
        observation, _ = self.env.reset(seed=seed)
        return observation
    
    