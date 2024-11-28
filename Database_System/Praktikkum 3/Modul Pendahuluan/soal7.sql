select a.P_NIK, a.P_Nama
from admin a
inner join pendataan p on a.P_NIK = p.Admin_P_NIK
inner join alumni al on p.Alumni_A_NRP = al.A_NRP
where al.A_Pekerjaan = 'Manager' and al.A_Nama != 'Restri Amalia';