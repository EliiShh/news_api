# שם הפרויקט

## תיאור הפרויקט
פרויקט זה נבנה באמצעות ספריות פייתון כמו Kafka, Flask ו-pandas. הוא מאפשר עיבוד, אחסון והבאת נתונים בצורה יעילה ושימוש ברשת RPC.

## התקנה
1. ודא שיש לך Python 3.8+ וסביבת Virtualenv במערכת שלך.
2. התקן את כל התלויות הנדרשות על ידי הרצת:
    ```bash
    pip install -r requirements.txt
    ```

## שימוש
### הרצת שרת Flask
להפעלת שרת Flask בצע:
```bash
export FLASK_APP=app.py
flask run
