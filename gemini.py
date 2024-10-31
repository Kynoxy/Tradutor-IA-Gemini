import google.generativeai as genai

google_API_KEY = "AIzaSyDL5I81qRPazb3o0_pDslcY-7CH-EDTeus"

genai.configure(api_key=google_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
while True:

    prompt = input("\ndigite sua pergunta: ")
    response = model.generate_content(prompt)
    print(response.text)
    continuar = input("\nDeseja continuar? (s/n):")

    if continuar.lower() != 's':
            break