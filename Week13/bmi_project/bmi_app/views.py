import os
from django.shortcuts import render
from google import genai
import markdown


def bmi_calculator(request):
    bmi = None
    category = None
    plan_html = None
    error_message = None

    if request.method == "POST":
        try:
            weight = float(request.POST.get("weight"))
            height_cm = float(request.POST.get("height"))
            age = int(request.POST.get("age"))
            gender = request.POST.get("gender")

            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 20:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            else:
                category = "Overweight"


            client = genai.Client(api_key="")

            prompt = f"""
                    Create a simple one-month diet and exercise plan.

                    Person details:
                    - Age: {age}
                    - Gender: {gender}
                    - Weight: {weight} kg
                    - Height: {height_cm} cm
                    - BMI: {bmi}
                    - BMI Category: {category}

                    Requirements:
                    - Write at least 3–5 sentences per section
                    - Provide a structured plan for each week

                    Format:

                    ## Week 1
                    Diet Plan:
                    Exercise Plan:

                    ## Week 2
                    Diet Plan:
                    Exercise Plan:

                    ## Week 3
                    Diet Plan:
                    Exercise Plan:

                    ## Week 4
                    Diet Plan:
                    Exercise Plan:

                    Use clear explanations and practical advice.
                """

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "top_k": 40,
                    "max_output_tokens": 2000,
                }
            )
            print(response)
            plan = response.candidates[0].content.parts[0].text
            plan_html = markdown.markdown(plan)

        except Exception as e:
            error_message = f"Error: {e}"

    return render(request, "bmi_app/bmi_form.html", {
        "bmi": bmi,
        "category": category,
        "plan": plan_html,
        "error_message": error_message,
    })