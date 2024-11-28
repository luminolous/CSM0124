select sum(DATEDIFF(o.tanggal_checkout, o.tanggal_checkin) * k.harga_per_malam) AS jumlah_uang,
avg(DATEDIFF(o.tanggal_checkout, o.tanggal_checkin) * k.harga_per_malam) AS ratarata_uang
from order o
join order_kamar ok on o.id = ok.order_id
join kamar k on ok.kamar_nomor = k.nomor;