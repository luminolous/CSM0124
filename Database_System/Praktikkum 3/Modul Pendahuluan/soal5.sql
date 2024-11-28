SELECT a.P_NIK, p.PD_ID
FROM admin a
INNER JOIN pendataan p ON a.P_NIK = p.Admin_P_NIK
INNER JOIN alumni al ON p.Alumni_A_NRP = al.A_NRP
WHERE al.A_Pekerjaan = 'Dosen';
