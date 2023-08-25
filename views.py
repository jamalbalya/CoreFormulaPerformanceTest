import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CoreFormula import PerformanceInspector

@csrf_exempt
def check_performance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inspector = PerformanceInspector()
            inspection_result_json = inspector.start_inspection(json.dumps(data))

            if inspection_result_json:
                return JsonResponse(json.loads(inspection_result_json))
            else:
                return JsonResponse({'error_message': 'Sorry, the inspection details provided seem to be invalid.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error_message': 'Oops! The JSON data appears to be in an incorrect format.'}, status=400)

    return JsonResponse({'error_message': 'This request method is not supported.'}, status=405)
