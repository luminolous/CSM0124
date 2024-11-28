select k.nomor, group_concat(f.nama order by f.nama separator ',') as fasilitas
from kamar k 
inner join kamar_fasilitas kf on k.nomor = kf.kamar_nomor
inner join fasilitas f on kf.fasilitas_id = f.id
where k.tipe_kamar = 'Deluxe'
group by k.nomor;