select GROUP_CONCAT(p.nama_pelanggan, o.jumlah_kamar, o.id order by p.nama_pelanggan, o.jumlah_kamar, o.id SEPARATOR ', ') as Detail_pesanan
from `order` as o
inner join pelanggan p on o.pelanggan_NIK = p.NIK 
where p.nama_pelanggan = 'Daniel Martinez';