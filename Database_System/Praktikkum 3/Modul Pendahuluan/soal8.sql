SELECT A.A_Pekerjaan AS Pekerjaan, COUNT(A.A_NRP) AS Jumlah_Alumni
FROM alumni A
GROUP BY A.A_Pekerjaan
ORDER BY COUNT(A.A_NRP) DESC;