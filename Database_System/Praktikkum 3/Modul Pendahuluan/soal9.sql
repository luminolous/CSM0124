select p.Alumni_A_NRP, count(pk.Pendataan_PD_ID) Jumlah_Kegiatan
from pendataan p 
inner join pendataan_kegiatan pk on p.PD_ID = pk.Pendataan_PD_ID
group by pk.Pendataan_PD_ID
order by Jumlah_Kegiatan desc;