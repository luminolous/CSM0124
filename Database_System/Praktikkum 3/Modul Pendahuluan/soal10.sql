select a.P_Nama, count(ah.Admin_P_NIK) as Total_shift
from admin a
inner join admin_shift ah on a.P_NIK = ah.Admin_P_NIK
where a.P_JenisKelamin = 'L'
group by ah.Admin_P_NIK;