INITIAL_PROMPT = """
Consider yourself a prompt engineering tutor. Your task is to assess and analyze the quality, clarity, and performance of user-submitted prompts for the given Exercise.

** Exercise: ** 
{exercise_content}


** User Prompt:**
{user_prompt}

**Instructions:**

1. **Criteria for Evaluation:**
   - **Clarity:** Assess if the prompt is clear and understandable. Is the language straightforward? Are there ambiguous terms?
   - **Specificity:** Evaluate how specific the prompt is. Does it provide enough detail for the AI to generate a focused output?
   - **Relevance:** Determine if the prompt is relevant to the intended context or task. Does it align with the expected outcome?
   - **Engagement:** Analyze if the prompt is engaging. Does it encourage creative or informative responses?
   - **Length:** Consider the length of the prompt. Is it too long, making it convoluted, or too short, lacking necessary details?

2. **Performance Metrics:**
   - **Expected Output:** Describe what type of response or information the prompt should ideally generate.
   - **Sample Outputs:** Generate 2 example responses from an AI model based on the provided prompt to illustrate potential outcomes.

3. **Feedback Generation:**
   - Provide constructive feedback based on the criteria assessed. Include suggestions for improvement, such as rephrasing, adding details, or simplifying language.
   - Highlight strengths of the prompt, if any, that could be retained in the revised version.

4. **Scoring System:**
   - Implement a scoring system (1-10 scale) for each criterion, where 10 represents outstanding quality and 1 signifies poor quality.
   - Calculate an overall score based on the average of the individual criteria scores.

**Output:**
- Return the output opnly and only HTML.
- HTML outputs should resonate with contemporary design trends while ensuring functionality and accessibility and attractiveness
- Summarize the evaluation results, including individual scores, overall score, and feedback for the user to enhance their prompt.
- Include a barchart for evaluation results on the top

"""


SAMPLE_RESPONSE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prompt Evaluation</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-gray-100 font-sans">
    <div class="container mx-auto p-8">
        <h1 class="text-3xl font-semibold mb-4 text-gray-800">Prompt Evaluation: Factorial Function</h1>

        <!-- Bar Graph -->
        <div class="bg-white shadow rounded-lg p-4 mb-4">
            <h2 class="text-xl font-medium mb-2 text-gray-700">Individual Scores</h2>
            <canvas id="scoreChart"></canvas>
        </div>

        <div class="bg-white shadow rounded-lg p-6 mb-4">
            <h2 class="text-2xl font-semibold mb-4 text-gray-800">Evaluation Results</h2>

            <div class="mb-4">
                <p class="font-medium text-gray-700"><strong>User Prompt:</strong> write a function to calculate factorial</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <h3 class="text-xl font-semibold mb-2 text-gray-700">Criteria Assessment</h3>
                    <ul class="list-disc list-inside text-gray-600">
                        <li><strong>Clarity:</strong> 4/10 - The prompt is understandable but lacks context.</li>
                        <li><strong>Specificity:</strong> 2/10 - Very vague; doesn't specify language, input/output types, or error handling.</li>
                        <li><strong>Relevance:</strong> 10/10 - Highly relevant to the task.</li>
                        <li><strong>Engagement:</strong> 1/10 - Doesn't encourage creative or informative responses.</li>
                        <li><strong>Length:</strong> 8/10 - Concise, but needs more detail.</li>
                    </ul>
                    <p class="text-lg font-semibold mt-2 text-gray-800">Overall Score: 5/10</p>
                </div>

                <div>
                    <h3 class="text-xl font-semibold mb-2 text-gray-700">Performance Metrics</h3>
                    <p class="text-gray-600"><strong>Expected Output:</strong> A Python function that takes an integer as input and returns its factorial.  It should ideally include error handling (e.g., for negative input) and docstrings. </p>
                    <h4 class="text-lg font-medium mt-4 mb-2 text-gray-700">Sample Outputs:</h4>
                    <div class="mb-2">
                        <p class="text-sm font-medium text-gray-700">Sample Output 1:</p>
                        <pre class="bg-gray-50 p-2 rounded text-sm text-gray-800">
                            <code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
                            </code>
                        </pre>
                    </div>
                    <div>
                        <p class="text-sm font-medium text-gray-700">Sample Output 2 (with potential issues):</p>
                        <pre class="bg-gray-50 p-2 rounded text-sm text-gray-800">
                            <code>
def factorial(x):
  result = 1
  for i in range(1, x+1):
    result *= i
  return result
                            </code>
                        </pre>
                    </div>
                </div>
            </div>

            <div>
                <h3 class="text-xl font-semibold mb-2 text-gray-700">Feedback and Suggestions</h3>
                <p class="text-gray-600">
                    The prompt is too vague and requires significant improvement. While the relevance is high, the lack of specificity results in unpredictable output.
                </p>
                <ul class="list-disc list-inside text-gray-600 mt-2">
                    <li><strong>Suggestion 1:</strong> Specify the programming language (Python).</li>
                    <li><strong>Suggestion 2:</strong> Mention the expected input and output types (integer input, integer output).</li>
                    <li><strong>Suggestion 3:</strong> Consider adding a constraint like "handle invalid input gracefully" or "include docstrings".</li>
                    <li><strong>Revised Prompt Example:</strong> "Write a Python function to calculate the factorial of a non-negative integer. Include error handling for invalid input (e.g., negative numbers) and add a docstring explaining the function's purpose."</li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        // JavaScript to create the bar chart
        const ctx = document.getElementById('scoreChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Clarity', 'Specificity', 'Relevance', 'Engagement', 'Length'],
                datasets: [{
                    label: 'Score',
                    data: [4, 2, 10, 1, 8],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 10
                    }
                }
            }
        });
    </script>
</body>
</html>
'''