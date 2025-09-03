🎯 Backend Developer Test (Python + Django)

Overview

You will build a Django REST API that manages soccer players and tracks how many times each player is “liked.”
The API should allow users to like players, and should provide ranking views across different dimensions.

⸻

Requirements
1. Database Schema
	•	Using the provided Players.json file, generate the appropreiate database schemas and apply them to your solution
	•	Generate a script/function that populates the database using this provided data into your designed schemas to ensure we are able to get the same ressults as you locally (or use django directly - ensure the json file is updated)

2. Soccer Players
	•	Implement a model for soccer players.
	•	Each player should have:
	•	Name
	•	Club
	•	Position (Goalkeeper, Defender, Midfielder, Forward)
	•	Number of likes (integer, default = 0)
	•	Create an endpoint that lists all players.
	•	The list should support optional filtering by club and/or position.

⸻

3. Liking a Player
	•	Create an endpoint that allows a user to “like” a specific player.
	•	Each request should increment that player’s like count by 1.
	•	The updated player data should be returned.

⸻

4. Rankings

Create endpoints that provide player rankings in different ways:
	1.	Overall ranking – returns all players ordered by total likes (highest first).
	2.	By position – groups players by their position, and sorts players within each group by likes.
	3.	By club – groups players by their club, and sorts players within each group by likes.

⸻

5. Bonus Features (Optional)
	•	Prevent the same user from liking the same player more than once (requires authentication).
	•	Add support for returning the “Top N” most liked players, where N is configurable.
	•	Add a way to return the most liked player(s) within each club.
	•	Add unit tests to verify ranking and like logic.
	•	Add pagination to the player list.

⸻

Expectations
	•	Use Django + Django REST Framework and a local postgres db.
	•	Follow RESTful design principles in your endpoint naming and structure.
	•	Keep the code clear, idiomatic, and well-structured.
	•	Include a short README describing your design choices and any assumptions.