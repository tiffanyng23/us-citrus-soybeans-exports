-- Export datasets on US citrus fruit and soybean export values from 2002-2020

SELECT 
	year, 
	month, 
	citrus_export_value,
	ROUND(AVG(citrus_export_value) OVER(ORDER BY YEAR, MONTH ROWS BETWEEN 11 PRECEDING AND CURRENT ROW),0) AS twelve_month_citrus_export_avg,
	soybeans_export_value,
	ROUND(AVG(soybeans_export_value) OVER(ORDER BY YEAR, MONTH ROWS BETWEEN 11 PRECEDING AND CURRENT ROW),0) AS twelve_month_soybean_export_avg
FROM us_exports;

SELECT 
	year, 
	ROUND(AVG(citrus_export_value),2) AS avg_citrus_export_value,
	ROUND(SUM(citrus_export_value), 2) AS total_citrus_export_value,
	ROUND(AVG(soybeans_export_value), 2) AS avg_soybeans_export_value,
	ROUND(SUM(soybeans_export_value), 2) AS total_soybeans_export_value
FROM us_exports
GROUP BY year
ORDER BY year;