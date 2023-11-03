# Lunar Lander
In this usecase the objective is to land a simple rocket on the moon. You task is to navigate the rocket using its three engines (left, right and main), and land it safely on the landing pad between the two flags. The rocket is subject to both gravity and wind.


<p align="center">
  <img src="../images/lunar_lander.gif" width=650>
</p>

## About the game
For extensive information about the game see [Lunar Lander](https://gymnasium.farama.org/environments/box2d/lunar_lander/).

A landing attempt is considered a success if a score of at least 200 points is achieved.

## Interaction
You'll receive a LunarLanderPredictRequestDto which contain the following:
```python
class LunarLanderPredictRequestDto(BaseModel):
    observation: List[float]
    reward: float
    is_terminal: bool
    total_reward: float
    game_ticks: int
```

- *The **observation** is an 8-dimensional vector: the coordinates of the lander in x & y, its linear velocities in x & y, its angle, its angular velocity, and two booleans that represent whether each leg is in contact with the ground or not* [(Observation Space)](https://gymnasium.farama.org/environments/box2d/lunar_lander/#observation-space).

- **reward** is the reward for the given action (See [Rewards](https://gymnasium.farama.org/environments/box2d/lunar_lander/#rewards)).
- **is_terminal** is a boolean that indicates whether the game is over or not.
- **total_reward** is the total score for your current game.
- **game_ticks** is the number of game tick currently running.

Given this information, your task is to predict the next action:
```python
class LunarLanderPredictResponseDto(BaseModel):
    action: int
```
- The **action** can take four different values:
  - 0: do nothing
  - 1: fire left orientation engine
  - 2: fire main engine
  - 3: fire right orientation engine

## Evaluation
**TODO: Update evaluation with desired scoring, N_attempts + time limit.**  
During the competetion you will be able to validate your solution against a validation seed. The best score you model recieve will be displayed on the scoreboard.

Once you have developed your solution, you should submit it for evaluation.  
**Notice, that you can only submit for evaluation once!** Thus, we encourage you to validate your code and API before submitting the model.

### Configurations
The evaluation of the game will run with the following configurations.
```python
env = gym.make(
    "LunarLander-v2",
    continuous: bool = False,
    gravity: float = -10.0,
    enable_wind: bool = True,
    wind_power: float = 15.0,
    turbulence_power: float = 1.5,
)
```

### Tips
If you are using Emily, you can find the documentation of your API where you can try out your model and verify the prediction. The documentation is by default found at ```0.0.0.0:4242/docs```, and then find the prediction endpoint for the use case.


## Getting Started using Emily
Open the project using:
```shell
emily open lunar-lander
```
A Docker container with a Python environment will be opened. Some content needs to be downloaded the first time a project is opened, this might take a bit of time.

A dummy response has been created in router.py. To take full advantage of Emily and the template, your code for the moves should go in here:

```python
@router.post('/predict', response_model=LunarLanderPredictResponseDto)
def predict(request: LunarLanderPredictRequestDto):
    # x, y, vx, vy, theta, vtheta, l1, l2 = oberservation = request.observation
    # reward = request.reward
    # total_reward = request.total_reward
    # game_ticks = request.game_ticks
    # game_is_over = request.is_terminal

    # Your moves go here!
    action = int(np.random.randint(5))

    return LunarLanderPredictResponseDto(
        action=action
    )

```

You can add new packages to the Python environment by adding the names of the packages to requirements.txt and restarting the project, or by using pip install on a terminal within the container which will result in the package being installed temporarily i.e. it is not installed if the project is restarted. <a href="https://emily.ambolt.io/docs/latest">Click here</a> to visit the Emily documentation.

## Run the game locally
To better explore the game's behavior, you can run the game locally.

### Virtual Environment
Start by setting up the environment, for example using either venv or conda:
```shell 
python -m venv .venv
source .venv/bin/activate # bash
.venv\Scripts\activate.bat # cmd
.venv\Scripts\Activate.ps1 # PowerShell
```

```shell 
conda create -n lunar_lander
conda activate lunar_lander
```

### Install dependencies
```shell 
pip install -r requirements.txt
```

### Experiment locally
You can either play the game, using the ```run_game.py``` script, or create your own script for local experiments.
