select r.nama_resepsionis, count(*) as jumlah_kamar
from resepsionis r 
inner join `order` o on r.id = o.resepsionis_id
group by r.nama_resepsionis
having count(*) > 2;