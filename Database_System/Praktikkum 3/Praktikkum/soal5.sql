select k.nomor, k.nama_kamar, k.tipe_kamar
from kamar k 
inner join kamar_fasilitas kf on k.nomor = kf.kamar_nomor 
inner join fasilitas f on kf.fasilitas_id = f.id
where f.nama = 'Wi-Fi'; 