create table jenis_lapangan (
    jl_id char(6),
    jl_nama varchar(100),
    jl_luas_lapangan float(2),
    jl_harga_sewa float(2)
);

alter table jenis_lapangan
add primary key (jl_id),

alter table lapangan
add column jenis_lapangan_id char(6) not null,
add constraint fk_jenis_lapangan_id foreign key (jenis_lapangan_id) references jenis_lapangan(jl_id);

alter table lapangan
drop column lp_jenis_lapangan,
drop column lp_luas_lapangan,
drop column lp_harga_sewa;