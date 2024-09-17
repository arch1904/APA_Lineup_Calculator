# Team Lineup Generator

This project is a Django web application designed to help organize teams for 8-ball and 9-ball pool games. It allows users to input team members, their skill levels for both game types, and then generates possible lineups based on specified criteria. The generated lineups are sorted based on the highest individual skill levels, ensuring a strategic team composition.

## Features

- **Input Team Members**: Add up to 8 players with their names and skill levels (SL) for both 8-ball and 9-ball games.
- **Game Type Selection**: Choose between 8-ball and 9-ball to generate lineups based on the selected game type.
- **Skill Level Filtering**: Generates lineups that meet the total skill level constraints.
- **Sorted Lineups**: Displays lineups in descending order based on the highest individual skill levels within each lineup.
- **Session Management**: Uses Django sessions to handle data between form submissions.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (TailwindCSS), JavaScript
- **Database**: SQLite (default with Django)
- **Tools**: Django Sessions, Django Templating

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 3.x or higher

### Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd team-lineup-generator
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

1. **Enter Player Information**:
   - On the home page, input up to 8 players with their names, 8-ball SL, and 9-ball SL.
   - Click "Submit" to save the player information.

2. **Select Game Type**:
   - After submitting player data, choose either 8-ball or 9-ball to generate the lineups.

3. **View Lineups**:
   - The application will display all possible lineups that meet the SL constraints.
   - Lineups are ordered in descending order based on the highest individual SL in each lineup.

## Project Structure

- **`templates/`**: Contains HTML files for different pages.
  - `player_form.html`: Form to input player data.
  - `game_selection.html`: Page to select the game type.
  - `lineup_results.html`: Page to display the generated lineups.
- **`views.py`**: Contains Django views for handling form submissions and generating lineups.
- **`urls.py`**: URL routing configuration for the application.
- **`generate_team_combos`**: Core function that generates and sorts the lineups.

## Key Functions

- **`generate_team_combos`**:
  - Generates all possible lineups for a team within the specified constraints.
  - Filters lineups based on the maximum allowed skill level sum.
  - Orders the lineups by the highest individual SL in descending order.

## Example Workflow

1. Input 8 players with their skill levels for 8-ball and 9-ball.
2. Submit the player information.
3. Select "8-ball" or "9-ball" to generate lineups.
4. View the generated lineups, sorted by the highest individual SL within each lineup.

## Screenshots

*(Include screenshots of the different pages here if available.)*

## Known Issues and Limitations

- The current implementation uses Django sessions to temporarily store player data. This may not be suitable for large-scale or multi-user applications without further modifications.
- Skill level constraints (maximum number of players and sum of skill levels) are hardcoded.

## Future Enhancements

- Allow dynamic configuration of maximum lineup size and skill level constraints.
- Improve the UI for a more interactive and user-friendly experience.
- Add user authentication for a multi-user environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

---

## Contact

For any inquiries or issues, please contact Archit Gupta at architgupta941@gmail.com

