INSERT INTO penyewa VALUES ('PY0007', 'Kamizato Ayato', '088899887788');
INSERT INTO tim_peminjam VALUES ('T00004', 'Genshin Badminton Club', 10);
INSERT INTO transaksi (
    tr_id, 
    tr_tgl_transaksi, 
    tr_tgl_sewa, 
    tr_waktu_mulai, 
    tr_lama_sewa, 
    tr_metode_pembayaran, 
    penyewa_id, 
    lapangan_id, 
    tim_id
) VALUES (
    'TR0006',
    '2024-11-10',
    CURRENT_DATE,
    CURRENT_TIME,
    3,
    'Transfer Bank',
    'PY0007',
    'LP0005',
    'T00004'
);
