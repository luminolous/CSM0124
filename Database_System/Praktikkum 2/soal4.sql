alter table lapangan
drop foreign key fk_jenis_lapangan_id;

alter table lapangan
drop column jenis_lapangan_id;

drop table jenis_lapangan;

alter table lapangan
add column lp_jenis_lapangan varchar(50),
add column lp_luas_lapangan float(2),
add column lp_harga_sewa float(2);