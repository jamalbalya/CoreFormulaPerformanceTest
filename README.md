Flow Process Explanation:

    Imports: The code begins by importing essential modules such as time, threading, requests, statistics, json, and urlparse.

    PerformanceInspector Class: A class named PerformanceInspector is defined. This class encapsulates the entire process of inspecting performance.

    Constructor (__init__): The constructor method is defined but left empty, as it doesn't require specific content in this version.

    start_inspection Method: This method serves as the entry point for starting the performance inspection. It takes inspection_data as input, which is a JSON package containing the website URL and visit count.

    JSON Parsing: The input inspection_data is parsed using json.loads() to extract the values of website and visits.

    Input Validation: The extracted website URL and visit count are validated using the validate_url function. It checks if the URL is valid and the visit count is a positive integer.

    Performance Metrics Calculation: Inside a loop that runs for the specified number of visits:
        The start time is recorded.
        An HTTP GET request is made using requests.get().
        The end time is recorded.
        The difference between start and end times gives the response duration.
        The response object is stored in received_responses, and the duration is added to response_times.

    Metric Calculations: After all visits, various performance metrics are calculated:
        avg_duration: Average response duration.
        duration_deviation: Deviation in response durations.
        error_rate: Percentage of zero-duration responses.
        reqs_per_second: Requests executed per second.
        min_duration: Shortest response duration.
        max_duration: Longest response duration.

    Data Rate Calculations: The received data rate and sent data rate per second are calculated in kilobytes based on the content length of responses and the automatically calculated data_size.

    JSON Result Generation: All calculated metrics are organized into the inspection_results dictionary. This dictionary is transformed into a JSON string using json.dumps().

    URL Validation Method (validate_url): This method checks if a given URL is valid by parsing it using urlparse and ensuring it has both a scheme and a netloc.

    Main Execution Block: The code creates an instance of the PerformanceInspector class. An example JSON package (example_inspection) is provided to simulate an inspection. The start_inspection method is called with the example data. 
    If results are obtained, they are printed; otherwise, an "Invalid inspection details" message is displayed.


Input JSON Structure:
{
    "website": "https://example.com",
    "visits": 50
}


    "website": Insert the URL of the website you want to evaluate.
    "visits": Specify the number of times you want to visit the site for assessment.

Output JSON Structure (Example):

{
    "average_duration": 0.305,
    "duration_deviation": 0.054,
    "error_rate": 0.0,
    "requests_per_second": 164.11042944785277,
    "min_duration": 0.284,
    "max_duration": 0.378,
    "received_kb_per_second": 0.0,
    "sent_kb_per_second": 9.8,
    "average_bytes": 15445.0
}

This code simulates the process of evaluating a website's performance, making HTTP requests, and calculating various performance metrics. It uses a structured JSON package as input and returns a JSON result after processing. 
The provided example input JSON is used for simulation, and the output JSON contains the calculated performance metrics.


for the Requirements, you need to run:
pip install -r requirements.txt


Implement Django:

1. cd CoreFormulaPerformanceTest
    python -m venv venv
2. bash: source venv/bin/activate
3. pip install django
4. django-admin startproject CoreFormulaPerformanceTestProject .
5. python manage.py startapp core_inspector
6. move file urls.py into folder: core_inspector
7. move move and replace views.py into folder: core_inspector
8. python manage.py runserver
9. you will see like this:
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 25, 2023 - 09:44:36
Django version 4.2.4, using settings 'CoreFormulaPerformanceTestProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

it's mean the server already run and ready to throw response from outside into script and give back the response json after script already finished process 

6. after you run the server, don't forget to run CoreFormula.py