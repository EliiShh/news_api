def process_content(content, client):
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"{content}  \n\n"
                               "אתה צריך להחזיר לי JSON של התוצאות הבאות על פי ניתוח האובייקט שנשלח אליך\n"
                               "\"city_name\": ,\n"
                               "\"country_txt\": ,\n"
                               "\"region_txt\":\n}\n"
                               "\"return me the region of the world it happened from among the following regions: ['Central America & Caribbean', 'North America', 'Southeast Asia', 'Western Europe', 'East Asia', 'South America', 'Eastern Europe', 'Sub-Saharan Africa', 'Middle East & North Africa', 'Australasia & Oceania', 'South Asia', 'Central Asia']\n"
                               "בבקשה שלח אך ורק את הJSON ללא תוספות של מילים של נימוס או סיכום\n"
                               "זה יהרוס לי את התוצאה\n"
                               "אני רוצה אך ורק את ה DICT"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        result = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                result += chunk.choices[0].delta.content or ""
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



