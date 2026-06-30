from datetime import datetime

def generate_report(prediction, confidence):

    report = f"""
Voice Gender Analysis Report

Prediction: {prediction}

Confidence: {confidence}

Date: {datetime.now()}
"""

    return report