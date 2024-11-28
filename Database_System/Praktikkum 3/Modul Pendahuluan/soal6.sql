select p.Alumni_A_NRP, count(pk.Pendataan_PD_ID) as Jumlah_Kegiatan
from pendataan p
inner join pendataan_kegiatan pk on p.PD_ID = pk.Pendataan_PD_ID
group by p.Alumni_A_NRP
having count(pk.Pendataan_PD_ID) >= 2;