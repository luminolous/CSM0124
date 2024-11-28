select A.P_NIK, A.P_Nama, P.PD_ID
from Admin A
inner join pendataan P on A.P_NIK = P.Admin_P_NIK
where PD_ID = 'PD0010' or PD_ID = 'PD0011' or PD_ID = 'PD0012' or PD_ID = 'PD0013' or PD_ID = 'PD0014' or PD_ID = 'PD0015'
group by PD_ID;