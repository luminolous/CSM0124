select p.NIK, p.nama_pelanggan, p.no_telp, k.nomor, k.nama_kamar, k.tipe_kamar
from pelanggan p 
inner join `order` o on p.NIK = o.pelanggan_NIK
inner join pembayaran pe on o.id = pe.order_id
inner join order_kamar ok on o.id = ok.order_id
inner join kamar k on ok.kamar_nomor = k.nomor
where pe.status = 'Belum Lunas';