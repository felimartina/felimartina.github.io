# AGENTS.md

This document provides guidelines for AI agents working on this repository. Please read it carefully before making any changes.

## General Guidelines

*   **Understand the Goal:** The primary goal of this project is to provide a generic and reusable trip itinerary visualizer. Before making any changes, make sure you understand this goal.
*   **Be Resourceful:** Use the tools at your disposal to understand the codebase and the project. Read the `README.md` files, and explore the code and data files.
*   **Keep it Generic:** All code should be generic so that we can easily swap itinerary and POI files for any other trip to anywhere in the world. Do not hardcode any data that is specific to a particular trip.
*   **Test Your Changes:** Before submitting your changes, make sure to test them thoroughly. If you make changes to the itinerary logic, ensure it works with different types of itineraries.

## Project-Specific Guidelines

### Data Schema

This section describes the data schema for the JSON files that drive the itinerary visualizer.

#### Data Files

The itinerary is generated from two JSON files:

*   `itinerary.json`: Contains the chronological list of events for the trip.
*   `poi.json`: Contains a list of points of interest for each city.

When you are asked to modify the itinerary, you should edit these files. The web application will automatically reflect the changes.

#### Itinerary Event Types

The `itinerary.json` file uses a `type` field to classify each event. The following types are currently supported:

*   `flight`
*   `flight_arrival`
*   `lodging`
*   `sleep`
*   `activity`
*   `daytrip`
*   `business`
*   `transport`

#### POI Categories

The `poi.json` file uses a `category` field to classify each point of interest. The following categories are currently supported:

*   `Parque`
*   `Atracción`
*   `Mirador`
*   `Templo`
*   `Compras`
*   `Mercado`
*   `Restaurante`
*   `Tienda`
*   `Tip`
*   `Alojamiento`
*   `Jardín`
*   `Museo`
*   `Café`

### Trip Summary Logic

The trip summary is calculated by the `calculateCityStays` function in `index.html`. This function determines the number of days and nights for each city stay. Certain event types from `itinerary.json` have a special meaning for this logic:

*   **`sleep`**: Each event with this type counts as one **night** in a city. This is the primary indicator of an overnight stay.
*   **`activity` / `business`**: Events with these types are used to count the number of **days** spent in a city. The calculation is based on the unique calendar days that have at least one `sleep`, `activity`, or `business` event.
*   **`daytrip`**: This event type signifies a day trip to a different location. A day that includes a `daytrip` event will not be counted as a full day in the main city, effectively reducing the day count.

The calculation of days is also affected by arrival and departure times:
*   If the arrival time is after 11:00 AM, half a day is subtracted.
*   If the departure time is before 1:00 PM, half a day is subtracted.
*   If the departure time is before 6:00 PM, half a day is subtracted.

When making changes that could affect the trip summary, please be mindful of this logic and the special role of the `sleep`, `activity`, and `daytrip` event types.

### Updating the Itinerary

When you are asked to update the itinerary, please follow these guidelines to ensure consistency:

*   **Flights:** When adding a flight, you should also add the following events:
    *   A `transport` event for the commute to the airport before the flight.
    *   A `flight_arrival` event to mark the landing. This is important for the timeline visualization.
*   **Day Trips:** When adding a day trip, remember to add `transport` events for the commute to and from the day trip location.
*   **Travel Duration:** For all `flight` and `transport` events, add a `duration` field. If the duration is not provided, please search for it online or make a reasonable estimate.

### Taking Screenshots

When you make changes to the website, you **must** provide a screenshot of the updated UI along with your code changes.

To take a screenshot, follow these steps:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```
2.  **Start the web server:**
    ```bash
    python3 -m http.server 8000 &
    ```
3.  **Run the screenshot script:**
    ```bash
    python scripts/take-screenshot.py --output timeline-updated.png
    ```
4.  **Share the screenshot:**
    When you submit your changes, mention the path to the screenshot you generated (e.g., `timeline-updated.png`).
