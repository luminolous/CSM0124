select a.A_NRP, a.A_Nama, k.Nama_Kg
from alumni a
inner join pendataan d on a.A_NRP = d.Alumni_A_NRP
inner join pendataan_kegiatan pk on d.PD_ID = pk.Pendataan_PD_ID 
inner join kegiatan k on pk.Kegiatan_ID_Kg = k.ID_Kg
where k.Nama_Kg = 'Diskusi Literasi Digital';