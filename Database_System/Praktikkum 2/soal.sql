create database praktikkum;

create table cleaning_service (
    cs_id char(6) primary key,
    cs_nama varchar(60),
    cs_telp varchar(15),
    cs_pengalaman int 
);

create table lapangan (
    lp_id char(6) primary key,
    lp_nama varchar(60),
    lp_alamat varchar(100),
    lp_jenis_lapangan varchar(50),
    lp_luas_lapangan float(2),
    lp_harga_sewa float(2)
);

create table pegawai (
    pg_id char(6) primary key,
    pg_nik char(16),
    pg_nama varchar(60),
    pg_gender char(1),
    pg_umur int,
    pg_telp varchar(15)
);

create table tim_peminjam (
    tim_id char(6) primary key,
    tim_nama varchar(50),
    tim_jumlah_anggota int
);

create table penyewa (
    py_id char(6) primary key,
    py_nama varchar(60),
    py_telp varchar(15)
);

create table cs_lapangan (
    lapangan_id char(6),
    cs_id char(6),
    primary key (lapangan_id, cs_id),
    constraint fk_lapangan_id foreign key (lapangan_id) references lapangan(lp_id)
    on update cascade
    on delete cascade,
    constraint fk_cs_id foreign key (cs_id) references cleaning_service(cs_id)
    on update cascade
    on delete cascade
);

create table transaksi (
    tr_id char(6) primary key,
    tr_tgl_transaksi date default current_date,
    tr_tgl_sewa date default current_date,
    tr_waktu_mulai time default current_time,
    tr_lama_sewa int,
    tr_pembuatan_membership boolean,
    tr_total_harga float(2),
    tr_metode_pembayaran varchar(15),
    pegawai_id char(6),
    penyewa_id char(6),
    lapangan_id char(6),
    tim_id char(6),
    constraint fk_pegawai_id foreign key (pegawai_id) references pegawai(pg_id)
    on update cascade
    on delete cascade,
    constraint fk_penyew_id foreign key (penyewa_id) references penyewa(py_id)
    on update cascade
    on delete cascade,
    constraint fk_lapangn_id foreign key (lapangan_id) references lapangan(lp_id)
    on update cascade
    on delete cascade,
    constraint fk_tim_id foreign key (tim_id) references tim_peminjam(tim_id)
    on update cascade
    on delete cascade
);

create table kartu_membership (
    mb_id char(6) primary key,
    mb_nik char(16),
    mb_alamat varchar(100),
    mb_tgl_pendaftaran date default current_date,
    mb_masa_berlaku int,
    penyewa_id char(6),
    constraint fk_penyewa_id foreign key (penyewa_id) references penyewa(py_id)
    on update cascade
    on delete cascade
);
