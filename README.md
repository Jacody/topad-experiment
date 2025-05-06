# TOPAD-Experiment

A behavioral economics "Take-or-Pass" decision experiment, developed with [oTree](https://www.otree.org/), a Python platform for online experiments.

## Project Description

This project implements a "Take-or-Pass and Double" (TOPAD) decision game developed as part of a master's thesis. In this experiment, participants must decide in multiple rounds whether to accept an offered amount of money ("Take") or decline and pass it to the next person ("Pass"), where the amount is then doubled.

### Experiment Procedure

1. Each participant receives a random position (1 to N) in each round.
2. The starting amount is €0.03 and doubles with each position.
3. Participants decide one after another (based on their position) whether to take the amount or pass it on.
4. If a participant takes the amount, they receive the payout and the round ends.
5. If all participants pass, the last participant receives the maximum amount.
6. The experiment runs over multiple rounds, with participants' positions randomly reassigned in each round.

## Installation

1. Clone the repository:
```
git clone https://github.com/YourUsername/topad-experiment.git
cd topad-experiment
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Configuration

The main configuration is in the `settings.py` file:

- `NUM_ROUNDS`: Corresponds to the number of participants (default 12)
- `STARTINGVALUE`: Starting amount of the game (default €0.03)
- Adjustment of the number of participants in the `SESSION_CONFIGS` section

## Running the Experiment

1. Start the local development server:
```
otree devserver
```

2. The experiment is then available at `http://localhost:8000`.

## Data Analysis

The project contains several Python scripts for analyzing the experimental data:

- `Analysis.py`: Main script for data analysis and creation of evaluation tables
- `Payoffperround.py`: Analysis of payouts per round
- `Completly_randomlists.py`: Generation of random positions for participants

## Project Structure

- `topad/`: Main module for the TOPAD game
  - `__init__.py`: Contains the game logic and page sequence
  - `TakeOrPass.html`: Main decision page
  - `Results.html`: Results display for each round
  - `Feedback.html`: Feedback form at the end of the experiment
  - `CombinedResults.html`: Summary of all round results
- `stall_page/`, `control/`: Additional modules for the experiment
- `_templates/`: HTML templates for general pages
- `_static/`: Static files (CSS, JavaScript)
- Analysis scripts: 
  - `Analysis.py`: Main evaluation script
  - `Payoffperround.py`: Payout analysis
  - `Completly_randomlists.py`: Generation of random positions

## Theoretical Background

The TOPAD experiment investigates decision-making behavior in sequential games with exponentially growing payouts. Particularly interesting aspects include:

- Risk appetite of participants
- Strategic considerations regarding position in the game
- Trust in subsequent players
- Behavior in repeated game rounds with changing positions

## Requirements

- Python 3.8+
- oTree 5.10+
- Django 4.2+
- Additional dependencies are listed in `requirements.txt`

## License

This project is licensed under the terms described in the [LICENSE](LICENSE) document.

## Publication Notes

Before publishing the code, the following steps should be taken:

1. Remove or replace sensitive data:
   - Check the `settings.py` file for hardcoded credentials
   - Ensure no personal paths are included (e.g., in Analysis.py)
   - Create a `.env.example` file with placeholders for sensitive data

2. Remove experiment-specific data:
   - Database file (`db.sqlite3`)
   - Participant information

3. Ensure that the documentation is complete to ensure reproducibility 