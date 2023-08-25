import json
import statistics
import time
from urllib.parse import urlparse

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def inspect_performance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inspector = PerformanceInspector()  # Assuming PerformanceInspector is defined in CoreFormula.py
            inspection_result_json = inspector.start_inspection(json.dumps(data))

            if inspection_result_json:
                return JsonResponse(json.loads(inspection_result_json))
            else:
                return JsonResponse({'error': 'Invalid inspection details.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


class PerformanceInspector:
    def __init__(self):
        pass

    def start_inspection(self, inspection_data):
        inspection_data = json.loads(inspection_data)
        site_url = inspection_data.get('website', '')
        num_visits = inspection_data.get('visits', 0)

        if not self.validate_url(site_url) or not isinstance(num_visits, int) or num_visits <= 0:
            return None

        response_times = []
        received_responses = []

        for _ in range(num_visits):
            start_time = time.time()
            response = requests.get(site_url)
            end_time = time.time()
            duration = end_time - start_time
            received_responses.append(response)
            response_times.append(duration)

        avg_duration = statistics.mean(response_times)
        duration_deviation = statistics.stdev(response_times) if len(response_times) > 1 else 0.0
        error_rate = (response_times.count(0) / num_visits) * 100
        reqs_per_second = num_visits / sum(response_times)
        min_duration = min(response_times)
        max_duration = max(response_times)

        received_kb_per_second = sum(len(response.content) / 1024 for response in received_responses) / sum(response_times)

        # Automatically calculate data_size
        data_size = num_visits * 5  # Adjust this factor as needed

        sent_kb_per_second = (num_visits * data_size) / sum(response_times) / 1024

        avg_bytes = sum(len(response.content) for response in received_responses) / len(received_responses)

        inspection_results = {
            "average_duration": avg_duration,
            "duration_deviation": duration_deviation,
            "error_rate": error_rate,
            "requests_per_second": reqs_per_second,
            "min_duration": min_duration,
            "max_duration": max_duration,
            "received_kb_per_second": received_kb_per_second,
            "sent_kb_per_second": sent_kb_per_second,
            "average_bytes": avg_bytes
        }

        return json.dumps(inspection_results)

    def validate_url(self, url):
        try:
            parsed_result = urlparse(url)
            return all([parsed_result.scheme, parsed_result.netloc]) and parsed_result.scheme in ["http", "https"]
        except:
            return False

if __name__ == "__main__":
    inspector = PerformanceInspector()

    example_inspection = '''
    {
        "website": "https://example.com",
        "visits": 50
    }
    '''

    inspection_result_json = inspector.start_inspection(example_inspection)

    if inspection_result_json:
        print("Performance Inspection Results:")
        print(inspection_result_json)
    else:
        print("Invalid inspection details.")
