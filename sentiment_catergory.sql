SELECT Sentiment_Score,

CASE 
WHEN Sentiment_Score > 0.5 THEN 'POSITIVE'
WHEN Sentiment_Score BETWEEN -0.5 AND 0.5 THEN 'NEUTRAL' 
WHEN Sentiment_Score < 0.5 THEN 'NEGATIVE'
ELSE 'UNKNOWN'
END AS Sentiment_Catergory,
COUNT(*) AS Sentiment_Count

FROM reddit_sentiment_analysis_20250221_214540

GROUP BY Sentiment_Catergory;
