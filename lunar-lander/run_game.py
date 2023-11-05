from game.environment import LunarLanderEnvHandler
import pygame
import time

lunar_env = LunarLanderEnvHandler(render_mode="human")

observation = lunar_env.reset(seed=0)

current_key = None


def get_move_from_keyboard():
    global current_key

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            current_key = event.key
        elif event.type == pygame.KEYUP:
            current_key = None

    if current_key == pygame.K_LEFT:
        return 1
    elif current_key == pygame.K_RIGHT:
        return 3
    elif current_key == pygame.K_UP:
        return 0
    elif current_key == pygame.K_DOWN:
        return 2
    else:
        return 0


while True:
    action = get_move_from_keyboard()
    observation, reward, terminated, total_reward, game_ticks = lunar_env.step(
        action)

    if total_reward >= 200:
        print("Landing completed! ", "Total reward: ", total_reward)
        observation = lunar_env.reset()

    if terminated:
        print("Landing failed! ", "Total reward: ", total_reward)
        observation = lunar_env.reset()
        total_reward = 0

    time.sleep(0.1)  # Allows to play the game by hand
