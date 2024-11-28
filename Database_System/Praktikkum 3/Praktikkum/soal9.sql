select f.nama, count(*) as banyak_digunakan
from fasilitas f 
inner join kamar_fasilitas kf on f.id = kf.fasilitas_id
group by kf.kamar_nomor
order by banyak_digunakan desc;
