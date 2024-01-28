#accuracy function
def calculate_performance_metrics (TP, FP, TN, FN):
	total_cases = TP + FP + TN + FN
	accuracy = (TP + TN) / total_cases if total_cases > 0 else 0 
	precision = TP / (TP + FP) if TP + FP > 0 else 0
	recall = TP / (TP + FN) if TP + FN > 0 else 0 
	f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
	
	return accuracy, f1_score

#Example1
test_cases = [{'TP': 30, 'FP': 10, 'TN': 50, 'FN': 10}]

for case in test_cases:
	accuracy, f1_score = calculate_performance_metrics(case['TP'], case['FP'], case['TN'], case['FN'])
	print(f"Accuracy: {accuracy:.2f}, F1 Score: {f1_score:.2f}")

#Example2
test_cases = [{'TP': 50, 'FP': 15, 'TN': 20, 'FN': 15}]

for case in test_cases:
	accuracy, f1_score = calculate_performance_metrics(case['TP'], case['FP'], case['TN'], case['FN'])
	print(f"Accuracy: {accuracy:.2f}, F1 Score: {f1_score:.2f}")
	
#Example3
test_cases = [{'TP': 70, 'FP': 10, 'TN': 10, 'FN': 10}]

for case in test_cases:
	accuracy, f1_score = calculate_performance_metrics(case['TP'], case['FP'], case['TN'], case['FN'])
	print(f"Accuracy: {accuracy:.2f}, F1 Score: {f1_score:.2f}")